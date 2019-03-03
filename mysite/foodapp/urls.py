from django.urls import path
from . import views
app_name = 'foodapp'
urlpatterns = [

    path('',views.index,name = 'homepage'),
    path('create_review', views.create_review, name ='create_review'),
    path('success',views.add_review,name = 'add'),
    path('search',views.search_res,name = 'search'),
    path('result',views.result,name = 'result'),
    path('restaurant/<int:res_id>/', views.show_restaurants ,name='show_res'),
    path('category',views.category , name = 'category'),
    path('category/a_la_cart',views.category_a , name = 'category _a'),
    path('category/street_food',views.category_s , name = 'category _s'),
    path('category/cafe',views.category_c , name = 'category _c'),

    #path('', views.index, name='index'),

]
