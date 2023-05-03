from tkinter.tix import Form
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from project.forms import PostCreateFrom, PostModifyFrom, CommentCreateForm
from project.models import Post, Comment
from django.contrib.auth.decorators import login_required

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html",{
        "post_list" : Post.objects.order_by("-created_at").all() ,
        "post_form" : PostCreateFrom() 

    })
def post_list_view(request: HttpRequest, ) -> HttpResponse:
    return render(request, "post.html",{
        "post_list": Post.objects.all()
    })

def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    return render (request, "post.html",{
        "post" : get_object_or_404(Post, pk=pk),
        "comments" : Comment.objects.filter(post__pk=pk),
        "comment_form" : CommentCreateForm()

    }) 

@login_required   
def post_create_view(request: HttpRequest, ) ->HttpResponse:
    
    if request.method != "POST" :
        return redirect("project:home")
    
    form = PostCreateFrom(request.POST, request.FILES)
    

    if form.is_valid():
        post = form.save(request.user, True)
        return redirect("project:posts", post.pk)
    # print(form.errors)    
    return redirect("project:home")    


@login_required
def post_delete_view(request: HttpRequest, pk :int) -> HttpResponse:
    post =get_object_or_404(Post, pk=pk)

    if request.user != post.user:
        return redirect("project:home")
    post.delete()
    return redirect("project:home")


@login_required
def post_modify_view(request: HttpRequest, pk :int) -> HttpResponse:
    post =get_object_or_404(Post, pk=pk)

    if request.user != post.user:
        return redirect("project:home")
    form = PostModifyFrom(instance=post)

    if request.method == "POST" :
        form = PostCreateFrom(request.POST, request.FILES)
    

        if form.is_valid():
            form.save( True)
        
    return  redirect(request, "post-edit.html",{
        "post_form" : form
    })

@login_required
def create_comment_view(request: HttpRequest)-> HttpResponse:
    if request.method == "GET":
        return redirect("project:home")


    form = CommentCreateForm(request.POST)
    post_pk = request.POST.get("post")
    get_object_or_404(Post, pk=post_pk)

    if form.is_valid():
        comment = form.save(comit=False)
        comment.user = request.user
        comment.save()
        return redirect("project:posts", post_pk )

    return render (request, "post.html",{
        "post" : get_object_or_404(Post, pk=post_pk),
        "comments" : Comment.objects.filter(post__pk=post_pk),
        "comment_form" : form

        
    })    