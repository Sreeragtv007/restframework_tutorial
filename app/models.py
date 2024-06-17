from django.db import models

# Create your models here.

class Students(models.Model):
    student_name=models.TextField()
    student_age=models.IntegerField()
    student_place=models.CharField(max_length=100)
    student_class=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.student_name
    
    