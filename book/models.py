from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Entry(models.Model):
	content	   = models.TextField()
	sender     = models.ForeignKey(User, related_name='entry_senders')
	recipient  = models.ForeignKey(User, related_name='entry_receivers')
	posted	   = models.DateTimeField(auto_now_add=True)
