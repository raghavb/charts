from django import forms
from django.contrib.auth.models import User

#ToDo: Error handling for the empty case
class RegistrationForm(forms.Form):
  email = forms.EmailField(max_length = 30, min_length = 1,
    widget=forms.TextInput(attrs={'class':'form-control',
                                    'placeholder':'Email'}), required=True)
  password = forms.CharField(max_length = 20, min_length = 1,
    widget=forms.PasswordInput(attrs={'class':'form-control',
                                        'placeholder':'Password'}), required=True)
  confirmPassword = forms.CharField(max_length = 20, label = 'Confirm Password',
    widget=forms.PasswordInput(attrs={'class':'form-control',
                                        'placeholder':'Confirm Password'}), required=True)

  # Customizes form validation for properties that apply to more
  # than one field.  Overrides the forms.Form.clean function.
  def clean(self):
    # Calls our parent (forms.Form) .clean function, gets a dictionary
    # of cleaned data as a result
    cleaned_data = super(RegistrationForm, self).clean()

    # Confirms that the two password fields match
    password = cleaned_data.get('password')
    confirmPassword = cleaned_data.get('confirmPassword')
    if password and confirmPassword and password != confirmPassword:
        raise forms.ValidationError("Passwords did not match.")

    # We must return the cleaned data we got from our parent.
    return cleaned_data

  # Customizes form validation for the email field.
  def clean_email(self):
    # Confirms that the email is not already present in the
    # User model database.
    email = self.cleaned_data.get('email')
    if User.objects.filter(username__exact=email):
        raise forms.ValidationError("email is already taken.")
    # We must return the cleaned data we got from the cleaned_data
    # dictionary
    return email

class DocumentForm(forms.Form):
    companyName = forms.CharField(label='Company Name', max_length = 30, min_length = 1)
    stockId = forms.CharField(label='Stock Id', max_length = 5, min_length = 1)
    docfile = forms.FileField(label='Select a file')