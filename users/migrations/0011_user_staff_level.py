# Generated by Django 4.0 on 2021-12-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_vacationuse_accepter_2_alter_vacationuse_accepter_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='staff_level',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]