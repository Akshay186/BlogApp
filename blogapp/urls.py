from django.urls import path, include
from .views import HomeView, ArticleDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView, LikeView, CommentView, DeleteCommentView
urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:category_arg_sluged>', CategoryView, name='category_view'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name="edit-article"),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name="delete-article"),
    path('like/<int:pk>', LikeView, name="post_like"),

    path('comment/<int:pk>', CommentView, name="post_comment"),
    #path('edit_comment/<int:pk>', EditCommentView, name="edit_comment"),
    path('delete_comment/<int:pk>', DeleteCommentView, name="delete_comment"),
]
