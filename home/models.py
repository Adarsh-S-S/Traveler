from django.db import models





class TourPackage(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    img=models.ImageField(upload_to="pic")
    discount=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)
    person=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.TextField()
    rating=models.DecimalField(max_digits=5, decimal_places=2)


