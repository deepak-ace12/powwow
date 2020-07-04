from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if (email and User.objects.filter(
                email=email).exclude(username=username).exists()):
            raise forms.ValidationError(
                'A user with this email address already exists.')
        # elif (username and User.objects.filter(
        #         username=username).exclude(email=email).exists()):
        #     raise forms.ValidationError(
        #         'A user with this username address already exists.')
        return cleaned_data

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
        fields = ('username', 'email', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder':'yyyy-mm-dd'
            }
        )
    )
        
    class Meta:
        model = Profile
        
        exclude = ('user',)

    
class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def clean(self):
        cleaned_data = super(UpdateUserForm, self).clean()
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if (email and User.objects.filter(
                email=email).exclude(username=username).exists()):
            raise forms.ValidationError(
                'A user with this email address already exists.')
        # elif (username and User.objects.filter(
        #         username=username).exclude(email=email).exists()):
        #     raise forms.ValidationError(
        #         'A user with this username address already exists.')
        return cleaned_data