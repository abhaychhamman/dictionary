# Generated by Django 2.2.6 on 2022-06-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0002_dictionary_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='key',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
