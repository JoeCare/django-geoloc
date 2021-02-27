from django.db import models
import os
# Create your models here.


class Locator(models.Model):

	request_ipv4 = models.CharField(max_length=15, default='check')
	# request_ipv4 = 'check'
	# access_key = os.getenv('ipstackKey')
	# data_format = '&output=json'
	# base_url = f'http://api.ipstack.com/{request_ipv4}?access_key={access_key}'

	# @property
	# def revealed_info(self):
	# 	return self.info if self.revealed else None
