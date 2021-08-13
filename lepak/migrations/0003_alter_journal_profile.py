# Generated by Django 3.2.6 on 2021-08-13 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lepak', '0002_journal_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journals', to=settings.AUTH_USER_MODEL),
        ),
    ]
