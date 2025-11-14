from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ])

    def __str__(self):
        return f"{self.name} - {self.client_name}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    project_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    budget = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
