# Generated by Django 4.1.1 on 2022-09-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='typ',
            field=models.CharField(default='Action', max_length=200),
        ),
    ]
