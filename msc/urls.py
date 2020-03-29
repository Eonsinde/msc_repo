from django.urls import path, re_path
from . import views
from django.contrib import admin

app_name = 'msc'

admin.site.site_header = 'Mahanaim Surgical Consult'
admin.site.site_title = 'MSC'
admin.site.index_title = "MSC Administration"


# write your urlpatterns here

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('review/', views.ReviewView.as_view(), name='review'),
    path('health-tips/', views.HealthView.as_view(), name='health-tips'),
]