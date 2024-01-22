from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.form import CreateUserForm
from app.models import Post, Contact, Comment


def index(request):
    post = Post.objects.all()[:3]
    # count = Comment.objects.count()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        c = Contact(name=name, phone_number=phone_number, subject=subject, message=message)
        c.save()
        return redirect('index')

    context = {'posts': post}
    return render(request, 'index.html', context)


def single(request, id):
    post = Post.objects.filter(id=id).first()
    recent = Post.objects.all()[:3]
    comment = Comment.objects.filter(post=id).order_by('-id')
    count = Comment.objects.filter(post=id).count()
    if request.method == 'POST':
        username = request.user.username
        text = request.POST.get('text')
        posts = id

        c = Comment(username=username, text=text, post=posts)
        c.save()

    context = {'post': post, 'recent_posts': recent, 'comments': comment, 'count': count}
    return render(request, 'single.html', context)


def posts(request):
    post = Post.objects.all().order_by('-id')
    # count = Comment.objects.count()
    context = {'posts': post}
    return render(request, 'posts.html', context)


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password incorrect')

    context = {}

    return render(request, 'registration/login.html', context)


def custom_logout(request):
    logout(request)
    return redirect('index')

