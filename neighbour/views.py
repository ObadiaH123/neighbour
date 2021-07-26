from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import NeighbourForm, UploadForm,ProfileForm,UpdateUserForm,UpdateUserProfileForm, Neighbour
from .models import Post,Profile, Healthcenter, Business
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    post = Post.images()
    neighbour=Neighbour.objects.all
    users = User.objects.exclude(id=request.user.id)
    return render(request,'index.html', {"images":post[::1],"users":users, 'neighbour':neighbour})

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

@login_required(login_url='/accounts/login/')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You did not make a selection"
    return render(request, 'results.html', {'message': message})

@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.images.all()
    

    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,
    
    }
    return render(request, 'user_profile.html', params)

def health(request):
    karen = Healthcenter.objects.get(pk=3)
    kenyatta= Healthcenter.objects.get(pk=5)


    return render(request, 'health.html', {"karen":karen, "kenyatta":kenyatta})


def business(request):
    factory = Business.objects.get(pk=3)
    hardware= Business.objects.get(pk=1)


    return render(request, 'business.html', {"factory":factory, "hardware":hardware})

def neighbour(request):
    if request.method == 'POST':
        form = NeighbourForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            neighbour = form.save(commit=False)
            neighbour.user = request.user.profile
            neighbour.save()
            return redirect('index')
    else:
        form = NeighbourForm()
    return render(request,'neighbour.html', {"form":form})

def emergency(request):
    police = Business.objects.get(pk=1)
    fire= Business.objects.get(pk=2)


    return render(request, 'emergency.html', {"police":police, "fire":fire})
