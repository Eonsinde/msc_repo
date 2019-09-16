from django.urls import path, re_path
from . import views

# write your urlpatterns here


urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('review/', views.ReviewView.as_view(), name='review'),
    path('health-tips/', views.HealthView.as_view(), name='health-tips'),
]