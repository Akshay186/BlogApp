from django import forms
from .models import Category, Post

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for choice in choices:
    choice_list.append(choice)


class PostForm(forms.ModelForm):
    class Meta:

        model=Post
        fields=('title', 'category', 'snippet', 'body', 'cover_image')

        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name',)

        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','category', 'snippet', 'body', 'cover_image')

        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }