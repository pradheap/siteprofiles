from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save

# Student Class relates default user model

class UserProfile(models.Model):
    user = models.OneToOneField(User,blank=True,related_name='colleger')
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address_line1 = models.CharField(max_length=16)
    address_line2 = models.CharField(max_length=16)
    address_line3 = models.CharField(max_length=16)
    pincode = models.CharField(max_length=16)
    area = models.CharField(max_length=16)
    city = models.CharField(max_length=16)
    mobile = models.CharField(max_length=16)
    website = models.CharField(max_length=16)
    
    @property
    def is_student(self):
        try:
            self.student
            return True
        except Student.DoesNotExist:
            return False
    
class Skills(models.Model):
    SKILLS = (
        ('mech', 'MECH'),
        ('eee', 'EEE'),
        ('cs', 'CS'),
        ('it', 'IT'),
    )
    RATING = (
        ('beginner', 'Beginner'),
        ('learner', 'Learner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    )
    skill = models.CharField(max_length=8, choices=SKILLS)
    rating = models.CharField(max_length=8, choices=RATING)
    

class Student(UserProfile):
    YEAR_IN = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    )
    BRANCHES = (
        ('mech', 'MECH'),
        ('eee', 'EEE'),
        ('cs', 'CS'),
        ('it', 'IT'),
    )
    student = models.OneToOneField(UserProfile,related_name='student') 
    skillset = models.ForeignKey(Skills,related_name='skills')
    passport = models.CharField(max_length=16)
    #resume = models.FileField()
    dob = models.DateTimeField()
    #avatar = models.FileField()
    roll_no = models.CharField(max_length=24)
    register_no = models.CharField(max_length=24)
    year = models.CharField(max_length=2, choices=YEAR_IN)
    branch = models.CharField(max_length=8, choices=BRANCHES)

class Employer(UserProfile):
    employer = models.OneToOneField(UserProfile,related_name='employer') 
    emp_id = models.CharField(max_length=24)

