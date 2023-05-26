from django.shortcuts import reverse
from django.db import models
from django.utils.text import slugify
from ckeditor import fields


class Home(models.Model):
    title = models.CharField(max_length=255, unique=True, default='Maharaja Hotel')
    subtitle = models.CharField(max_length=255, default='Your ocassion, our cakes!')
    image1 = models.ImageField(upload_to='Home/', default='default.jpg')
    image2 = models.ImageField(upload_to='Home/', default='default.jpg')
    image3 = models.ImageField(upload_to='Home/', default='default.jpg')
    description = fields.RichTextField()
    slug = models.SlugField(unique=True, blank=True)

    phone1 = models.CharField(max_length=20, default='+91-9518519268')
    phone2= models.CharField(max_length=20, default='+91-9518519268')
    email1 = models.EmailField( default='shubhamsahu1234@gmail.com')
    email2 = models.EmailField( default='shubhamsahu@gmail.com')

    facebook = models.URLField(max_length=255, default='facebook')
    instagram = models.URLField(max_length=255, default='instagram')
    linkedin = models.URLField(max_length=255, default='linkedin')
    twitter = models.URLField(max_length=255, default='twitter')

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:home-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:home-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:home-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:home-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:home-delete-page',
                       kwargs={
                           'slug': self.slug
                       })


class About(models.Model):
    title = models.CharField(max_length=255, unique=True, default='About Us')
    subtitle = models.CharField(max_length=255, default='This section is about me!')
    image = models.ImageField(upload_to='About/', default='default.jpg')
    description = fields.RichTextField()
    slug = models.SlugField(unique=True, blank=True)

    youtube = models.URLField(max_length=255, default='youtube')

    sub_image1 = models.ImageField(upload_to='About/', default='default.jpg')
    sub_image2 = models.ImageField(upload_to='About/', default='default.jpg')
    sub_image3 = models.ImageField(upload_to='About/', default='default.jpg')

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:about-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:about-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:about-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:about-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:about-delete-page',
                       kwargs={
                           'slug': self.slug
                       })


class Chef(models.Model):
    title = models.CharField(max_length=255, unique=True, default='Sanjeev')
    subtitle = models.CharField(max_length=255, default='cakes!')
    image = models.ImageField(upload_to='Chef/', default='default.jpg')
    slug = models.SlugField(unique=True, blank=True)

    facebook = models.URLField(max_length=255, default='facebook')
    instagram = models.URLField(max_length=255, default='instagram')
    twitter = models.URLField(max_length=255, default='twitter')

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:home-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:home-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:home-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:home-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:home-delete-page',
                       kwargs={
                           'slug': self.slug
                       })


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True, default='Cakes')
    subtitle = models.CharField(max_length=50, default='Check our cakes ')
    image = models.ImageField(upload_to='Category/', default='default.jpg')
    description = fields.RichTextField()
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:category-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:category-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:category-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:category-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:category-delete-page',
                       kwargs={
                           'slug': self.slug
                       })


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True, default='Pineapple Cake')
    subtitle = models.CharField(max_length=255, default='Check this product!')
    image = models.ImageField(upload_to='Product/', default='default.jpg')
    actual_price = models.DecimalField(decimal_places=2, max_digits=5)
    discount_price = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    description = fields.RichTextField()
    #
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag = models.CharField(choices=(
                                ('featured', 'featured'),
                                ('recent', 'recent'),
                            ), max_length=20, default='featured')
    #
    related_home = models.ForeignKey(Home, on_delete=models.CASCADE, default=f'kirti-agarbatti')
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    def get_final_price(self):
        if self.discount_price:
            final_price = self.actual_price - self.discount_price
            return final_price
        else:
            final_price = self.actual_price
            return final_price

    # Project Design
    def get_object_list_url(self):
        return reverse('ProjectDesign:product-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:product-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:product-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:product-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:product-delete-page',
                       kwargs={
                           'slug': self.slug
                       })

    # Project Model
    def get_model_product_url(self):
        return reverse('ProjectModel:product-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    guest_count = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    description = fields.RichTextField()
    slug = models.SlugField(blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:home-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:home-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:home-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:home-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:home-delete-page',
                       kwargs={
                           'slug': self.slug
                       })



