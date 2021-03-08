from django import forms
class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField(label="E-Mail")
    subject = forms.CharField(required=False)





