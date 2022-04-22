from datetime import datetime
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import (Post, Music, Comment, MusicComment)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostCreateForm, CommentForm, MusicCommentForm



def home (request):
    top_posts = Post.objects.filter(created__day = datetime.now().day, special=True)[:5] 
    trending_posts = Post.objects.filter(trending=True).order_by('-created')[:10]
    print(top_posts)
    news_posts = Post.objects.all().order_by('-created')[:15]
    music_posts = Music.objects.all().order_by('-posted_on')[:15]
    return render(request, 'blog/home.html', context={
        'news_posts':news_posts,
        'music_posts':music_posts,
        'top_posts': top_posts,
        'trending_posts':trending_posts,
    })

def detail(request,slug ):
    news_post  = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post = news_post)
    related_news = Post.objects.filter(category=news_post.category).order_by('-created')[:8]
    if request.method == 'POST':
        commentform  = CommentForm(request.POST)
        if commentform.is_valid():
            commentform.save(commit = False)
            if not request.user.is_authenticated:
                commentform.instance.author = 'anonymous'
                commentform.instance.post = news_post
                commentform.save()
                messages.success(request, 'comment submitted for processing')
            commentform.instance.author = request.user
            commentform.instance.post = news_post
            commentform.save()
            messages.success(request, 'comment submitted for processing')
            return redirect(reverse('detail', kwargs={'slug':news_post.slug}))
    comment_form = CommentForm()
    context = {
        'post': news_post,
        'comments':comments,
        'commentform' : comment_form,
        'related' : related_news
    }
    return render(request, 'blog/detail.html', context)

def musics(request):
    songs = Music.objects.all().order_by('category')
    return render(request, 'blog/music.html', context={'songs':songs})
def news(request):
    news = Post.objects.all()
    return render(request, 'blog/news.html', context={'news':news})
def trending(request):
    trending_posts = Post.objects.filter(trending=True).order_by('-created')
    return render(request, 'blog/trending.html', context={'trending_posts':trending_posts})
    
def music_page(request,slug ):
    music_post  = Music.objects.get(slug=slug)
    comments = MusicComment.objects.filter(post = music_post)
    related = Music.objects.filter(category=music_post.category).exclude(title=music_post.title).order_by('-posted_on')[:10]
    title= music_post.title
    print(music_post.title)
    print(music_post.uploader)

    if request.method == 'POST':
        commentform  = MusicCommentForm(request.POST)
        if commentform.is_valid():
            commentform.save(commit = False)
            if not request.user.is_authenticated:
                commentform.instance.author = 'anonymous'
                commentform.instance.post = music_post
                commentform.save()
                messages.success(request, 'comment submitted for processing')
            commentform.instance.author = request.user
            commentform.instance.post = music_post
            commentform.save()
            messages.success(request, 'comment submitted for processing')
            return redirect(reverse('music_page', kwargs={'slug':music_post.slug}))
    comment_form = MusicCommentForm()
    context = {
        'title': title,
        'music': music_post,
        'comments':comments,
        'commentform' : comment_form,
        'related' : related
    }
    return render(request, 'blog/music_page.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST,request.FILES)
        if form.is_valid():
            print('validated')
            form.save(commit = False)
            # if not  request.user.is_authenticated:
            #     form.instance.author  = 'anonymous user'
            form.instance.author = request.user
            post = form.save()
            messages.success(request, 'Post created successfully' )
            return redirect(reverse('detail', kwargs={'slug': post.slug}))
    form = PostCreateForm()
    return render(request, 'blog/create.html', context={'form': form})


def edit_post(request, slug):
    post = Post.objects.get(slug = slug)
    if request.method == 'POST': 
        form = PostCreateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'post successfully edited')
            return redirect(reverse('detail', kwargs={'slug': post.slug}))
        messages.error(request, 'post editing unsucccessful')
    form = PostCreateForm(instance=post)
    return render(request, 'blog/edit.html', context={'form':form})

def delete_post(request,slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'blog/delete.html' ,context={'post':post})
