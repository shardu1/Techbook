# Generated by Django 4.1.5 on 2023-08-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.CharField(max_length=230),
        ),
    ]
