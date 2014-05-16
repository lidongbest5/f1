from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from guess.models import *
import urllib2
import urllib
from pyquery import PyQuery as pq
from django.utils import simplejson as json
import datetime, time, hashlib, requests
from BeautifulSoup import BeautifulSoup

races_list = [GuessList1,GuessList2,GuessList3,GuessList4,GuessList5,GuessList6,GuessList7,GuessList8,GuessList9,GuessList10,GuessList11,GuessList12,GuessList13,GuessList14,GuessList15,GuessList16,GuessList17,GuessList18,GuessList19]
result_list = [GuessResult1,GuessResult2,GuessResult3,GuessResult4,GuessResult5,GuessResult6,GuessResult7,GuessResult8,GuessResult9,GuessResult10,GuessResult11,GuessResult12,GuessResult13,GuessResult14,GuessResult15,GuessResult16,GuessResult17,GuessResult18,GuessResult19]

def showResult(id):
	result_db = result_list[id-1]
	p = result_db.objects.all().order_by('-totalScore','time')[0:20]
	for i in p:
		i.total = User.objects.get(name=i.userid).score
	return p

def showAllResult():
	p = User.objects.all().order_by('-score')[0:100]
	return p

def showPre(request):
	nn = 1
        for i in range(1,20):
       		if int(Races.objects.get(id=i).finish) == 0:
        		nn = i
        		break
	races = Races.objects.get(id=nn)
	return render_to_response('index.html',{'status':0,'data':showResult(nn),'races':races,'race_id':nn})

def setRe(request):
	nn = 1
        for i in range(1,20):
        	if int(Races.objects.get(id=i).finish) == 0:
        		nn = i
        		break
	Races.objects.filter(id=nn).update(finish=1)
	return HttpResponse("1")

