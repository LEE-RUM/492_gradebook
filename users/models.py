from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from PIL import Image

class Role(models.Model):
  TEACHER = 1
  STUDENT = 2
  ROLE_CHOICES = (
    (TEACHER, 'Teacher'),
    (STUDENT, 'Student'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
#   permissions = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
    return self.get_id_display()


class User(AbstractUser):

    GENDER_CHOICES = (
        ("F", "Female"),
        ("M", "Male"),
        ("O", "Other"),
    )

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
        help_text=_(
            "150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        null=True,
        blank=True
    )

    email = models.EmailField(
        _("email"),
        max_length=255,
        unique=True,
        null=False,
        help_text=_(
            "Enter your email address here."
        ),
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_of_birth = models.DateTimeField(_("date_of_birth"), auto_now=False, auto_now_add=False, null=True, blank=True)
    gender = models.CharField(_("gender"), max_length=50, choices=GENDER_CHOICES)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics/', null=True)
    bio = models.TextField(blank=True)
    role = models.ForeignKey(Role, verbose_name=_("role"), on_delete=models.CASCADE, related_name="users", null=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @property
    def is_teacher(self):
        return self.role.id == Role.TEACHER