# Generated by Django 2.2.6 on 2019-12-05 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS361WebApp', '0003_prioritylist_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'TA'), (2, 'Instructor'), (3, 'Administrator')], null=True),
        ),
    ]
