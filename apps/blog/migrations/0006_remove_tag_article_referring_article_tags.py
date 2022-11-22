# Generated by Django 4.1.3 on 2022-11-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='article_referring',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.tag', verbose_name='Тег'),
        ),
    ]
