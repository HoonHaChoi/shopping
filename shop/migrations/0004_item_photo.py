# Generated by Django 2.1.4 on 2019-01-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_item_is_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]