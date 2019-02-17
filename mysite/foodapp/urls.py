from django.urls import path
from . import views
app_name = 'foodapp'
urlpatterns = [

    path('',views.index,name = 'homepage'),
    path('create_review',views.Create,name = 'create_review'),
    path('success',views.add_review,name = 'add'),
    #path('', views.index, name='index'),

]
