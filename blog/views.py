from .forms import PostForm
from django.shortcuts import render
from django.utils import timezone
from .models import Post, User
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

# add a new line
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    print(posts,'postssssssssssssss')
    context = {'posts':posts}
    return render(request, 'blog/post_list.html',context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post,'got this post')
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# create a new views for sign-up page
@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        state = request.POST.get('state')
        city = request.POST.get('city')
        country = request.POST.get('country')
        image = request.FILES.get('image')

        user = User.objects.create_user(username=username,email=email,password=password,state=state,city=city,country=country,image=image)
        if user:
            return redirect("post_list")

    # messages.info(request,"Applications submited")

    return render(request, 'blog/sign_up.html')

# create a new views for login page
@csrf_exempt
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
       

        if user :
            print('inside ifffffffff')
            login(request, user)
            # Redirect to a success page or user dashboard
            return redirect('post_list')  # Replace 'home' with your desired URL name
        else:
            # Handle invalid login (e.g., display an error message)
            messages.error(request, 'Invalid username or password.')
        

   
    return render(request, 'blog/login.html')

def sign_out(request):
    logout(request)
    return redirect("post_list")


# create a new views for profile page
@csrf_exempt
def profile_page(request):
    user = request.user
    context = {'profile':user}
    return render(request, 'blog/profile.html',context)

# create a new views for edit page
def edit_page(request):
    user = request.user
    context = {'edit':user}
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        state = request.POST.get('state')
        city = request.POST.get('city')
        country = request.POST.get('country')
        image = request.FILES.get('image')

        # user = User.objects.update.user(username=username,email=email,password=password,state=state,city=city,country=country,image=image)
        user.email = email
        user.username = username
        user.password = password
        user.state = state
        user. city = city
        user. country = country
        user. image = image
        user.save()
        
        return redirect("profile")
        
    return render(request, 'blog/edit.html', context)


    
