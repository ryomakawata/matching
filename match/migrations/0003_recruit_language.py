# Generated by Django 2.1.5 on 2020-06-20 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='language',
            field=models.CharField(choices=[('JAVA', 'JANA'), ('C', 'C'), ('C++', 'C++'), ('C#', 'C#'), ('Javascript', 'Javascript'), ('jQuery', 'jQuery'), ('HTML・CSS', 'HTML・CSS'), ('PHP', 'PHP'), ('Ruby', 'Ruby'), ('Python', 'Python'), ('Objective-c', 'Objective-c'), ('Swift', 'Swift')], max_length=25, null=True),
        ),
    ]
