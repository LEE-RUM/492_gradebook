from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# models class, which includes class choices, and fields for when user signs up
User = get_user_model()

class StudentClass(models.Model):
    Biology = 1
    Calculus = 2
    Data_Structures = 3
    Discreet_mathematics = 4
    Art_History = 5
    western_civilization = 6
    Computer_Architecture = 7
    Programming_dynamics = 8

    CLASS_CHOICES = (
        (Biology, 'Biology'),
        (Calculus, 'Calculus'),
        (Data_Structures, 'Data Structures'),
        (Discreet_mathematics, 'Discreet mathematics'),
        (Art_History, 'Art History'),
        (western_civilization, 'western civilization'),
        (Computer_Architecture, 'Computer Architecture'),
        (Programming_dynamics, 'Programming dynamics'),
    )

    class_id = models.PositiveSmallIntegerField(choices=CLASS_CHOICES, primary_key=True)
    student = models.ForeignKey(User, verbose_name=_("student"), on_delete=models.CASCADE, related_name="classes")
    grade = models.CharField(_("grade"), max_length=50)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return self.get_class_id_display()

    def name(self):
        return self.get_class_id_display()