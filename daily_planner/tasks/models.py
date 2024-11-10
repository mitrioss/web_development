from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('В работе', 'В работе'),
        ('Направлена в работу', 'Направлена в работу'),
        ('Выполнена', 'Выполнена'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)  # Добавляем поле для дедлайна

    def __str__(self):
        return self.title
