from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from .models import Post


def home(request):
    posts = Post.objects.all()

    return render(request, "blog/home.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post_detail.html", {"post": post})


def post_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        slug = slugify(title)

        Post.objects.create(
            title=title,
            slug=slug,
            content=content
        )

        return redirect("home")

    return render(request, "blog/post_create.html")


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.slug = request.POST["slug"]
        post.content = request.POST["content"]

        post.save()

        return redirect("post_detail", slug=post.slug)

    return render(request, "blog/post_edit.html", {"post": post})