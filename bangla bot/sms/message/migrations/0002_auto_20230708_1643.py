# Generated by Django 3.2.8 on 2023-07-08 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='info',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='number',
        ),
    ]
