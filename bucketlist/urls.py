from django.urls import path
from bucketlist import views

urlpatterns = [
    path('bucketlist/', views.BucketlistList.as_view()),
    path('bucketlist/<int:pk>/', views.BucketlistItemDetail.as_view()),
]