# Generated by Django 3.2.2 on 2021-05-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_todo_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
