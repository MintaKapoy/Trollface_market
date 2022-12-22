from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.safestring import mark_safe
from config.settings import MEDIA_ROOT


class BlogCategory(models.Model):
    name = models.CharField(verbose_name="Ім'я категоріі", max_length=255)
    image = ProcessedImageField(verbose_name="Зображеня", upload_to="blog/category/",
                                processors=[ResizeToFill(600, 400)], null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія блога"
        verbose_name_plural = "Категорії блога"

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width=70>")

    image_tag_thumbnail.short_description = "Зображення"

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = "Зображення"


class Tag(models.Model):
    name = models.CharField(verbose_name="Тег", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Article(models.Model):
    category = models.ForeignKey(to=BlogCategory, verbose_name="Категорії", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    text_preview = models.TextField(verbose_name="Текст-превью", null=True, blank=True)
    text = models.TextField(verbose_name="Текст")
    publish_date = models.DateTimeField(verbose_name="Дата публікації")
    tags = models.ManyToManyField(to=Tag, verbose_name="Тег", related_name="articles", blank=True)
    image = ProcessedImageField(verbose_name="Зображеня", upload_to="blog/article/", null=True, blank=True)
    image_thumbnail = ImageSpecField(source="image", processors=[ResizeToFill(600, 400)])
    updated_at = models.DateTimeField(verbose_name="Дата змінення", auto_now=True)
    created_at = models.DateTimeField(verbose_name="Дата ствонення", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
