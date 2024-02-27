from django.urls import path
from .views import posts_view

urlpatterns = [
   path('posts/', posts_view),
   path('posts/<int:post_id>/', posts_view),
]
