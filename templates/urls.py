from django.urls import path
from templates.page import list
from templates.page.write import blog_write, service_write, questions_write,service_case_write
from templates.db import DB

urlpatterns = [
    path('', list.redirect),
    path('service_list/', list.service, name='service'),
    path('service_write/', service_write.service_write, name='service_write'),
    path('service_case/', list.service_case, name='service_case'),
    path('service_case_write/', service_case_write.service_case_write, name='service_case_write'),
    path('questions/', list.questions, name='questions'),
    path('questions_write/', questions_write.questions_write, name='questions_write'),
    path('blog_list/', list.blog_list, name='blog_list'),
    path('blog_write/',blog_write.blog_write, name='blog_write'),
    path('create/', DB.create, name = 'create')
]