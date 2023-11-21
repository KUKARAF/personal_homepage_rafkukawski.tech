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
    path('test', views.template_index, name='template_test'),
    path('new', views.new_item),#meant to be used with query string 
    path('contact/', views.contact_form), #send email to me, is forwarded to rafal.kuka94@gmail.com 
    path('delete/<int:todo_id>/', views.delete, name='delete'), #no query string params, are you sure msg needs tobe implemented on client side
    path('detail/<int:todo_id>.json', views.detail, name='detail'),
    path('update/<int:todo_id>/', views.update_item, name='update_item'), #meant to be used with id in url  + query string params
    path('status/<int:todo_id>', views.status_set, name='status_set'), 
    ]
