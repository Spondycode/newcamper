from django import forms    
from .models import Plot, Comment, Reply
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


# Create Plot form
class PlotAddForm(ModelForm):
    class Meta:
        model = Plot
        fields = ['title', 'description', 'price', 'season', 'plot', 'what3words', 'campsite', 'countries', 'categories', 'plot_image']
        labels = {
            'title': 'Name Plot',
            'description': '',
            'price': 'Per Night',
            'season': 'What time of Year?',
            'plot': '',
            'what3words': '',
            'campsite': '',
            'countries': 'Country',
            'categories': 'Type of Plot',
            'plot_image': 'Image',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Your name for it...'}), # 'class': 'form-control'
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add a description...'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Add a price...'}),
            'plot': forms.TextInput(attrs={'placeholder': 'Plot ID/number or None...'}),
            'what3words': forms.TextInput(attrs={'placeholder': 'Add a what3words URL...'}),
            'campsite': forms.TextInput(attrs={'placeholder': 'Campsite name or None...'}),
        }


class PlotEditForm(ModelForm):
    class Meta:
        model = Plot
        fields = ["title", "description", "price", 'season', "plot", "what3words", "campsite", "countries", "categories", "plot_image"]
        labels = {
                'title': 'Name Plot',
                'description': '',
                'price': 'Per Night',
                'season': 'What time of Year?',
                'plot': '',
                'what3words': '',
                'campsite': '',
                'countries': 'Country',
                'categories': 'Type of Plot',
                'plot_image': 'Image',
            }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Your name for it...'}), # 'class': 'form-control'
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add a description...'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Add a price...'}),
            'plot': forms.TextInput(attrs={'placeholder': 'Campsite ID or None...'}),
            'what3words': forms.TextInput(attrs={'placeholder': 'Add a what3words URL...'}),
            'campsite': forms.TextInput(attrs={'placeholder': 'Campsite name or None...'}),
        }
     
     
     
class PlotReportForm(ModelForm):
    class Meta:
        model = Plot
        fields = ["reason"]
        labels = {
            "report": "Reason for reporting this plot",
        }

        
        
        
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]
        
        
class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.TextInput(attrs={'placeholder': 'Add a comment...'}),
        }
        labels = {
            "body": "",
        }
        
        
        
class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ["body"]
        widgets = {
            "body": forms.TextInput(attrs={'placeholder': 'Add a reply...'}),
        }
        labels = {
            "body": "",
        }