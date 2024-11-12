from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django import forms
from django.http import JsonResponse

class PostForm(forms.Form):
    content = forms.CharField(max_length=280)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'user' and password == 'user':
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('nowonfeed')
    return render(request, 'nowonfeed/login.html')

def nowonfeed_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form = PostForm()
    posts = request.session.get('posts', [])

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.cleaned_data['content']
            posts.insert(0, new_post)
            request.session['posts'] = posts
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'new_post': new_post, 'username': request.user.username})

    return render(request, 'nowonfeed/feed.html', {'form': form, 'posts': posts})

def logout_view(request):
    logout(request)
    return redirect('login')
