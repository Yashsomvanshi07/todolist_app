from django.db import models

class Tasklist(models.Model):  
    task = models.CharField(max_length=500)  # A field for storing a task description
    done = models.BooleanField(default=False)  # A field for tracking task completion, defaults to False
    
    def __str__(self):  
        return self.task + " - " + str(self.done)
