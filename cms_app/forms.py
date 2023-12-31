from django import forms


class regform(forms.Form):
    fname = forms.CharField(max_length=50)
    lname = forms.CharField(max_length=20)
    image = forms.FileField()
    emailid = forms.EmailField()
    addr = forms.CharField(max_length=250)
    contact = forms.IntegerField()
