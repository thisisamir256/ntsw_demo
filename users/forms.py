from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'national_code',
            'birth_date',
            'username',
            'password1',
            'password2',
            'mobile',
            'phone',
            'postal_code',
            'email',
            'use_2fa',
            'avatar',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].disabled = True
        self.fields["username"].widget.attrs["readonly"] = True
