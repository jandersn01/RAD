from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required = True ,max_length=254, help_text='Enter a valid email address.',
                             widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address', 'class': 'input-text'}))

    class Meta:
        model = get_user_model()  # Substitua pelo modelo de usuário personalizado, se necessário
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, 
                               widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'input-text'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'input-text'}))