# Generated by Django 4.0.1 on 2022-01-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_jarvis_list_document_title_jarvis_list_document_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='oil_moneyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('oil_type', models.CharField(max_length=10)),
                ('oil_money', models.FloatField()),
            ],
        ),
    ]
