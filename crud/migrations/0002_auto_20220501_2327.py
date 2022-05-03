# Generated by Django 3.2.9 on 2022-05-01 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('class_id', models.PositiveSmallIntegerField(choices=[(1, 'Biology'), (2, 'Calculus'), (3, 'Data Structures'), (4, 'Discreet mathematics'), (5, 'Art History'), (6, 'western civilization'), (7, 'Computer Architecture'), (8, 'Programming dynamics')], primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=50, verbose_name='grade')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='student')),
            ],
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]