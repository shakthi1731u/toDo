from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def toggle_complete(self):
        self.completed = not self.completed
        self.save()

    def __str__(self):
        return self.title

