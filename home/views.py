from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        # If user is already authorized, pass through to notes.list
        if self.request.user.is_authenticated:
            return redirect('notes.list')

        # The replicates the original signin functionality, but blocks currently
        # signed in users from creating another account
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


# Preferred class based approach
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


# Preferred class based approach
# Note use of .mixins above
class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = 'home/login.html'
    # login_url = '/admin'


# More primative method
# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})


# More primative method
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})