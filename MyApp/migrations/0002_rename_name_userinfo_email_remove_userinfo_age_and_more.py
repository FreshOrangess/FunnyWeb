# Generated by Django 4.0.3 on 2022-04-13 23:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='name',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='age',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=32),
            preserve_default=False,
        ),
    ]
