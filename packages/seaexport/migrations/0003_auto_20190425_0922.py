# Generated by Django 2.1.3 on 2019-04-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seaexport', '0002_auto_20190424_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seaexportfreightbookingattachedfile',
            name='file',
            field=models.FileField(max_length=200, upload_to='media/'),
        ),
    ]
