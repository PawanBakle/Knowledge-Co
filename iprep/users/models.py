from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    ROLE_CHOICE = [('FRONTEND','Frontend Developer'),('BACKEND','Backend Developer'),('DEVOPS','Devops Engineer')]
    name = models.CharField(max_length=50,choices=ROLE_CHOICE)
    def __str__(self):
        return self.get_name_display()
# Create your models here.
class CustomUser(AbstractUser):
    EXP = [('LEARNER','Learner'),('INTERMEDIATE','Intermediate'),('PROFESSIONAL','Professional')]
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    experience_level = models.CharField(max_length=20,choices=EXP)
    profile_completed = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.get_name_display()







