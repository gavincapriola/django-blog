from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            messages.success(
                request, "Your account has been created! You're now able to log in")
            form.save()
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
