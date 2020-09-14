# Generated by Django 3.1 on 2020-08-24 02:05

from django.db import migrations
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0007_ratemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratemodel',
            name='f3',
            field=simplepro.components.fields.RateField(default=3.5, verbose_name='评分3'),
        ),
    ]