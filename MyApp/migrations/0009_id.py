# Generated by Django 4.0.3 on 2022-04-22 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_rename_message_sender_messages_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
