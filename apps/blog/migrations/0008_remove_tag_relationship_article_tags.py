# Generated by Django 4.1.3 on 2022-11-26 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_article_tags_tag_relationship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='relationship',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.tag', verbose_name='Тег'),
        ),
    ]
