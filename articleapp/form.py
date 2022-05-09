from django.forms import ModelForm
form django import forms

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget= forms.Textarea(attrs={'class': 'editable',
                                                            'style': 'height : auto;'}))

    project = fomrs.ModelChoiceField(queryset=Project.objects.all, required=False)

    class Meta:
        model = Article
        fields = ['title', 'image','project', 'content']