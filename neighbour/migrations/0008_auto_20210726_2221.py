# Generated by Django 3.1.7 on 2021-07-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0007_auto_20210726_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]