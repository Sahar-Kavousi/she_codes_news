from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image']
        widgets = {
            'pub_date': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'title': forms.TextInput(  # Use TextInput for CharField
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter a title',
                }
            ),

            'content': forms.Textarea(  # Use TextInput for CharField
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter a content',
                }
            ),
            'image': forms.TextInput(  # Use TextInput for CharField
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter an image url',
                }
            ),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add your comment',
                }
            ),
            'email': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your email address',
                }
            ),
            'name': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your name',
                }
            ),
        }
