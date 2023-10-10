from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddtweetForm(forms.Form):
    nickname_input = forms.CharField(label="Nickname",max_length=50)
    tweet_input = forms.CharField(label="Tweet",max_length=100,
                                  widget=forms.Textarea(attrs={"class":"tweetmessage"}))
    #widget=forms.Textarea olarak bırakırsak varsayılanı ayarlar
    #widget=forms.Textarea(attrs={"class":"tweetform"}) tweetform özelliklerini ayarlar

class AddtweetModelForm(ModelForm):
    class Meta:
        model=Tweet
        fields =["username","message"]