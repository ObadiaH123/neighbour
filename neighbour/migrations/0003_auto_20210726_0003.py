# Generated by Django 3.1.7 on 2021-07-25 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0002_auto_20210725_2302'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Post',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='followed',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='follower',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]