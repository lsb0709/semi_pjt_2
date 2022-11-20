# Generated by Django 3.2.13 on 2022-11-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupcard',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='socks',
            field=models.IntegerField(blank=True),
        ),
    ]