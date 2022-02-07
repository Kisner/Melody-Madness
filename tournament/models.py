# Create your models here.
from django.db import models


class Vote(models.Model):
    # which round were in
    round_num = models.IntegerField(default=0)
    # did the round start or not
    round_started = models.IntegerField(default=0)

    # keeps tally of votes
    option_0_count = models.IntegerField(default=0)
    option_1_count = models.IntegerField(default=0)
    option_2_count = models.IntegerField(default=0)
    option_3_count = models.IntegerField(default=0)
    option_4_count = models.IntegerField(default=0)
    option_5_count = models.IntegerField(default=0)
    option_6_count = models.IntegerField(default=0)
    option_7_count = models.IntegerField(default=0)
    option_8_count = models.IntegerField(default=0)
    option_9_count = models.IntegerField(default=0)
    option_10_count = models.IntegerField(default=0)
    option_11_count = models.IntegerField(default=0)
    option_12_count = models.IntegerField(default=0)
    option_13_count = models.IntegerField(default=0)
    option_14_count = models.IntegerField(default=0)
    option_15_count = models.IntegerField(default=0)

    #artists winners
    winner1 = models.CharField(max_length=100, default="")
    winner2 = models.CharField(max_length=100, default="")
    winner3 = models.CharField(max_length=100, default="")
    winner4 = models.CharField(max_length=100, default="")
    winner5 = models.CharField(max_length=100, default="")
    winner6 = models.CharField(max_length=100, default="")
    winner7 = models.CharField(max_length=100, default="")
    winner8 = models.CharField(max_length=100, default="")


