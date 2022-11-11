# Generated by Django 3.2.13 on 2022-11-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age_range',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='introduce',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='user',
            name='profileimage',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]