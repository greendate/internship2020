from django import forms
from django.forms import ModelForm, Textarea, TextInput, IntegerField, ChoiceField, RadioSelect, NumberInput
from .models import UserInfo, Book, Comment

TYPE_CHOICES = [
    (1, 'Action and adventure'),
    (2, 'Art/architecture'),
    (3, 'Autobiography'),
    (4, 'Business/economics'),
    (5, 'Classic'),
    (6, 'Cookbook'),
    (7, 'Dictionary'),
    (8, 'Crime'),
    (9, 'Encyclopedia'),
    (10, 'Drama'),
    (11, 'Guide'),
    (12, 'Fairytale'),
    (13, 'Health/fitness'),
    (14, 'Fantasy'),
    (15, 'History'),
    (16, 'Humor'),
    (17, 'Horror'),
    (18, 'Journal'),
    (19, 'Mystery'),
]

class UserEditForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('telegram_alias', 'messenger_alias')

        widgets = {
            'telegram_alias': TextInput(attrs={'id': 'telegram_alias', 'placeholder': 'telegram'}),
            'messenger_alias': TextInput(attrs={'id': 'messenger_alias', 'placeholder': 'messenger'}),
        }


class UploadBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'author', 'price', 'cover', 'description', 'type')
        type = ChoiceField(widget=RadioSelect, choices = TYPE_CHOICES)
        widgets = {
            'name': TextInput(attrs={'id': 'name', 'placeholder': 'Book Title'}),
            'author': TextInput(attrs={'id': 'author', 'placeholder': 'Author'}),
            'cover': TextInput(attrs={'id': 'cover_url', 'placeholder': 'https://sample-cover.jpg'}),
            'price': NumberInput(attrs={'id': 'price', 'step': "0.1"}),
            'description': Textarea(attrs={'id': 'description', 'placeholder': 'Short description..'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {
            'text': Textarea(attrs={'id': 'text', 'placeholder': "Type your comment here.."}),
        }
