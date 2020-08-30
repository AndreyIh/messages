from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    content = forms.CharField(label='Текст сообщения', widget=forms.Textarea(
                              attrs={'class': 'form-control quill-editor',
                                     'placeholder': 'Место для вашего комментария'}))
    media_file = forms.ImageField(required=False, label='Добавить изображение',
                                  widget=forms.FileInput(attrs={'id': 'media_files',
                                                                'class': 'form-control'}))

    class Meta:
        model = Message
        fields = ('content', 'media_file',)
