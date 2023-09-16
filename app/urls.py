from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
from django.conf.urls.static import static 


admin.site.site_header = 'KC GREEN'  
            
admin.site.index_title = 'KC GREEN'                 
admin.site.site_title = 'Welcom to KC GREEN'

urlpatterns = [
    
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    
    path('client',views.client,name="client"),

    path('categories/', views.category_list, name='category_list'),
    path('categories/<slug:category_slug>/subcategories/', views.subcategory_list, name='subcategory_list'),
    path('subcategories/<slug:subcategory_slug>/products/', views.product_list, name='product_list'),
    path('products/<slug:product_slug>/', views.product_detail, name='product_detail'),

    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),


    path('events/', views.event_list, name='event_list'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 