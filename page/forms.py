from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your Name",
        widget=forms.TextInput(attrs={
            "placeholder": "Name :",
            "class": "form-control border-light py-2 bg-light"
        })
    )
    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={
            "placeholder": "Email :",
            "class": "form-control border-light py-2 bg-light"
        })
    )
    subject = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Subject :",
            "class": "form-control border-light py-2 bg-light"
        })
    )
    comments = forms.CharField(
        label="Comments",
        widget=forms.Textarea(attrs={
            "rows": 4,
            "placeholder": "Message :",
            "class": "form-control border-light py-2 bg-light"
        })
    )