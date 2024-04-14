import os
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from userprofile.models import Profile, FollowerCount, Contact
from posts.models import Post
from userprofile.forms import MyLoginForm, SignUpForm

# Create your views here.
@login_required(login_url="login", redirect_field_name='login')
def index(request):
    context = {}
    template_file = os.path.join("posts", "home.html")
    user_profile = Profile.objects.get(user=request.user)
    post_objs = Post.objects.all()
    
    context = {
        "user_profile": user_profile,
        "posts": post_objs
    }
    return render(request, template_file, context)

@login_required(login_url="login")
def settings(request):
    template_file = os.path.join("user", "general_setting.html")

    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # If the profile doesn't exist, create a new one for the user
        user_profile = Profile.objects.create(user=request.user, id_user=request.user.id)

    if request.method == "POST":
        profile_pic = request.FILES.get("profile_pic")
        bio = request.POST.get("bio")
        location = request.POST.get("location")
        
        if location:
            user_profile.location = location
        if profile_pic is None:
            profile_pic = user_profile.profile_pics
        user_profile.profile_pics = profile_pic
        user_profile.bio = bio
        user_profile.save()

        return redirect('/')

    context = {
        "user_profile": user_profile
        }
    return render(request, template_file, context)

def login_view(request):
    template_file = os.path.join("user", "signin.html")
    if request.method == "POST":
        form = MyLoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('/home')
            error_message = {
                "message": "Invalid credential"
                }

            return render(request, template_file, error_message)
    else:
        form = MyLoginForm()
    context = {"form": form}
    return render(request, template_file, context)

def signup_view(request):
    template_file = os.path.join("user", "signup.html")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            
            form.save()
            user_obj = User.objects.get(username=username)
            
            new_profile = Profile.objects.create(user=user_obj,
                                            id_user=user_obj.id)
            new_profile.save()

            return render(request, template_file)
    else:
        form = SignUpForm()
    context = {"form": form}
    return render(request, template_file, context)

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='login')
def profile(request):
    template_file = os.path.join('user', "main_profile.html")
    context = dict()
    user_profile = Profile.objects.filter(user=request.user).first()
    post_objs = Post.objects.filter(user=request.user.username)
    context["num_following"] = FollowerCount.objects.filter(follower=request.user.username).count()
    context["num_follower"] = FollowerCount.objects.filter(user=request.user.username).count()
    context["user_profile"] = user_profile
    context["posts"] = post_objs
    return render(request, template_file, context)

@login_required(login_url="login")
def follow_user(request):
    if request.method == 'POST':
        new_follower = request.user.username
        new_following = request.POST.get("following")
        
        
        is_previous_following = FollowerCount.objects.filter(
            follower=new_follower, 
            user=new_following
            ).exists()
        if not is_previous_following:
            follow_obj = FollowerCount(follower=new_follower, user=new_following)
            follow_obj.save()
        else:
            FollowerCount.objects.filter(follower=new_follower, user=new_following).delete()
        return redirect(f'user/{new_following}')
    return redirect('/')

def about_view(request):
    template_file = os.path.join('public', 'about.html')
    return render(request, template_file)

def faq_view(request):
    template_file = os.path.join('public', 'faq.html')
    return render(request, template_file)

def about_view(request):
    template_file = os.path.join('public', 'about.html')
    return render(request, template_file)

def contact_view(request):
    template_file = os.path.join('public', 'contact.html')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact_obj = Contact(name=name, email=email, message=message)
        contact_obj.save()
        message = {"message": 'Your request is successfully sent'}
        return render(request, template_file, message)

    return render(request, template_file)

def features_view(request):
    template_file = os.path.join('public', 'features.html')
    return render(request, template_file)