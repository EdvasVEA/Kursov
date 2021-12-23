"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import CommentZ
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class PoolForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    design = forms.ChoiceField(label='Ваша оценка дизайна нашего сайта',
                               choices=[('1', 'Отлично'), ('2', 'Хорошо'), ('3', 'Нормально'), ('4', 'Плохо'), ('5', 'Очень плохо')],
                               widget=forms.RadioSelect, initial=1)
    functio = forms.ChoiceField(label='Ваша оценка функциональности нашего сайта',
                               choices=[('1', 'Отлично'), ('2', 'Хорошо'), ('3', 'Нормально'), ('4', 'Плохо'), ('5', 'Очень плохо')],
                               widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Вы посещаете наш сайт',
                                 choices=(('1', 'Каждый день'),
                                 ('2', 'Несколько раз в день'),
                                 ('3', 'Несколько раз в неделю'),
                                 ('4', 'Несколько раз в месяц')), initial=1)
    notice = forms.BooleanField(label='Стоит ли добавить фоновое оформление сайта в виде gif-картинок?',
                               required=False)
    message = forms.CharField(label='Ваши пожелания',
                              widget=forms.Textarea(attrs={'rows':12,'cols':20}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class CommentZForm (forms.ModelForm):
    class Meta:
        model = CommentZ
        fields = ('name', 'phone', 'address', 'text',)
        labels = {'name': "Ваше имя", 'phone': "Ваш телефон", 'address': "Адрес доставки", 'text': "Напишите, что вы хотите заказать, и ваши личные пожелания к заказу"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}
