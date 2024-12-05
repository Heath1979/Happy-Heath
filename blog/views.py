from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Post, Comment, Location
from .forms import CommentForm, PostForm

# Create your views here.


class PostList(generic.ListView):
    """
    Display all published posts in blog/index.html
    and set number of posts per page.
    """
    model = Post
    template_name = "blog/index.html"
    paginate_by = 6
    """
    enable search functionality
    """
    def get_queryset(self):
        queryset = Post.objects.filter(status=1)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(category__type__icontains=query) |
                Q(location__name__icontains=query)
            )
        return queryset


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments relate dto the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:'blog.CommentForm'
    **Template:**
    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted. Thank you for being part of the community'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.
    **Context**
    ``post``
        An instance of :model:'blog.post'.
    ``commemt``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:'blog.CommentForm'.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.
    **Context**
    ``post``
        An instance of :model:'blog.post'.
    ``comment``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(LoginRequiredMixin, generic.CreateView):
    """
    Add create post view
    """
    template_name = 'blog/add_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('await_approval')
    """
    credit to perplexity AI
    """
    def form_valid(self, form):
        form.instance.author = self.request.user
        location_name = form.cleaned_data.get('location')
        location, created = Location.objects.get_or_create(name=location_name)
        form.instance.location = location
        return super(AddPost, self).form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin,
               SuccessMessageMixin, generic.UpdateView):
    """
    Add edit post view
    """
    template_name = 'blog/edit_post.html'
    model = Post
    form_class = PostForm
    success_message = "The post '%(title)s' was updated successfully"

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_message(self, cleaned_data):
        return self.success_message % {'title': self.object.title}


class DeletePost(LoginRequiredMixin, UserPassesTestMixin,
                 generic.DeleteView):
    """
    Add delete post view
    """
    template_name = 'blog/delete_post.html'
    model = Post
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context
