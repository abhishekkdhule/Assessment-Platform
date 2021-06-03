from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from . models import User

class SettingsBackend(BaseBackend):

    def authenticate(email=None, password=None):
        print("authenticate called")
        try:
            user = User.objects.get(email=email)
            if(check_password(password,user.password)):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
  