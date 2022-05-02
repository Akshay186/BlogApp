from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditPostForm, AddCategoryForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

#def home(request):
#   return render(request, 'home.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering =['-date']
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     cat_menu=Category.objects.all()
    #     context = super(HomeView, self).get_context_data(object_list=None, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articledetail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = post.likes.filter(id=self.request.user.id).exists()
        context['liked']=liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form): #this function is overrided to automatically set the author of the post as current user.
        form.instance.author=self.request.user
        return super().form_valid(form)

    #fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'add_category.html'
    #fields = '__all__'

class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'

def CategoryView(request, category_arg_sluged):
    category_arg=category_arg_sluged.replace('-', ' ')
    posts = Post.objects.filter(category=category_arg)
    return render(request, 'category_view.html', {'category':category_arg.title(), 'category_posts': posts})

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


def CommentView(request, pk):
    post = get_object_or_404(Post, id=pk)
    commentBody= request.POST['comment_body']
    comment = Comment(post=post, by=request.user, body=commentBody)
    comment.save()
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def EditCommentView(request, pk):
    pass

def DeleteCommentView(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    post = comment.post
    if(request.user == comment.by):
        comment.delete()
    return HttpResponseRedirect(reverse('article-detail', args=[str(post.id)]))