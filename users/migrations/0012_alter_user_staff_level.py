# Generated by Django 4.0 on 2021-12-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_user_staff_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='staff_level',
            field=models.IntegerField(default=99),
        ),
    ]