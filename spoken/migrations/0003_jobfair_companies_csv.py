# Generated by Django 3.0.5 on 2020-04-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoken', '0002_jobfair_brochure'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobfair',
            name='companies_csv',
            field=models.FileField(default='', upload_to='companies_csv/'),
        ),
    ]