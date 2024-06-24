from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'review']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название фильма'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Укажите описание фильма'}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Оставьте отзыв'}),
        }