def showRaces(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	if(request.session.get('member_id', False)):
		userid = request.session['member_id']
		user = {'islogin':True,'userid':userid,'score':getUserScore(userid),'index':getUserIndex(userid),'sign':getUserSign(userid)}
	else:
		user = {'islogin':False}
	races = Races.objects.get(id=offset)
	content = Content.objects.get(id=1)
	if(offset < 3):
		return render_to_response('index.html',{'status':3,'races':races,'race_id':offset,'user':user,'content':content})
	else:
		status = races.finish
		ostatus = Races.objects.get(id=offset-1).finish
		if(status == 1):
			return render_to_response('index.html',{'status':0,'data':showResult(offset),'races':races,'race_id':offset})
		elif(status == 0 and ostatus == 1):
			if(datetime.datetime.now().strftime("%Y-%m-%d %H:%i:%s") > (Races.objects.get(id=offset).time+datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%i:%s")):
				return render_to_response('index.html',{'status':4,'races':races,'race_id':offset,'user':user,'content':content})
			else:
				rate = Driver.objects.all().order_by('rate')	
				return render_to_response('index.html',{'status':1,'rate':rate,'races':races,'race_id':offset,'user':user,'content':content})
		else:
			return render_to_response('index.html',{'status':2,'races':races,'race_id':offset,'user':user,'content':content})


def showIndex(request):
	# getBet()
	mm = 1
	for i in range(1,20):
		if int(Races.objects.get(id=i).finish) == 0:
			mm = i
			break
	return HttpResponseRedirect('/f1/races/'+ str(mm) +'/')

def total(request):
	return render_to_response('index.html',{'status':6,'data':showAllResult(),'race_id':0})

def getBet():
	res = urllib2.urlopen('https://sports.bwin.com/en/sports/6/betting/formula-1').read()
	d = pq(res)
	for i in range(0,22):
		Driver.objects.filter(ename=d('.option-name').eq(i).html()).update(rate=float(d('.odds').eq(i).html()))

def login(request):
	if request.is_ajax():
		userid = request.POST.get('userid')
		password = request.POST.get('password')
		page = 'http://internal.passport.sohu.com/interface/authuser'
 		ct = long(time.time())
 		code = hashlib.md5(str(userid)+'1082'+'*G#Cr%0yQM3>n3[c<%qcZX8ZjcBHy+'+str(ct)).hexdigest()
 		params = '<?xml version="1.0" encoding="GBK"?><info><usertype>0</usertype><userid>'+userid+'</userid><appid>1082</appid><ct>'+str(ct)+'</ct><code>'+code+'</code><password>'+password+'</password><pwdtype></pwdtype></info>'
		headers = {'Content-Type' : 'application/xml'}
		req = urllib2.Request(page, params, headers)
		page = urllib2.urlopen(req)
		d = BeautifulSoup(page.read(),fromEncoding="gbk").findAll("status")[0].string
		if d == "0":
			if User.objects.filter(name=userid).count() == 0:
				p = User(name=userid,score=110,blackList=1,time=datetime.datetime(2010,1,1,1,1,1))
				p.save()
			request.session['member_id'] = userid
			return HttpResponse(json.dumps({"code":1,"userid":userid,"d":d,'score':getUserScore(userid),'index':getUserIndex(userid),'sign':getUserSign(userid)}))	
		elif d == "3":
			return HttpResponse(json.dumps({"code":0,"errortype":3}))
		else:
			return HttpResponse(json.dumps({"code":0,"errortype":4,"d":d,"params":params}))

def test(request):
	page = 'http://internal.passport.sohu.com/interface/authuser'
	ct = long(time.time())
	code = hashlib.md5('lidongtest@sohu.com'+'1082'+'*G#Cr%0yQM3>n3[c<%qcZX8ZjcBHy+'+str(ct)).hexdigest()
	params = '<?xml version="1.0" encoding="GBK"?><info><usertype>0</usertype><userid>lidongtest@sohu.com</userid><appid>1082</appid><ct>'+str(ct)+'</ct><code>'+code+'</code><password>lidong</password><pwdtype></pwdtype></info>'
	headers = {'Content-Type' : 'application/xml'}
	req = urllib2.Request(page, params, headers)
	page = urllib2.urlopen(req)
	return HttpResponse(BeautifulSoup(page.read(),fromEncoding="gbk").findAll("status")[0].string == "0")

def getUserIndex(userid):
	data = User.objects.all().order_by('-score')
	i = 0
	for item in data:
		i += 1
		if item.name == userid:
			index = i
			break
	return i

def getUserScore(userid):
	ob = User.objects.get(name=userid)
	score = ob.score
	return score

def getUserSign(userid):
	ob = User.objects.get(name=userid)
	time = (ob.time+datetime.timedelta(hours=8)).strftime("%Y-%m-%d")
	now = datetime.datetime.now().strftime("%Y-%m-%d")
	return (time == now)

def logout(request):
	if request.is_ajax():
		del request.session['member_id']
		return HttpResponse('1')

def sign(request):
	if request.is_ajax():
		userid = request.POST.get('userid')
		ob = User.objects.get(name=userid)
		score = ob.score
		time = (ob.time+datetime.timedelta(hours=8)).strftime("%Y-%m-%d")
		now = datetime.datetime.now().strftime("%Y-%m-%d")
		if(time == now):
			return HttpResponse(json.dumps({"code":0}))
		else:
			User.objects.filter(name=userid).update(time=datetime.datetime.now(),score=score+5)
			return HttpResponse(json.dumps({"code":1,"score":score+5}))

def submit(request):
	if request.is_ajax():
		userid = request.POST.get('userid')
		races = request.POST.get('races')
		score = request.POST.get('score')
		driver = request.POST.get('driver')
		races_db = races_list[int(races) - 1]
		rate = Driver.objects.get(id=driver).rate
		tscore = User.objects.get(name=userid).score
		if(float(tscore)-float(score) < 0):
		    return HttpResponse(json.dumps({"code":0}))
		p = races_db(userid=userid,rate=rate,score=score,totalScore=float(rate)*float(score),driverid=driver,time=datetime.datetime.now(),leftScore=float(tscore)-float(score),driverName=Driver.objects.get(id=driver).cname,raceName=Races.objects.get(id=races).name)
		p.save()
		User.objects.filter(name=userid).update(score=float(tscore)-float(score))
		return HttpResponse(json.dumps({"code":1,"score":float(tscore)-float(score)}))

def root(request):	
	return render_to_response('root.html',{'data':Driver.objects.all()})

def setContent(request):
	if request.is_ajax():
		data = request.POST.get('data')
		Content.objects.filter(id=1).update(rule=data)
		return HttpResponse("1")

def setContact(request):
	if request.is_ajax():
		data = request.POST.get('data')
		Content.objects.filter(id=1).update(contact=data)
		return HttpResponse("1")

def setResult(request):
	if request.is_ajax():
		raceid = request.POST.get('raceid')
		chamid = request.POST.get('chamid')
		chamname = request.POST.get('chamname')
		Races.objects.filter(id=raceid).update(finish=0,champion=chamid,championName=chamname)
		result_db = result_list[int(raceid)-1]
		if len(result_db.objects.all()) > 0:
			return HttpResponse("0")
		races_db = races_list[int(raceid)-1]
		ob = races_db.objects.filter(driverid=chamid).order_by('userid')
		lenth = len(ob)
		m = 1
		for i in range(0,lenth):
			if i == 0:
				p = result_db(userid=ob[i].userid,score=ob[i].score,totalScore=ob[i].totalScore,time=ob[i].time)
				p.save()
			else:
				if(ob[i].userid == ob[i-1].userid):
					a = result_db.objects.get(id=m)
					result_db.objects.filter(id=m).update(score=a.score+ob[i].score,totalScore=a.totalScore+ob[i].totalScore)
				else:
					p = result_db(userid=ob[i].userid,score=ob[i].score,totalScore=ob[i].totalScore)
					p.save()
					m += 1
		c = result_db.objects.all()
		for i in range(0,len(c)):
			b = User.objects.get(name=c[i].userid)
			User.objects.filter(name=c[i].userid).update(score=b.score+c[i].totalScore)
		return HttpResponse("1")

def history(request):
	userid = request.session['member_id']
	user = {'islogin':True,'userid':userid,'score':getUserScore(userid),'index':getUserIndex(userid),'sign':getUserSign(userid)}
	content = Content.objects.get(id=1)
	a = []
	for i in range(0,19):
		a += races_list[i].objects.filter(userid=userid).order_by('time')
	return render_to_response('index.html',{'status':5,'user':user,'content':content,'race_id':0,'data':a})

def findHistory(request):
	if request.is_ajax():
		userid = request.POST.get("name")
	        a = ''
		for i in range(0,19):
                	b = races_list[i].objects.filter(userid=userid).order_by('time')
			for n in b:
			    a += '<tr>'
			    a += '<td>'+n.time.strftime("%Y-%m-%d %H:%M") +'</td>'
			    a += '<td>'+str(i+1)+'</td>'
			    a += '<td>'+n.driverName+'</td>'
			    a += '<td>'+str(n.score)+'</td>'
			    a += '<td>'+str(n.rate)+'</td>'
			    a += '<td>'+str(n.leftScore)+'</td>'
			    try:
			    	c = result_list[i].objects.get(userid=userid)
			    except result_list[i].DoesNotExist:
				a += '<td>0</td>'
			    else:
			    	a += '<td>'+str(c.totalScore)+'</td>'
			    a += '</tr>'
		return HttpResponse(a)

def change(request):
	if request.is_ajax():
		userid = request.session['member_id']
		ob = User.objects.get(name=userid)
		return HttpResponse(json.dumps({"name":ob.rname,"phone":ob.phone,"address":ob.address,"code":ob.code}))

def changeSave(request):
	if request.is_ajax():
		userid = request.session['member_id']
		rname = request.POST.get('name')
		phone = request.POST.get('phone')
		address = request.POST.get('address')
		code = request.POST.get('code')
		User.objects.filter(name=userid).update(rname=rname,phone=phone,address=address,code=code)
		return HttpResponse("1")


def findUser(request):
	if request.is_ajax():
		userid = request.POST.get('data')
		ob = User.objects.get(name=userid)
		return HttpResponse(json.dumps({"name":ob.rname,"phone":ob.phone,"address":ob.address,"code":ob.code}))




