from django.db import models
from accounts.models import *
# Create your models here.

# class FriendsList(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name="user_id")
#     friends_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name="friends_id")


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True,related_name="sender_message_set")
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True,related_name="reciever_message_set")
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.sender.first_name}-{self.sender.last_name}'


class ChatList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True,related_name="user")
    expert = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True,related_name="expet")

    class Meta:
        unique_together = ('user', 'expert')