from django.db import models

class Team(models.Model):
    #team_digraph = models.CharField(max_length=2, primary_key=True)
    team_location = models.CharField(max_length=30)
    team_name = models.CharField(max_length=30)

    class Meta:
        ordering = ('team_location',)

    def __unicode__(self):
        return "%s %s" % (self.team_location, self.team_name)

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=2)
    depth = models.PositiveIntegerField(blank=True)
    team = models.ForeignKey(Team)
    score = models.IntegerField(blank=True)
    
    class Meta:
        ordering = ('last_name',)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

class User(models.Model):
    user_name = models.CharField(max_length=30)
    score = models.IntegerField(blank=True)
    team = models.ForeignKey(Team)

    class Meta:
        ordering = ('user_name',)
    
    def __unicode__(self):
        return self.user_name

