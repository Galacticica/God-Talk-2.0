from django.db import models
from accounts.models import User

# class Message(models.Model):
#     body = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
