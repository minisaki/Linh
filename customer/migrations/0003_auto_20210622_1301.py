# Generated by Django 3.0.4 on 2021-06-22 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20210622_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='content_report',
        ),
        migrations.AddField(
            model_name='report',
            name='content_report',
            field=models.ManyToManyField(null=True, related_name='text_report', to='customer.TextReport'),
        ),
    ]