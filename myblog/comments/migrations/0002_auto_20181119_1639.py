# Generated by Django 2.1.2 on 2018-11-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]