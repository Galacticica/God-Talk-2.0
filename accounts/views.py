from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .forms import LoginForm, SignupForm

User = get_user_model()

class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

class MySignupView(FormView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = "/"  # Redirect to home page after successful signup

    def form_valid(self, form):
        # Create a new user
        user = User.objects.create(
            email=form.cleaned_data["email"],
            username=form.cleaned_data["email"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            role=form.cleaned_data["role"],
            password=make_password(form.cleaned_data["password"]),  # Hash the password
        )
        # Log the user in
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle invalid form submission
        return super().form_invalid(form)

