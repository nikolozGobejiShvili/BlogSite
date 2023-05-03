from django.urls import path
from project.views import home_view, post_create_view, post_detail_view , post_list_view, post_delete_view, post_modify_view, create_comment_view

app_name = "project"
urlpatterns = [
    path("", home_view, name="home"),
    path("post/<int:pk>/", post_detail_view, name="posts"),
    path("create/post/", post_create_view, name="post-create"),
    path("post/", post_list_view, name="post-list"),
    path("post/<int:pk>/delete/", post_delete_view , name= "post-delete" ),
    path("post/<int:pk>/modify/", post_modify_view , name= "post-modify" ),
    path("post/add/comment/", create_comment_view, name="comment-create")
]
