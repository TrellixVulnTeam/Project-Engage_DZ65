# Generated by Django 2.2.4 on 2019-09-06 06:53

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20190903_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorurl',
            name='url',
            field=models.CharField(max_length=1000, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]
