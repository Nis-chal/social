from django.shortcuts import render,redirect


from django.contrib import messages



from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from profile_app.forms import UserForm,UserProfileInfoForm


from .auth import unauthenticated_user


# Create your views here.

def index(request):
    context = {
        'active_homepage':'active'
    }
    return render(request,'landing_page.html',context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


@unauthenticated_user
def register(request):
# while you register you fill two form for profile and user where two form is passed
# and hashing algorithm is used to hash the password while saving using .set_password method

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            messages.add_message(request, messages.SUCCESS, 'User registered successfully')
            return redirect ('/account/user_login')
        else:
             messages.add_message(request, messages.ERROR, 'Something went wrong')
             return render(request, 'login_register_app/registration.html', {'user_form':user_form,'profile_form':profile_form}) 
        

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        context ={
            'user_form':user_form,'profile_form':profile_form,'active_register':'active',

        }

    return render(request,'login_register_app/registration.html',context)

#if the user is active then they are logged in and sent to post_list page
@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =authenticate(request,username = username ,password= password)

        if user:
            
            if not user.is_staff:
                login(request,user)
                return redirect('/post/post_list')

            elif user.is_staff:
                login(request,user)
                return redirect('/admins/admins')


            else:
                
                return render(request,'login_register_app/login.html',{})
        else:
           messages.add_message(request, messages.ERROR, 'Invalid Username or Password')
           return render(request,'login_register_app/login.html',{'active_login':'active'})

    else:
        return render(request,'login_register_app/login.html',{'active_login':'active'})

def Not_found(request):
    return render(request,'not_found.html')