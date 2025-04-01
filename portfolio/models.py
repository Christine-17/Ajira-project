from django.db import models

class AjiraInfo(models.Model):
    mission = models.TextField()
    vision = models.TextField()
    motto = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    link = models.URLField()

    def __str__(self):
        return self.motto
