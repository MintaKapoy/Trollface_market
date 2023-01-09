from django.db import models


class MetaTagMixin(models.Model):
    name = None
    title = None
    meta_title = models.CharField(verbose_name="Meta title", max_length=255, null=True, blank=True)
    meta_description = models.CharField(verbose_name="Meta description", max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(verbose_name="Meta keywords", max_length=255, null=True, blank=True)

    def get_meta_title(self):
        if self.meta_title:
            return self.meta_title
        else:
            return self.name or self.title

    class Meta:
        abstract = True
