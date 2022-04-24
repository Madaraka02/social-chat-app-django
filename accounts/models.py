import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
def get_profile_image_path(self, filename):
    return f"profile_images/{self.pk}/{'profile_image.png'}"


def get_default_image_path():
    return "default.png"

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", unique=True,max_length=70)
    username = models.CharField(max_length=100)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.FileField(upload_to=get_profile_image_path, null=True, blank=True, default=get_default_image_path)
    hide_email = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f"profile_images/{self.pk}/"):]    
    # check wether has permission to perform admin activities
    def has_perm(self, perm, obj=None):
        return self.is_admin    

    def has_module_perms(self, app_label):
        return True



