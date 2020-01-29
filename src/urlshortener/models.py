from django.db import models

class SussURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return str(self.url) #self.id or self.pk to get the id

    def __unicode__(self):
        return str(self.url)
