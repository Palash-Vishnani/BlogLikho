from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.utils.regex_helper import Choice
from .models import BlogPost

class PostForm(ModelForm):
    class Meta:
        model=BlogPost
        template_name="editor.html"
        fields=['author','title','category','heading2','content2','about','linkedin_link','other_link','image']
        labels={'author':'Author','title':'Title','category':'Category','heading2':'Heading','content2':'Body','about':'About','linkedin_link':'LinkedIn Profile(optional)','other_link':'Instagram Profile(optional)','image':'Upload Blog Image'}
        # CHOICES= (('Option 1', 'Option 1'),('Option 2', 'Option 2'))
        # docfile = forms.FileField(label='Select Image')

        widgets={
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            # 'pub_date': forms.HiddenInput(attrs={'class':'form-control'}),
            # 'category': forms.Select(attrs={'class':'form-control'}),
            'heading2': forms.TextInput(attrs={'class':'form-control'}),
            'content2': forms.Textarea(attrs={'class':'form-control'}),
            'about': forms.Textarea(attrs={'class':'form-control'}),
            'linkedin_link': forms.TextInput(attrs={'class':'form-control','placeholder':'Paste your linkedin profile url'}),
            'other_link': forms.TextInput(attrs={'class':'form-control','placeholder':'Paste your instagram profile url'}),
            # 'image': forms.HiddenInput(attrs={'class':'form-control', 'id':'pic', 'name':'pic', 'value':'default.jpeg'}),
            'image': forms.FileInput(attrs={'class':'form-control', 'id':'pic', 'name':'pic', 'value':'default.jpeg'}),
            'category': forms.HiddenInput(attrs={'class':'form-control', 'id':'myText', 'name':'category', 'value':'Blogs'}),
        }