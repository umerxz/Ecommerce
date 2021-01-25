from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class MyUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100,default='')
    lastname=models.CharField(max_length=100,default='')
    email=models.EmailField(unique=True,default='')
    CHOICE = (
        ('B', 'Buyer'),
        ('S', 'Seller'),
    )
    Register_As = models.CharField(max_length=6, choices=CHOICE,default='Select')

    def __str__(self):
        return self.user.username

class Product(models.Model):
    seller=models.ForeignKey(MyUser,on_delete=models.DO_NOTHING,blank=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.PositiveSmallIntegerField()
    stock=models.PositiveSmallIntegerField()
    img=models.ImageField()

    CHOICE = (
        ('Shirts', 'Shirts'),
        ('T-shirts', 'T-shirts'),
        ('Jackets', 'Jackets'),
        ('Jeans', 'Jeans'),
        ('Shorts', 'Shorts'),
        ('Tights', 'Tights'),
        ('Trousers', 'Trousers'),
        ('Joggers', 'Joggers'),
        ('Sneakers', 'Sneakers'),
        ('Pumps', 'Pumps'),
        ('Heels', 'Heels'),
    )
    type = models.CharField(max_length=10, choices=CHOICE,default='')

    category_choice=(('W','Women'),('M','Men'),('K','Kid'))
    category=models.CharField(max_length=5,choices=category_choice,default='null')

    def __str__(self):
        return self.title#,kwargs={'pk':self.pk})

class Order(models.Model):
    customer=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    address=models.CharField(max_length=200,blank=True,null=True)
    total_price=models.PositiveIntegerField(blank=True,null=True)
    is_complete=models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        items=self.item_set.all()
        total=sum([x.get_total for x in items])
        return total

    @property
    def get_item_total(self):
        items=self.item_set.all()
        total=sum([x.quantity for x in items])
        return total

class Item(models.Model):
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING,default='')
    order=models.ForeignKey(Order,on_delete=models.DO_NOTHING,)
    quantity=models.PositiveSmallIntegerField(blank=False,null=True,default=0)

    def __str__(self):
        return str(self.product.title)

    @property
    def get_total(self):
        return self.quantity*self.product.price
