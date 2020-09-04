from django.db import models

class Division(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Upazila(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    full_Name = models.CharField(max_length=45)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    upazila = models.ForeignKey(Upazila, on_delete=models.SET_NULL, blank=True, null=True)
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    email = models.EmailField(max_length=255, unique=True)
    mobile_No = models.CharField(max_length=11, unique=True)
    date_of_Birth = models.DateField()
    university_choice = (
        ('Bangladesh Agricultural University', 'Bangladesh Agricultural University'),
        ('Hajee Mohammad Danesh Science and Technology University', 'Hajee Mohammad Danesh Science and Technology University'),
        ('Khulna University', 'Khulna University'),
        ('Noakhali Science and Technology University', 'Noakhali Science and Technology University'),
        ('Patuakhali Science & Technology University', 'Patuakhali Science & Technology University'),
        ('University of Rajshahi', 'University of Rajshahi'),
        ('Sher-e-Bangla Agricultural University', 'Sher-e-Bangla Agricultural University'),
        ('Sylhet Agricultural University', 'Sylhet Agricultural University'),
        ('Others', 'Others'),
    )
    university_Name = models.CharField(choices=university_choice, max_length=100)
    picture = models.ImageField(upload_to='images/', blank=True)

    
    def __str__(self):
        return self.full_Name
