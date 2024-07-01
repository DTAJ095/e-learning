from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum_list, name='forum_list'),
    path('<int:forum_id>/', views.thread_list, name='thread_list'),
    path('<int:forum_id>/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('<int:forum_id>/create_thread/', views.create_thread, name='create_thread'),
    path('<int:forum_id>/<int:thread_id>/create_reply/', views.create_reply, name='create_reply'),
]