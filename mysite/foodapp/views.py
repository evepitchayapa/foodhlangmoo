from django.http import HttpResponse
from .models import Restaurants,Review,timezone
from django.shortcuts import render,get_object_or_404,Http404

# Create your views here.

def index (request):
    return render(request,'foodapp/homepage.html')

def create_review (request):
    name = str(Restaurants.objects.get(pk=1))
    context = {'name':name}
    return render(request,'foodapp/review_page.html',context)

def add_review(request):
    topic = str(request.POST['topic'])
    point = int(request.POST['point'])
    review_detail = str(request.POST['review_detail'])
    name = Restaurants.objects.get(pk=1)
    review = name.review_set.create(summary_review = topic,point =point,review_text = review_detail,date_review = timezone.now())
    review.save()
    context = {'name' : name,'review':review}
    return render(request,'foodapp/showreview.html',context)

def search_res(request):
    return render(request,'foodapp/search.html')

def result (request):
    keyword = (request.POST['search'])
    r = Restaurants.objects.filter(name_text__startswith = keyword)
    count = len(r)
    context = {'lstname':r,'count':count,'key':keyword}
    return  render(request,'foodapp/result.html',context)

def show_restaurants (request,res_id):
    res = Restaurants.objects.get(pk=res_id)
    review = res.review_set
    context = {'res': res,'lstreview':review}
    return render(request, 'foodapp/show_restaurant.html',context )

def category (request):
    context = {}
    return render(request,'foodapp/category.html',context)

def category_a(request):
    a = Restaurants.objects.filter(category__startswith = 'อ')
    context = {'a': a}
    return render(request,'foodapp/a_la_cart.html',context)
def category_s(request):
    s = Restaurants.objects.filter(category__startswith  = 'ส')
    context = {'s':s}
    return render(request,'foodapp/street_food.html',context)
def category_c(request):
    c = Restaurants.objects.filter(category__startswith  = 'ค')
    context = {'c':c}
    return render(request,'foodapp/cafe.html',context)

