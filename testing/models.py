from django.db import models

# Create your models here.
class OTPcontact(models.Model):
    Contact = models.CharField(max_length=15)
    OTP = models.CharField(max_length=6)
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=254)
    def __str__(self):
        return self. Contact