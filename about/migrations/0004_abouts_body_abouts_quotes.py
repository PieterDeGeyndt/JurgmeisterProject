# Generated by Django 4.0 on 2021-12-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_rename_about_abouts'),
    ]

    operations = [
        migrations.AddField(
            model_name='abouts',
            name='body',
            field=models.TextField(default='Dit is fake bodytext, vervang mij in de admin'),
        ),
        migrations.AddField(
            model_name='abouts',
            name='quotes',
            field=models.TextField(default='Dit is fake quotetext, vervang mij in de admin'),
        ),
    ]
