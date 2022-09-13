from django.db import models

# Create your models here.

class Persona:
    def __init__(self):
        self.nombre = models.CharFied(max_length = 50)
        
    def __str__(self):
        return self.nombre

