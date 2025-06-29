from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, VoteForm
from .models import Candidate, Vote
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('voting')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('admin:index')  # Redirect to Django admin home page
        else:
            return HttpResponse("Invalid credentials or not an admin", status=403)
    return render(request, 'admin_login.html')

@login_required
def voting(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.user = request.user
            vote.save()
            vote.candidate.total_votes += 1
            vote.candidate.save()
            return redirect('results')
    else:
        form = VoteForm()
        form.fields['candidate'].queryset = Candidate.objects.all()
    return render(request, 'voting.html', {'form': form})

@login_required
def results(request):
    candidates = Candidate.objects.order_by('-total_votes')
    return render(request, 'results.html', {'candidates': candidates})

def forgot_password(request):
    # Implement password reset functionality
    return render(request, 'forgot_password.html')