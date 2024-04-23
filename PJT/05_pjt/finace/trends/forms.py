from .models import Keyword,Trend
from django import forms
class KeywordForm(forms.ModelForm):
    name = forms.CharField(
        label='키워드'
    )
    class Meta:
        model = Keyword
        fields = ('name',)