# Generated by Django 4.1.2 on 2022-11-22 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nuru', '0008_remove_message_date_time_remove_message_message_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='Phone_number',
        ),
    ]
