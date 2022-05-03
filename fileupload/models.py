from django.db import models


class StoreDoc(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    file = models.FileField(
        upload_to='documents/%m/%d/%Y/', blank=True, null=True)

    def __str__(self):
        return self.name
