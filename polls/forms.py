from django import forms

class NameForm(forms.Form):
  screenname = forms.CharField(label="Search for a user:",max_length=32)