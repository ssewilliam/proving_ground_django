from django.db import models

class Uploads(models.Model):
    file = models.FileField(blank=False, null=False)
    name = models.CharField(blank=False, max_length=255, null=False )

    def __str__(self):
        return self.file.name
