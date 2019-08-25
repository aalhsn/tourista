from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    pretty_picture = models.ImageField()
    activities = models.TextField()
    optimal_visiting_season = models.CharField(max_length=10)


    def __str__(self):
    	return self.name

    def save(self, *args, **kwargs):
	    for field_name in ['name', 'activities',"optimal_visiting_season"]:
	        val = getattr(self, field_name, False)
	        if val:
	            setattr(self, field_name, val.capitalize())
	    super(Destination, self).save(*args, **kwargs)