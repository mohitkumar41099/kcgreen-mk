from django.utils.text import slugify
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
# Create your models here.


# ---------------home-----------
class Home(models.Model):
	

	about = RichTextField()
	copyright = models.CharField(max_length=255,blank=True,null=True)
	


	def __str__(self):
		return self.title


# -----------category-----------------------
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subcategory/')
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subcategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# ------------product----------

class Product(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    model_no = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    image_one = models.ImageField(upload_to='products/')
    image_two = models.ImageField(upload_to='products/')
    image_three = models.ImageField(upload_to='products/')
    pdf = models.FileField(upload_to='pdf',blank=True,null=True)
    youtube = EmbedVideoField()
    slug = models.SlugField(unique=True)
    des_title_one = RichTextField()
    des_one = RichTextField()
    des_title_two = RichTextField()
    des_two = RichTextField()
    des_title_three = RichTextField()
    des_three = RichTextField()
    des_title_four = RichTextField(blank=True,null=True)
    des_four = RichTextField(blank=True,null=True)
    des_title_five = RichTextField(blank=True,null=True)
    des_five = RichTextField(blank=True,null=True)
    des_title_six = RichTextField(blank=True,null=True)
    des_six = RichTextField(blank=True,null=True)
    des_title_seven = RichTextField(blank=True,null=True)
    des_seven = RichTextField(blank=True,null=True)
    des_title_eight = RichTextField(blank=True,null=True)
    des_eight = RichTextField(blank=True,null=True)
    des_title_nine = RichTextField(blank=True,null=True)
    des_nine = RichTextField(blank=True,null=True)
    des_title_ten = RichTextField(blank=True,null=True)
    des_ten = RichTextField(blank=True,null=True)
    description = RichTextField(blank=True,null=True)
    related_products = models.ManyToManyField('self', blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.title
    

# -----------------------------------client------------------------------

class Client(models.Model):
    client_logo = models.ImageField(upload_to='clients/')

    def __str__(self):
        return str(self.client_logo)



# ---------------blog---------------------
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_image_1/')
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    name = models.CharField(max_length=255,blank=True,null=True)
    email = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name  




# --------------event------------

class Event(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image_1 = models.ImageField(upload_to='event_image_1/')
    image_2 = models.ImageField(upload_to='event_image_2/')
    image_3 = models.ImageField(upload_to='event_image_3/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    


    def __str__(self):
        return self.title






# -----------contact--------------------
class Contact(models.Model):
	category = models.CharField(max_length=255,blank=True,null=True)
	name = models.CharField(max_length=255,blank=True,null=True)
	phone = models.CharField(max_length=255,blank=True,null=True)
	email = models.CharField(max_length=255,blank=True,null=True)
	subject = models.CharField(max_length=255,blank=True,null=True)
	message = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.name



# -----------Testimonial--------------------
class Testimonial(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='testimonial_images')
    rating = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.author





