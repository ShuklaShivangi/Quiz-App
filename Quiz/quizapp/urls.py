from django.contrib import admin 
from django.urls import path
from . import views


# Django admin Header customization

admin.site.site_header = "QuizApp Administration"
admin.site.site_title = "Brainy Quiz"
admin.site.index_title = "Welcome to Brainy Quiz Admin Panel"


urlpatterns = [
    
    path('', views.index, name='index'),
    path("quiz/<int:quiz_id>",views.quiz_detail,name="quiz_detail"),
    path("quiz/<int:quiz_id>/submit",views.quiz_submit,name="quiz_submit")
]