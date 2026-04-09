from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo'] # array because using custom form by us
        
class UserRegistrationForm(UserCreationForm): #use in-built UserCreationForm
    email = forms.EmailField() # add extra field
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2') #tuple since we are using built-in form

#styling the SearhForm here 
#using widgets which adds all style classes fields etc
class SearchForm(forms.Form):
    #it adds label = 'Text:' bydefault to remove it add label='' and label_suffix=''
    #or just keep in template as {{form.text}} to only show input fields no labels
    text = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control me-2",
                "type": "search",
                "placeholder": "Search",
                "aria-label": "Search",
                "id": "text",
                "name": "text",
            }
        )
    )