# Generated by Django 3.0 on 2020-10-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20201005_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='/static/images/cover.jpg', null=True, upload_to='img'),
        ),
    ]
