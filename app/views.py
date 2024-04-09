from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')

class Logout(LogoutView):
    next_page = reverse_lazy('home')

class PostList(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    login_url = reverse_lazy('login')
    form_class = PostForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')



class PostUpdate(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update.html'
    success_url = reverse_lazy('home')
    success_message = 'Post updated successfully'

class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


def comment(request, post_id):
    if request.method == 'POST':
        author = User.objects.get(id=request.user.id)
        text = request.POST.get('text')
        post1 = Post.objects.get(id=post_id)
        Comment.objects.create(author=author, text=text, post=post1)
        return redirect('comment', post_id)
    post = Post.objects.get(id=post_id)
    return render(request, 'comment.html', {'post_id': post ,'post': post.comments.all()})