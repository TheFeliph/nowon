from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect, render
from django import forms
from django.http import JsonResponse
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt

def run_migrations():
    call_command('migrate')

run_migrations()

User = get_user_model()
if not User.objects.filter(username='user').exists():
    User.objects.create_user(username='user', password='user')

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

@csrf_exempt
def nowonfeed_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form = PostForm()
    posts = request.session.get('posts', [])

    if request.method == 'POST':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            content = request.POST.get('content')
            if content:
                posts.insert(0, content)
                request.session['posts'] = posts
                return JsonResponse({'new_post': content, 'username': request.user.username})
            else:
                return JsonResponse({'error': 'Invalid content'}, status=400)

        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.cleaned_data['content']
            posts.insert(0, new_post)
            request.session['posts'] = posts

    return render(request, 'nowonfeed/feed.html', {'form': form, 'posts': posts})

def logout_view(request):
    logout(request)
    return redirect('login')
