from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def init(self, *args, **kwargs):
        super(SignUpForm, self).init(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'w-full bg-[#121212] border border-[#282828] rounded p-3 text-white focus:border-green-500 focus:outline-none transition',
                'placeholder': self.fields[field].label
            })
            self.fields[
                field].help_text = ""