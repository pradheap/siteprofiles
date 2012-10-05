from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save

# Student Class relates default user model

class UserProfile(models.Model):
    user = models.OneToOneField(User,blank=True,related_name='colleger')
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    mobile = models.CharField(max_length=12)
    
    @property
    def is_student(self):
        try:
            self.student
            return True
        except Student.DoesNotExist:
            return False
    
class Address(models.Model):
    website = models.CharField(max_length=32)
    blog = models.CharField(max_length=32)
    address_line1 = models.CharField(max_length=32)
    address_line2 = models.CharField(max_length=32)
    address_line3 = models.CharField(max_length=32)
    pincode = models.CharField(max_length=6)
    area = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    country = models.CharField(max_length=24)
    phone = models.CharField(max_length=16)
    

class College(models.Model):
    AFFILIATION = (
        ('anna_univ', 'Anna University'),
        ('deemed', 'Deemed'),
        ('autonomous', 'Autonomous'),
    )
    TYPE = (
        ('govt', 'Government'),
        ('govt_aid', 'Government-Aided'),
        ('private', 'Private'),
    )
    address = models.ForeignKey(Address)
    name = models.CharField(max_length=64)
    ugc_cgpa = models.CharField(max_length=16)
    ugc_grade = models.CharField(max_length=16)
    established = models.CharField(max_length=16)
    faculties = models.CharField(max_length=4)
    affiliation = models.CharField(max_length=12, choices=AFFILIATION)
    type = models.CharField(max_length=12, choices=TYPE)
    
class Skill(models.Model):
    SKILLS = (
        ('c', 'C'),
        ('cpp', 'C++'),
        ('vb', 'VB'),
        ('java', 'JAVA'),
    )
    TYPES = (
        ('soft', 'Soft-Skills'),
        ('it', 'IT-Skills'),
    )
    skill = models.CharField(max_length=8, choices=SKILLS)
    skill_type = models.CharField(max_length=8, choices=TYPES)

class Student(UserProfile):
    student = models.OneToOneField(UserProfile,related_name='student')
    skills = models.ManyToManyField(Skill, through='SkillSet')
    study = models.ManyToManyField(College, through='Education')
    address = models.ForeignKey(Address)
    passport = models.CharField(max_length=16)
    #resume = models.FileField()
    dob = models.DateTimeField()
    #avatar = models.FileField()
    roll_no = models.CharField(max_length=24)
    register_no = models.CharField(max_length=24)
 
class Professor(UserProfile):
    professor = models.OneToOneField(UserProfile,related_name='professor')
    working = models.ManyToManyField(College, through='Teaching') 
    address = models.ForeignKey(Address)
    prof_id = models.CharField(max_length=24)

class Education(models.Model):
    YEAR_IN = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    )
    BRANCHES = (
        ('aero', 'Aeronautics'),
        ('auto', 'Automobile'),
        ('cs', 'Computer Science'),
        ('civ', 'Civil'),
        ('eee', 'Electrical and Electronics'),
        ('ece', 'Electronics and Communication'),
        ('it', 'Information Technology'),
        ('mech', 'Mechanical'),
        ('mecht', 'Mechatronics'),
    )
    college = models.ForeignKey(College)
    student = models.ForeignKey(Student)
    date_of_joining = models.DateTimeField()
    date_of_pass = models.DateTimeField()
    year = models.CharField(max_length=2, choices=YEAR_IN)
    branch = models.CharField(max_length=8, choices=BRANCHES)
    
class SkillSet(models.Model):
    RATING = (
        ('beginner', 'Beginner'),
        ('learner', 'Learner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    )
    skill = models.ForeignKey(Skill)
    student = models.ForeignKey(Student)
    rating = models.CharField(max_length=8, choices=RATING)
    best_score = models.CharField(max_length=8, choices=RATING)
    last_score = models.CharField(max_length=8, choices=RATING)
    
class Teaching(models.Model):
    BRANCHES = (
        ('aero', 'Aeronautics'),
        ('auto', 'Automobile'),
        ('cs', 'Computer Science'),
        ('civ', 'Civil'),
        ('eee', 'Electrical and Electronics'),
        ('ece', 'Electronics and Communication'),
        ('it', 'Information Technology'),
        ('mech', 'Mechanical'),
        ('mecht', 'Mechatronics'),
    )
    SUBJECTS = (
        ('maths', 'Maths'),
        ('ed', 'Engineering Drawing'),
        ('atd', 'Applied Thermodynamics'),
        ('pe', 'Power Electronics'),
    )
    college = models.ForeignKey(College)
    professor = models.ForeignKey(Professor)
    date_of_joining = models.DateTimeField()
    date_left = models.DateTimeField()
    subject = models.CharField(max_length=2, choices=SUBJECTS)
    branch = models.CharField(max_length=8, choices=BRANCHES)

class Employer(UserProfile):
    employer = models.OneToOneField(UserProfile,related_name='employer') 
    address = models.ForeignKey(Address)
    emp_id = models.CharField(max_length=24)
    company = models.CharField(max_length=40)

class Company(models.Model):
    address = models.ForeignKey(Address)
    name = models.CharField(max_length=48)
    head_count = models.CharField(max_length=8)
    revenue = models.CharField(max_length=12)
    head_quarters = models.CharField(max_length=64)    
    