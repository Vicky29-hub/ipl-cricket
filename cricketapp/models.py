from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Login(AbstractUser):
    usertype=models.CharField(max_length=40)
    viewpassword=models.CharField(max_length=40)

class Register(models.Model):
    name=models.CharField(max_length=40,null=True)
    Address=models.CharField(max_length=40,null=True)
    email=models.CharField(max_length=40,null=True)
    phone=models.CharField(max_length=40,null=True)
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)

class Club(models.Model):
    name = models.CharField(max_length=40,null=True)
    owner = models.CharField(max_length=40,null=True)
    email=models.CharField(max_length=40,null=True)
    contact_number = models.CharField(max_length=20,null=True)
    logo = models.ImageField(upload_to="uploadImage",max_length=None,null=True)
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    # team1_fixtures = models.ForeignKey(Fixture, related_name='team1', on_delete=models.CASCADE)
    # team2_fixtures = models.ForeignKey(Fixture, related_name='team2', on_delete=models.CASCADE)
    

class Fixture(models.Model):
    date = models.DateField(null=True)
    venue = models.CharField(max_length=100,null=True)
    team1 = models.ForeignKey(Club, related_name='team1_fixtures', on_delete=models.CASCADE,null=True)
    team2 = models.ForeignKey(Club, related_name='team2_fixtures', on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=20, default='Scheduled',null=True)
    result = models.CharField(max_length=100, blank=True, null=True)

class Player(models.Model):
    image= models.ImageField(upload_to="uploadImage",max_length=None,null=True)
    name = models.CharField(max_length=100,null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE,null=True)
    age = models.IntegerField(null=True)
    role=models.CharField(max_length=100,null=True)
    batting_average = models.FloatField(null=True)
    bowling_average = models.FloatField(null=True)

class News(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    image= models.ImageField(upload_to="uploadImage",max_length=None,null=True)
    content = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True,null=True)

class Feedback(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE,null=True)
    feedback = models.TextField(null=True)
    date_submitted = models.DateTimeField(auto_now_add=True,null=True)

class Complaint(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE,null=True)
    complaint = models.TextField(null=True)
    date_submitted = models.DateTimeField(auto_now_add=True,null=True)
