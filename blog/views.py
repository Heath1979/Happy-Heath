from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import CreateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Post, Comment
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
                Q(category__category__icontains=query) |
                Q(location__location__icontains=query)
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
        An instance of :form:'blog.CommentForm'.            
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
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

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
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(CreateView):
    """ 
    Add create post view
    """
    template_name = 'blog/add_post.html'
    model = Post
    form_class = PostForm
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPost, self).form_valid(form)
