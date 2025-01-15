from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, get_user_model
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout

User = get_user_model()

def register_view(request):

    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password1'))
            new_user.save()
            new_user = authenticate(
                username = form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            if new_user is not None:
                login(request, new_user)
            return redirect('home')
        print('THE USER IS REGISTERED SUCCESSFULLY')
    else:
        print('THE USER CANNOT BE REGISTERED')
        form=UserRegisterForm()

    context = {
        'form':form,
        'right':True,
    }

    return render(request, 'userauths/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email=request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except Exception as e:
            print(e)
            messages.warning(request, f'User with email {email} does not exist')
        user = authenticate(request=request, email=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid email or password')


    context = {

    }

    return render(request, 'userauths/login.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('userauths:login')