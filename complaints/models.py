from django.db import models

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    complaint_type = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='complaints/', null=True, blank=True)
    
    
    
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)


    status = models.CharField(max_length=50, default="Submitted")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name