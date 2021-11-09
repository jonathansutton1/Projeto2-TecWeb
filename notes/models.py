from django.db import models

class Fin(models.Model):
    symbol = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=12, decimal_places=4)
    date = models.DateField()
    id = models.AutoField(primary_key=True)    
    
    def __str__(self):
        
        return ("{0}.{1}".format(self.id, self.symbol))