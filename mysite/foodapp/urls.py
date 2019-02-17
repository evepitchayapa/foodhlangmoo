from django.urls import path
from . import views
app_name = 'foodapp'
urlpatterns = [

    path('',views.index,name = 'homepage'),
    path('create_review',views.Create,name = 'create_review'),
    path('success',views.add_review,name = 'add'),
    path('search',views.search_res,name = 'search'),
    path('result',views.result,name = 'result')
    #path('', views.index, name='index'),

]
