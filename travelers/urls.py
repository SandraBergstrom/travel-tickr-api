from django.urls import path
from travelers import views


urlpatterns = [
    path('travelers/', views.TravelerList.as_view)
]