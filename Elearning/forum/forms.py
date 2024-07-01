from django import forms
from .models import Forum, Thread, Reply


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'description']

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']