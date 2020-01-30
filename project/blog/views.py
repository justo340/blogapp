from django.shortcuts import render


posts =[
 {
    'author': 'justo',
    'title': 'blog post 1',
    'content': 'first post content',
    'date_posted': 'july 27, 2019'
 },
{
    'author': 'peter',
    'title': 'blog post 2',
    'content': 'second post content',
    'date_posted': 'july 28, 2019'
 }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
