# Generated by Django 4.0.3 on 2022-04-19 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('shop', models.TextField(blank=True)),
                ('item', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
