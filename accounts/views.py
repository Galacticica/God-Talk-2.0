from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.shortcuts import redirect
from allauth.account.views import LoginView, SignupView
from .forms import CustomLoginForm, CustomSignupForm

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = CustomLoginForm

class CustomSignupView(SignupView):
    template_name = "accounts/signup.html"
    form_class = CustomSignupForm


def login_page(request):
    """Create a view for the login page."""
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            return redirect("/")  
    else:
        form = CustomLoginForm()
    template = loader.get_template("accounts/login.html")
    context = {"form": form}
    return HttpResponse(template.render(context, request))

def signup_page(request):
    """Create a view for the signup page."""
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save(request)  
            return redirect("/")  
    else:
        form = CustomSignupForm()
    template = loader.get_template("accounts/signup.html")
    context = {"form": form}
    return HttpResponse(template.render(context, request))

