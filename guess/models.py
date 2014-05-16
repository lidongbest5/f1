from django.db import models
import datetime

class Driver(models.Model):
	cname = models.CharField(max_length=128)
	ename = models.CharField(max_length=128)
	team = models.CharField(max_length=128)
	rate = models.FloatField()
	def __unicode__(self):
		return self.cname

class Races(models.Model):
	name = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	champion = models.IntegerField(default=0)
	championName = models.CharField(max_length=128,blank=True)
	finish = models.IntegerField()
	def __unicode__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=128)
	score = models.FloatField()
	time = models.DateTimeField(blank=True,null=True)
	blackList = models.IntegerField(default=1)
	phone = models.CharField(max_length=128,blank=True,null=True)
	address = models.CharField(max_length=512,blank=True,null=True)
	rname = models.CharField(max_length=128,blank=True,null=True)
	code = models.CharField(max_length=128,blank=True,null=True)
	def __unicode__(self):
		return self.name

class Content(models.Model):
	rule = models.TextField()
	contact = models.TextField()

class GuessList1(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList2(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList3(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList4(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList5(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList6(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList7(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList8(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList9(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList10(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList11(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList12(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList13(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList14(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList15(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList16(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList17(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList18(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessList19(models.Model):
	userid = models.CharField(max_length=128)
	raceName = models.CharField(max_length=128)
	rate = models.FloatField()
	score = models.FloatField()
	totalScore = models.FloatField()
	leftScore = models.FloatField()
	driverid = models.IntegerField()
	driverName = models.CharField(max_length=128)
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult1(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult2(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult3(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult4(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult5(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult6(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult7(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult8(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult9(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult10(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult11(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult12(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult13(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult14(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult15(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult16(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult17(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult18(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

class GuessResult19(models.Model):
	userid = models.CharField(max_length=128)
	score = models.FloatField()
	totalScore = models.FloatField()
	time = models.DateTimeField(blank=True,default=datetime.datetime.now())
	def __unicode__(self):
		return self.userid

