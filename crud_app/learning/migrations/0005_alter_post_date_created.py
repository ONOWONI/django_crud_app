# Generated by Django 4.0.6 on 2022-08-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]