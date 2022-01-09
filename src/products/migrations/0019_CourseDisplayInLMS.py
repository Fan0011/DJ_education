# Generated by Django 3.2.10 on 2022-01-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_ProductGroups'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='display_in_lms',
            field=models.BooleanField(default=True, help_text='If disabled will not be shown in LMS', verbose_name='Display in LMS'),
        ),
    ]
