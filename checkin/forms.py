from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Username'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    
class AddForm(forms.Form):
    name = forms.CharField(label='Full name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    company = forms.CharField(label="Company's name", max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    identification_number = forms.CharField(label='ID number', max_length=100 ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone_number = forms.CharField(label='Phone number', max_length=100 ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    temperature = forms.IntegerField(max_value=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # The Order: 1886
