# Generated by Django 3.1.2 on 2020-10-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lvivarc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arcobj',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
