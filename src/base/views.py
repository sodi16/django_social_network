from django.contrib.auth import authenticate, login, logout, get_user_model, get_user
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LoginView
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, DetailView
from base.models import User, Post
from base.forms import LoginForm, PostForm, RegisterForm
from base.forms import ProfilPictureForm


def index(request):
    user = request.user
    if user.is_authenticated:
        return feed(request)
    else:
        return render(request, 'base/home.html', context={'user': user})


@login_required
def feed(request):
    """
    Feed is the main home after user is logged, he can his friends/strangers publications
    """
    posts = Post.objects.all()
    # display all user connections's posts
    # user = get_user(request)
    # posts = [post for connection in user.connections.all() for post in connection.posts.all()]
    return render(request, 'base/feed.html', {'posts': posts})

    # paginator
    # paginator = Paginator(posts, 5)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # return render(request, 'base/feed.html', {'posts': posts, 'page_obj': page_obj})


def logout_user(request):
    logout(request)
    return redirect('login_page')


class Login(LoginView):
    template_name = 'base/login.html'
    redirect_authenticated_user = True


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profil', pk=user.pk)
    return render(request, 'base/register.html', {'form': form})


class UserList(ListView):
    model = User
    template_name = 'base/all_users_list.html'
    context_object_name = 'users'


class UserDetail(DetailView):
    model = User
    template_name = 'base/profil.html'
    context_object_name = "user"


@login_required
def profil_page(request, pk):
    context = {}
    user = get_object_or_404(User, pk=pk)
    if pk == get_user(request).pk:
        context['']
    return render(request, 'base/profil.html')


@login_required
def connections(request):
    user = get_user(request)
    return render(request, 'base/user_connections.html', {'user': user})

@permission_required('base.filter_user')
@login_required
def messages(request):
    return render(request, 'base/messages.html')


@login_required
def post_page(request, pk):
    """
    Display the page of a unique post, it can be a image or only content text
    """
    return render(request, 'base/post_page.html', context={'pk': pk})


@login_required
def blog_and_photo_upload(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user = get_user(request)
            post = Post.objects.create(image=form.cleaned_data['image'], content=form.cleaned_data['content'],
                                title=form.cleaned_data['title'], author=user)
            user.posts.add(post)
            user.save()
            return redirect('home')
    return render(request, 'base/upload_post.html', {'form': form})


@login_required
def add_profil_picture(request):
    form = ProfilPictureForm()
    if request.method == 'POST':
        print('ENTERED IN POST')
        form = ProfilPictureForm(request.POST, request.FILES)
        if form.is_valid():
            user = get_user(request)
            user.profil_picture = request.FILES['profil_pic']
            user.save()
            return redirect('profil', pk=user.pk)
    return render(request, 'base/change_profil_picture.html', {'form': form})


def search_user(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        results = User.objects.filter(Q(username__contains=query) | Q(first_name__contains=query) |
                                       Q(last_name__contains=query))
        return render(request, 'base/search_user.html', {'results': results})


