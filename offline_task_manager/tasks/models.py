from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    time_to_complete = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_synced = models.BooleanField(default=False)

    def __str__(self):
        formatted_date = self.created_at.strftime('%y/%m/%d')  # Formata a data
        return f"{self.name} - {formatted_date}"
