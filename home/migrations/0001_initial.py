# Generated by Django 2.2.1 on 2019-05-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aufgaben',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aufgabe', models.CharField(max_length=160)),
                ('deadline', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
