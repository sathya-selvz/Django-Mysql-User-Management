from django.db import models

class UserData(models.Model):  
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    # Foreign Key → connects to UserData
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)

    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.user.name}'s Profile"
