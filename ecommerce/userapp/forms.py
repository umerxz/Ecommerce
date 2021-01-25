from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import MyUser,Product,Order
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class CustomerForm1(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']
        widgets={
                    'username':forms.TextInput(attrs={'placeholder':'Username..'}),
                    'password1':forms.TextInput(attrs={'placeholder':'Password..'}),
                    'password2':forms.TextInput(attrs={'placeholder':'Confirm Password..'}),
                }

class CustomerForm2(forms.ModelForm):
    class Meta:
        model=MyUser
        fields=('firstname','lastname','email','Register_As')
        widgets={
                    'firstname':forms.TextInput(attrs={'placeholder':'Firstname..'}),
                    'email':forms.EmailInput(attrs={'placeholder':'Email..'}),
                    'lastname':forms.TextInput(attrs={'placeholder':'Lastname..'}),
                }

class AddProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['seller','title','description','price','stock','img','type']
        widgets={
                    'seller':forms.HiddenInput(),
                    'title':forms.TextInput(attrs={'placeholder':'Title..','class':'title'}),
                    'description':forms.Textarea(attrs={'placeholder':'Description..','class':'description'}),
                    'price':forms.NumberInput(attrs={'placeholder':'Price..','class':'price'}),
                    'stock':forms.NumberInput(attrs={'placeholder':'Quantity..','class':'stock'}),
                }
