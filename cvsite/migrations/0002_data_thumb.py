# Generated by Django 3.0.7 on 2020-06-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]