from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):

    error_messages = {
        "invalid_login": (
            "رمز عبور یا نام کاربری اشتباه است"
        ),
        
    }