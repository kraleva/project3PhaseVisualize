from django.db import models

class Following(models.Model):
    follower = models.OneToOneField('User', models.DO_NOTHING,related_name="follower", primary_key=True)
    user = models.OneToOneField('User', models.DO_NOTHING,related_name="user", primary_key = True)
    class Meta:
        managed = False
        db_table = 'following'
        unique_together = (('follower', 'user'),)

class Relationship(models.Model):
    user1 = models.OneToOneField('User', models.DO_NOTHING,related_name="user1", primary_key=True)
    user2 = models.OneToOneField('User', models.DO_NOTHING,related_name="user2", primary_key=True)
    user1_retweettimes = models.IntegerField()
    user2_retweettimes = models.IntegerField()
    typeofrelationship = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'relationship'
        unique_together = (('user1', 'user2'),)

    def __str__(self):
        return self.typeofrelationship

class Tweet(models.Model):
    tweet_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField('User', models.DO_NOTHING)
    createdat = models.DateField(blank=True, null=True)
    tweet = models.CharField(max_length=280, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tweet'
    def __str__(self):
        return self.tweet

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    screenname = models.CharField(max_length=32)
    location = models.CharField(max_length=50, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    protected = models.BooleanField()
    verified = models.BooleanField()
    followers = models.IntegerField()
    friends = models.IntegerField()
    listed = models.IntegerField()
    favourites = models.IntegerField()
    statuses = models.IntegerField()
    createdat = models.DateTimeField(blank=True, null=True)
    defaultacc = models.BooleanField()
    hobby1 = models.CharField(max_length=32, blank=True, null=True)
    hobby2 = models.CharField(max_length=32, blank=True, null=True)
    isbrillentrager = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.screenname

# Create your models here.
