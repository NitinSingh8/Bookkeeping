# Generated by Django 4.0.3 on 2022-04-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourrecord',
            name='price',
            field=models.FloatField(),
        ),
    ]
