#! coding=utf-8
from django import forms
from pagedown.widgets import AdminPagedownWidget
from models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(label=u'标题', widget=forms.TextInput(attrs={'size':118}))
    content = forms.CharField(label=u'内容', widget=AdminPagedownWidget())
    snippet = forms.CharField(label=u'摘要', widget=forms.Textarea(attrs={'cols':85, 'rows':7}))
    class Meta:
        model = Blog
        widgets = {
            'snippet': forms.Textarea(attrs={'rows':4,'cols':15}),
        }

    def save(self, commit=True):
        '''
            默认的保存方式即为发布文章
        '''
        instance = super(BlogForm, self).save(commit=False)
        instance.published = True 
        if commit:
            instance.save()
        return instance
