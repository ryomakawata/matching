# Generated by Django 2.1.5 on 2020-06-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
