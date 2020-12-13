from django.urls import path

from . import views

'''
example requests: 
    create new todo:
    http://127.0.0.1:8000/todo/new?todo_name=dissapoint_parents_yet_again&todo_auth=rafa&due_date=2020-12-8&importance=1
    
    update request

    '''

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.template_index, name='template_index'),
    path('new', views.new_item),#meant to be used with query string 
    path('delete/<int:todo_id>/', views.delete, name='delete'), #no query string params, are you sure msg needs tobe implemented on client side
    path('detail/<int:todo_id>/', views.detail, name='detail'),
    path('update/<int:todo_id>/', views.update_item, name='update_item'), #meant to be used with id in url  + query string params
    ]
