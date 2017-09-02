# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models

class Album(models.Model):
	user=models.ForeignKey(User,default=1)
	artist=models.CharField(max_length=100)
	album_title=models.CharField(max_length=100)
	genre=models.CharField(max_length=100)
	album_logo=models.FileField()
	is_favorite = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('Music:detail',kwargs={'pk':self.pk})

	def __str__(self):
		return self.artist +' - '+ self.album_title



class Song(models.Model):
	album = models.ForeignKey(Album,on_delete=models.CASCADE)
	song_title=models.CharField(max_length=100)
	audio_file=models.FileField(default='')
	is_favorite=models.BooleanField(default=False)
	
	def __str__(self):
		return self.song_title



