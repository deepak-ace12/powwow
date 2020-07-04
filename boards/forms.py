from django import forms

from .models import Topic, Post, Board


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is in your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text should be 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class NewBoardForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Description'}
        ),
        max_length=100,
        help_text='The max length of the text should be 100.'
    )

    class Meta:
        model = Board
        fields = ['name', 'description']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]