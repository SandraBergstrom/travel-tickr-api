from django.urls import path
from bucketlist import views


urlpatterns = [
    path('bucketlist/', views.BucketList.as_view()),
    path('bucketlist/<int:pk>/', views.BucketListDetail.as_view()),
]
