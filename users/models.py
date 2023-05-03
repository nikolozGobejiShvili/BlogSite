from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

class User(AbstractUser):
    avatar = models.ImageField(upload_to="users/avatars/",
                               default="users/avatars/default_user_avatar.png",
                               blank=True,
                               verbose_name=_("Avatar")
                               )


# Create your models here.
class Meta:
    verbose_name = _("User")
    verbose_name_plural = _("Users")