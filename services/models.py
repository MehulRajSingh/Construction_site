from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField(default="No description provided.")
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.CharField(max_length=100, default="General")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# from django.db import models
# from django.urls import reverse
# from django.utils.text import slugify
# from django.utils import timezone
    
# class Service(models.Model):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True, blank=True)
#     description = models.TextField(blank=True, default='')  # Add blank=True and default
#     base_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     featured_image = models.ImageField(upload_to='services/', null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('services:service_detail', kwargs={'slug': self.slug})

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['name']

# class ServiceImage(models.Model):
#     service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_images')
#     image = models.ImageField(upload_to='services/gallery/')
#     caption = models.CharField(max_length=200, blank=True)
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"Image for {self.service.name}"

# class ServiceFeature(models.Model):
#     service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='features')
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     icon = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.title

#     def get_icon_class(self):
#         icon_map = {
#             'construction': 'fas fa-hard-hat',
#             'renovation': 'fas fa-paint-roller',
#             'design': 'fas fa-drafting-compass',
#             'consultation': 'fas fa-comments',
#             'maintenance': 'fas fa-tools',
#             'repair': 'fas fa-wrench',
#         }
#         return icon_map.get(self.icon, 'fas fa-check')