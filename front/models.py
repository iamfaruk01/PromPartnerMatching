from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    preferred_partners = models.TextField(blank=True)
 
    def __str__(self):
        return self.name
