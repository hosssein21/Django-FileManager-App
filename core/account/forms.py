from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model =User
        fields = ('email', 'password1', 'password2', )

        def save(self):
            user_obj = User.objects.create_user(email=self.cleaned_data["email"],
                                            password=self.cleaned_data["password1"])
            self.send_mail(user_obj)
            return user_obj
    error_messages = {
        "password_mismatch": _("دو رمز وارد شده مطابقت ندارد"),
    }

class LoginForm(AuthenticationForm):

    error_messages = {
        "invalid_login": (
            "رمز عبور یا نام کاربری اشتباه است"
        ),
        
    }