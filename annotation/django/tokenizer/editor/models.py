from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    state_text = models.CharField(max_length=10)

class TextFile(models.Model):
    file_name = models.CharField(max_length=50)
    file_location = models.CharField(max_length=200)
    first_worker = models.ForeignKey(User, related_name="first_worker")
    first_worker_state = models.ForeignKey(Status, related_name="first_worker_state")
    first_worker_comment = models.TextField(blank=True)
    second_worker = models.ForeignKey(User, related_name="second_worker")
    second_worker_state = models.ForeignKey(Status, related_name="second_worker_state")
    second_worker_comment = models.TextField(blank=True)
    judge = models.ForeignKey(User, related_name="judge")
    jurisdiction_state = models.ForeignKey(Status, related_name="jurisdiction_state")
    file_content1 = models.TextField(blank=True)
    file_content2 = models.TextField(blank=True)
    file_content_final = models.TextField(blank=True)
    file_content_original = models.TextField(blank=True)

class RegexFix(models.Model):
    pattern = models.CharField(max_length=200)
    replacement = models.CharField(max_length=200)
