# Generated by Django 3.1.2 on 2020-10-28 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lvivarc', '0003_auto_20201028_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arcobj',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/Church of St. Nicholas.html'),
        ),
    ]
