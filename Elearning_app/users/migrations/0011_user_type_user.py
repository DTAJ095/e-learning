# Generated by Django 4.2.13 on 2024-07-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type_user',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
