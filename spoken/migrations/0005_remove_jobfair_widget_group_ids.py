# Generated by Django 3.0.5 on 2020-04-22 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spoken', '0004_jobfair_widget_group_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobfair',
            name='widget_group_ids',
        ),
    ]
