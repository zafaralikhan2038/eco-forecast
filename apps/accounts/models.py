from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser
    with additional fields for profile information
    """
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    profile_photo = models.ImageField(
        upload_to='profile_photos/', 
        null=True, 
        blank=True, 
        verbose_name=_('Profile Photo'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user account should be treated as active. '
            'Unselect this instead of deleting accounts.'
        )
    )

    def __str__(self):
        return self.username