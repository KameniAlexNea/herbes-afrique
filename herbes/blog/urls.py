from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    
    path('',views.IndexView.as_view(), name='post_list'),
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit, name='post_edit'),
    
    #path('^post/(?P<pk>[0-9]+)/$/',views.post_detail, name='post_detail'),

]
