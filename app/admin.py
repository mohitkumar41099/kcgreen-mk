from django.contrib import admin
from .models import Event, Home, Post,Product , Category ,Subcategory,Contact,Comment,Testimonial,Client

class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('related_products',)


# Register your models here.
admin.site.register(Home)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Testimonial)
admin.site.register(Client)
