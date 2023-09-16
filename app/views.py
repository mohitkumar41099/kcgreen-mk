
from urllib import request
from django.shortcuts import get_object_or_404, render,redirect



from app.form import CommentForm
from .models import Event, Home, Post,Product , Category ,Subcategory,Contact,Testimonial,Client
from django.contrib import messages
# Create your views here.


def home(request):
    home = Home.objects.all()
    product=Product.objects.all()
    events = Event.objects.all()

    categories = Category.objects.all()
    subcategorys = Subcategory.objects.all()
   
    
    context = {'home':home,'product':product,'categories':categories ,'subcategorys':subcategorys,'events':events}
    return render(request,'index.html',context)




def about(request):
    home = Home.objects.all()
    product=Product.objects.all()
    categories = Category.objects.all()
    subcategorys = Subcategory.objects.all()
    context = {'home':home,'product':product, 'categories':categories ,'subcategorys':subcategorys}
    return render(request,'about.html',context)




def client(request):
    clients = Client.objects.all()
    testimonials = Testimonial.objects.all()
    categories = Category.objects.all()
    
    contect ={'categories': categories,'testimonials':testimonials,'clients':clients}
    return render(request, 'clients.html', contect)






def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})



def subcategory_list(request, category_slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    subcategories = category.subcategory_set.all()
    return render(request, 'subcategory_list.html', {'subcategories': subcategories,'categories':categories})



def product_list(request, subcategory_slug):
    categories = Category.objects.all()
    subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
    products = subcategory.product_set.all()
    return render(request, 'product_list.html', {'products': products,'categories':categories})



def product_detail(request, product_slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, slug=product_slug)
    
    related_products = product.related_products.all()
    return render(request, 'product_detail.html', {'product': product, 'related_products': related_products , 'categories':categories})
# ___________________blog___________________________________________

def post_list(request):
    
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    categories = Category.objects.all()
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post , 'categories':categories})

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    
    return render(request, 'add_comment.html', {'form': form, 'post_id': post_id})

# ___________________event___________________________________________


def event_list(request):
    categories = Category.objects.all()
    subcategorys = Subcategory.objects.all()
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events,'categories':categories,'subcategorys':subcategorys})



def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event_detail.html', {'event': event})





# _____________________________________contact______________________________

def contact(request):
  
    categories = Category.objects.all()

    if request.method == 'POST':
        category = request.POST['category']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if len(name) > 4:
            contact = Contact(category=category,name=name,phone=phone,email=email,subject=subject,message=message)
            contact.save()
            messages.success(request,'Successfully Form Submit')
            return redirect('/contact')
        else:
            messages.error(request,'First Name Should Be more then 4 chars')
            return redirect('/contact')
    return render(request,'contact.html',{'categories':categories})


# _____________________________________testimonials______________________________




