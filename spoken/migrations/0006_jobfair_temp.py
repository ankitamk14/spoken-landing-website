# Generated by Django 3.0.5 on 2020-04-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoken', '0005_remove_jobfair_widget_group_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobfair',
            name='temp',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
