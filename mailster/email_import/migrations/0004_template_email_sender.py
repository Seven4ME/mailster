# Generated by Django 3.0.5 on 2020-05-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_import', '0003_auto_20200518_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='email_sender',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
