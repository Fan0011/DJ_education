# Generated by Django 3.1.7 on 2021-04-11 15:12

from django.db import migrations, models
from django.db.migrations.operations.fields import RemoveField


class Migration(migrations.Migration):

    dependencies = [
        ('a12n', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordlessauthtoken',
            name='used',
        ),
        migrations.AddField(
            model_name='passwordlessauthtoken',
            name='used',
            field=models.DateTimeField(null=True),
        ),
    ]
