# Generated by Django 3.0.8 on 2020-08-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdpacapps', '0002_auto_20200810_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endorsement_list',
            name='end_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
