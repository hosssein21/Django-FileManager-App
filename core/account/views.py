from django.contrib.auth import views as auth_views
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import LoginForm

class LoginView(SuccessMessageMixin,auth_views.LoginView):
    template_name='account/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    success_message="باموفقیت وارد شدید {}"

    def get_success_message(self, cleaned_data):
        return self.success_message.format(self.request.user.email.encode('utf-8').decode('utf-8'))


class LogoutView(auth_views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Set the success message
        messages.success(request, "شما با موفقیت خارج شدید.")
        return super().dispatch(request, *args, **kwargs)

class SignupView(CreateView):
    pass