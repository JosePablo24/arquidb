from django.db import models
from django.utils import timezone

class Example(models.Model):
    name_example = models.CharField(max_length=254, null=False)
    year_example = models.IntegerField(null=False)
    delete_example = models.BooleanField(default=False)
    create_example = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name_example
    
    class Meta: 
        db_table = 'Exampe'