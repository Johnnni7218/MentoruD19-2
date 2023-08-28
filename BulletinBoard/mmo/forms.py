from django import forms
from .models import Post, Feedback


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'name_post',
            'body_post',
            'category',
            'user',
        ]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'post',
            'body_feedback',
            'user'
        ]
