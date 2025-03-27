from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (
    CustomUserCreationForm, 
    LoginForm, 
    ProfilePhotoForm, 
    CustomUserChangeForm,
    CustomPasswordChangeForm,
)
from django.contrib.auth.forms import PasswordChangeForm

def register_view(request):
    """
    Handle user registration
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard:index')  # Redirects to dashboard after successful registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    """
    Handle user login
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('dashboard:index')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    """
    Handle user logout
    """
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('index')

# @login_required
# def profile_view(request):
#     """
#     Display user profile
#     """
#     print(request.user.profile_photo.url)
#     return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def profile_view(request):
    """
    Display user profile
    """
    # Safely handle profile photo
    try:
        profile_photo_url = request.user.profile_photo.url if request.user.profile_photo else None
    except (ValueError, AttributeError):
        profile_photo_url = None
    
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'profile_photo_url': profile_photo_url
    })

@login_required
def profile_photo_upload(request):
    """
    Handle profile photo upload
    """
    if request.method == 'POST':
        form = ProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile photo updated successfully!')
            return redirect('accounts:profile')
    else:
        form = ProfilePhotoForm(instance=request.user)
    
    return render(request, 'accounts/profile_photo_upload.html', {'form': form})

@login_required
def edit_profile(request):
    """
    Handle profile editing
    """
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def change_password(request):
    """
    Handle password change
    """
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Password changed successfully!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    
    return render(request, 'accounts/change_password.html', {'form': form})