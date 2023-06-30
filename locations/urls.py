from django.urls import path
from locations import views

urlpatterns = [
    path('locations/', views.LikeList.as_view()),
    path('locations/<int:pk>/', views.LikeDetail.as_view()),
]