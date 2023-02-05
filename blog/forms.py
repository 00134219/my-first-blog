from django import forms
from .models import Post
from .models import Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
# 知識の技
class CommentCreateForm(forms.ModelForm):
    """コメントフォーム"""
    class Meta:
        model = Comment
        exclude = ('target', 'created_at')
