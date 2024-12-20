from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/home.html'),
         name='home'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('await-approval/', TemplateView.as_view
         (template_name='blog/await_approval.html'),
         name='await_approval'),
    path('delete_post/<slug:slug>/', views.DeletePost.as_view(),
         name='delete_post'),
    path('edit/<slug:slug>/', views.EditPost.as_view(), name='edit_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
