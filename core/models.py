from django.db import models

# Create your models here.


class Message(models.Model):
    message_name = models.CharField(max_length=80)
    message_email = models.EmailField(max_length=254)
    message_phone = models.CharField(max_length=15, blank=True, null=True)
    message_text = models.TextField()

    def __str__(self):
        return self.message_email