# Generated by Django 4.0.2 on 2022-03-04 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0004_rename_category_category_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='ABC', through='postings.TagList', to='postings.Tag'),
        ),
    ]
