import uuid
from django.db import models


class Experience(models.Model):
    CATEGORY_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-time'),
        ('full-time', 'Full-time'),
        ('freelance', 'Freelance'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='full-time',
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None

class Achievement(models.Model) :
    LEVEL_CHOISES = [ ('campus','Campus'), ('national','National'),('international','International')
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=255,choices=LEVEL_CHOISES,default = 'campus')
    achieved_at = models.DateField()

    def __str__(self) :
        return self.title

    def is_top_tier(self) :
        return self.level in ['international','national']