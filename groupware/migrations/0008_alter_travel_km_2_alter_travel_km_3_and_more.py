# Generated by Django 4.0.1 on 2022-01-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupware', '0007_travel_total_km'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='km_2',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='km_3',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='km_4',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='km_5',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='total_km',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
