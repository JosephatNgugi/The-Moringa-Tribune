from django import forms

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='Firsr Name', max_length=30)
    email = forms.EmailField(label='Email')
    