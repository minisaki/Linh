# Generated by Django 3.0.4 on 2020-04-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_myuser_string_verify_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='make_varify_email_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]