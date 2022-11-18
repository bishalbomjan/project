from django.urls import path
from home import views
urlpatterns = [
    path('aboutus/', views.aboutus, name='aboutus'),
    path('download/', views.download, name='download'),
    path('notice/', views.notice, name='notice'),
    path('college/', views.colleges, name='college'),
    path('program/', views.program, name='program'),
]
