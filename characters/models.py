from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='characters/', null=True, blank=True)  

    def __str__(self):
        return self.name

class Move(models.Model):
    character=models.ForeignKey(Character, on_delete = models.CASCADE, null=True)
    command = models.CharField(max_length=100)
    hitlevel = models.CharField(max_length=100)
    damage = models.CharField(max_length=100)
    startup = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    hit = models.CharField(max_length=100)
    counterhit = models.CharField(max_length=100)

    def __str__(self):
        return (self.id)
