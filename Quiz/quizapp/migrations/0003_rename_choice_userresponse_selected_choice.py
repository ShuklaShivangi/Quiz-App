# Generated by Django 5.0.4 on 2024-04-16 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_userresponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userresponse',
            old_name='choice',
            new_name='selected_choice',
        ),
    ]
