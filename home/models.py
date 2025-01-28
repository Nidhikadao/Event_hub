from django.db import models


# Create your models here.
ACADEMIC_YR_CHOICES =[
        ("1", "1st year"),
        ("2", "2nd year"),
        ("3", "3rd year"),
        ("4", "4th year"),
    ]
COURSE_CHOICES=[
        ("1", "Btech"),
        ("2", "Polytech"),
        ("3", "BCA"),
        ("4", "BSC"),
        ("5", "BBA")
    ]
CLUB_CHOICES= [
        ("1", "Technology"),
        ("2", "Creativity"),
        ("3", "Sports"),
        ("4", "Cultural"),
        ("5", "Reasearch"),
    ]
    
class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    fname= models.CharField(max_length=250)
    lname= models.CharField(max_length=250)
    email= models.CharField(max_length=100)
    collegename=models.CharField(max_length=500)
    academicyr= models.CharField(
        max_length=20,
        choices= ACADEMIC_YR_CHOICES,
        default= '1'
    )
    course= models.CharField(
        max_length=20,
        choices= COURSE_CHOICES,
        default= '1'
    )
    clubs= models.CharField(
        max_length=20,
        choices= CLUB_CHOICES,
        default= '1'
    )
    describe= models.TextField()
    timeStamp= models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__ (self):
        return f'{self.fname} {self.lname} - {self.email}'