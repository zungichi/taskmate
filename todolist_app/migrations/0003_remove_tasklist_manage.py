# Generated by Django 4.0.3 on 2022-05-14 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_tasklist_manage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='manage',
        ),
    ]
