# Generated by Django 4.1.3 on 2023-01-09 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta description'),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta keywords'),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta title'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta description'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta keywords'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta title'),
        ),
        migrations.AddField(
            model_name='tag',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta description'),
        ),
        migrations.AddField(
            model_name='tag',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta keywords'),
        ),
        migrations.AddField(
            model_name='tag',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta title'),
        ),
    ]