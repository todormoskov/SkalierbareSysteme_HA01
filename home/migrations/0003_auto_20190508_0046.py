# Generated by Django 2.2.1 on 2019-05-08 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190507_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aufgaben',
            name='aufgabe',
            field=models.TextField(max_length=160),
        ),
    ]
