from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadForm,ProfileForm,UpdateUserForm,UpdateUserProfileForm,CommentForm
from .models import Image,Profile,Follow,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.images()
    users = User.objects.exclude(id=request.user.id)
    return render(request,'index.html', {"images":images[::1],"users":users})

def post(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return redirect('index')
    else:
        form = UploadForm()
    return render(request,'post_image.html', {"form":form})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    images = request.user.profile.images.all()
    print(images)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,
    }
    return render(request, 'profile.html', params)

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('profile')
    else:
        form = UploadForm()
    return render(request,'edit_profile.html',{"form":form})
