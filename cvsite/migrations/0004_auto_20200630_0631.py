# Generated by Django 3.0.5 on 2020-06-30 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvsite', '0003_auto_20200630_0618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='Description',
            new_name='description',
        ),
    ]
