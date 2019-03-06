from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"