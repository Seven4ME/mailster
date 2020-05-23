# Generated by Django 3.0.5 on 2020-05-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_import', '0002_campaign_email_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='email_subject',
        ),
        migrations.AddField(
            model_name='template',
            name='email_subject',
            field=models.CharField(default='', max_length=255),
        ),
    ]