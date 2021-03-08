from django.db import models
class Contact(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email= models.EmailField()
    ip_address = models.GenericIPAddressField(null=True)
    message= models.TextField()
    first_name= models.CharField(max_length=50)
    def __str__(self):
        return f'{self.first_name}{self.last_name}'

class FileUpload(models.Model):
    file = models.FileField(upload_to="pictures")

# Create your models here.
