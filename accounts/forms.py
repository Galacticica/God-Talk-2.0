from allauth.account.forms import LoginForm, SignupForm
from django import forms

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].label = "Email"
        self.fields["login"].widget.attrs.update({"placeholder": "Email Address"})
        self.fields["password"].widget.attrs.update({"placeholder": "Password"})

class CustomSignupForm(SignupForm):
    ROLE_CHOICES = [
        (None, 'Select Role'),
        ('presem', 'Pre-Seminary Student'),
        ('seminary', 'Seminary Student'),
        ('theologyprof', 'Theology Professor'),
        ('pastor', 'Pastor'),
        ('churchworker', 'Church Worker'),
    ]

    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}),
        label="First Name"
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}),
        label="Last Name"
    )
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        required=False,
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "Select Role"}),
        label="Role (if any)"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Email"
        self.fields["email"].widget.attrs.update({"placeholder": "Email Address"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Password"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Confirm Password"})

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.role = self.cleaned_data.get('role') or None
        user.save()
        return user