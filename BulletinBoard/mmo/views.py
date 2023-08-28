from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from .tasks import accept_alert

from .forms import PostForm, FeedbackForm
from .models import Post, Feedback


class PostList(ListView):
    model = Post
    ordering = "name_post"
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 6


class FeedbackList(LoginRequiredMixin, ListView):
    model = Feedback
    template_name = 'feedbacks.html'
    context_object_name = 'feedbacks'
    paginate_by = 6
    pk_url_kwarg = "post_id"

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Feedback.objects.filter(post=post_id)


class FeedbackListUser(LoginRequiredMixin, ListView):
    model = Feedback
    template_name = 'feedbacks_user.html'
    context_object_name = 'feedbacks_user'
    paginate_by = 6
    pk_url_kwarg = "post_id"

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Feedback.objects.filter(post=post_id)


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostDetailUser(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_user.html'
    context_object_name = 'post_user'


class FeedbackDetail(DetailView):
    model = Feedback
    template_name = 'feedback.html'
    context_object_name = 'feedback'


@login_required
def post_create(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'post_edit.html', {'form': form})


@login_required
def feedback_create(request):
    form = FeedbackForm
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'feedback_edit.html', {'form': form})


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


class FeedbackDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'feedback_delete.html'
    success_url = reverse_lazy('post')


def filter_posts(request):
    current_user = request.user
    posts = Post.objects.filter(user=current_user)
    return render(request, 'user_posts.html', {'posts': posts})


def feed_accept(request):
    accept_alert.delay()
    return render(request, 'feed_accept.html')
