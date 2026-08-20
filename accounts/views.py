from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import RegisterForm

from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    if request.user.role == 'PATIENT':
        return render(
            request,
            'accounts/patient_dashboard.html'
        )

    elif request.user.role == 'DOCTOR':
        return render(
            request,
            'accounts/doctor_dashboard.html'
        )

    elif request.user.role == 'LAB':
        return render(
            request,
            'accounts/lab_dashboard.html'
        )

    elif request.user.role == 'PHARMACY':
        return render(
            request,
            'accounts/pharmacy_dashboard.html'
        )

    return redirect('core:home')


def register(request):

    if request.user.is_authenticated:
        return redirect('core:home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            messages.success(
                request,
                'Account created successfully. Please log in.'
            )

            return redirect('accounts:login')

    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('accounts:dashboard')

        messages.error(
            request,
            'Invalid username or password.'
        )

    return render(
        request,
        'accounts/login.html'
    )


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('accounts:login')