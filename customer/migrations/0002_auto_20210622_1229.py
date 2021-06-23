# Generated by Django 3.0.4 on 2021-06-22 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='content_report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_report', to='customer.TextReport'),
        ),
    ]