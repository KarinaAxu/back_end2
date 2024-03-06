from django.db import models

class Todo(models.Model):
    title = models.CharField(null=False, max_length=100, default='')
    description = models.CharField(null=False, max_length=255, blank=True, default='')
    due_date = models.DateField(null=False, blank=False)
    status = models.BooleanField(default=False)

class Meta:
    verbose_name = 'Todo'
    verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title