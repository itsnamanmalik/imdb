from django.db import models



class Movie(models.Model):
    name = models.CharField(blank=False,null=False,max_length=100)
    year = models.CharField(null=False,blank=False,max_length=20)
    rating = models.FloatField(null=False, blank=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Movies"
