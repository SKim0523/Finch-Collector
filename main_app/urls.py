from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('finches/', views.FinchList.as_view(), name="finch_list"),
    path('finches/<int:pk>/', views.FinchDetails.as_view(), name="finch_detail"),
    path('finches/new/', views.FinchCreate.as_view(), name="finch_create"),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name="finch_update"),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name="finch_delete"),
    path('finches/<int:pk>/comments/new', views.CommentCreate.as_view(), name='comment_create'),
    path('finches/<int:pk>/comments/update', views.CommentUpdate.as_view(), name='comment_update'),
    path('finches/<int:pk>/comments/delete', views.CommentDelete.as_view(), name='comment_delete'),
    path('lists/<int:pk>/finches/<int:finch_pk>/', views.ListFinchAssoc.as_view(), name="list_finch_assoc"),
]