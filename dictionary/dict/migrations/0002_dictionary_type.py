# Generated by Django 2.2.6 on 2022-06-03 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='type',
            field=models.CharField(default='', max_length=40),
        ),
    ]
