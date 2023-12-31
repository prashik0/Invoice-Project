from django.db import models

class Invoice(models.Model):
    customer_name = models.CharField(max_length=255)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.pk} {self.customer_name} {self.date}"

    
class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.pk} Desc" 
