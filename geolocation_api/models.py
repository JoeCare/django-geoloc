from django.db import models
import os, requests
# Create your models here.


class Locator(models.Model):

	request_ipv4 = models.CharField(max_length=15, default='check',
									help_text='Please input desired IP address')
	# request_ipv4 = 'check'
	# access_key =
	# data_format = '&output=json'

	# @property
	# def revealed_info(self):
	# 	return self.info if self.revealed else None
