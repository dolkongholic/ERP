# Generated by Django 4.0 on 2021-12-13 10:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_vacationlist_add_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationlist',
            name='target_people',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
