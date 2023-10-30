from django.shortcuts import render ,HttpResponse , redirect
import requests
from django.http import HttpResponse
from message.models import Contact ,qnat
#from message.forms import MessageForm,GMessageForm,ContactForm,GContactForm

# Create your views here.





def signIn(request):
	
	return render(request,'login.html')


def llm(request):
	
	return render(request,'llm.html')

def addqna(request):
	if request.method == 'POST':
		question= request.POST['question']
		answer= request.POST['answer']
		qnav = qnat.objects.create(question=question , answer=answer)
		context = {'message': 'Question  answer saved' }
		return render(request,'addqna.html',context)
	else:
		return render(request,'addqna.html')


def qna(request):
	allqna = qnat.objects.all()
	context ={'allqna': allqna}
	
	return render(request,'qna.html',context)

def facebook(request):
	
	return render(request,'facebook.html')




def tst(request):
	allqna = qnat.objects.all()
	qlist= []
	pklist=[]
	for ob in allqna:
		qlist.append(ob.question)
		pklist.append(ob.id)

	import requests

	API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
	headers = {"Authorization": "Bearer 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"}
	ques = "That is a happy person"
	payload = {
		"inputs": {
			"source_sentence": ques,
			"sentences": qlist
		},
	}


	response = requests.post(API_URL, headers=headers, json=payload)
	#str(print(response.json()))
	print(response.json())	


def chat(request):
	if request.method == 'POST':
		msg= request.POST['message']
		#print(type(msg)) #str
		ques = "That is a happy person"
		ques = msg
		allqna = qnat.objects.all()
		qlist= []
		pklist=[]
		for ob in allqna:
			qlist.append(ob.question)
			pklist.append(ob.id)

		import requests
		API_URL = "https://api-inference.huggingface.co/models/l3cube-pune/bengali-sentence-similarity-sbert"
		headers = {"Authorization": "Bearer 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"}
		
		payload = {
			"inputs": {
				"source_sentence": ques,
				"sentences": qlist
			},
		}


		response = requests.post(API_URL, headers=headers, json=payload)
		#str(print(response.json()))
		print(response.json())	
		zz= response.json()
		lvalue= zz[0]
		lindex=0

		for index , val in enumerate(zz):
		  if val > lvalue:
		    lvalue=val
		    lindex=index


		print(lvalue)
		print(lindex)

		modelpk=str(pklist[lindex])
		objbypk= qnat.objects.get(pk=modelpk)
		ansfromdb= objbypk.answer




		context = {'message': ansfromdb}
		#contact = Contact.objects.create(question=msg)
		return render(request,'chat.html',context)
	else:
		return render(request,'chat.html')



'''
def chat(request):
	if request.method == 'POST':
		msg= request.POST['message']
		#print(type(msg)) #str
		context = {'message': msg }
		#contact = Contact.objects.create(question=msg)
		return render(request,'chat.html',context)
	else:
		return render(request,'chat.html')



def message(request):
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = MessageForm(request.POST)		
	
	return render(request,'message.html',{'form':form})

def gmessage(request):
	if request.method == 'POST':
		form = GMessageForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = GMessageForm(request.POST)
	
	return render(request,'gmessage.html',{'form':form})



def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = ContactForm(request.POST)
	
	return render(request,'contact.html',{'form':form})


def gcontact(request):
	if request.method == 'POST':
		form = GContactForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = GContactForm(request.POST)
	
	return render(request,'gcontact.html',{'form':form})


def fromExcel(request):
	
	return render(request,'fromexcel.html')



def reports(request):
	
	return render(request,'reports.html')







#create contact
def createcontact(request):
	pass




def sendSMS():
	api_key =0
	msg=0
	num=0
	url=f'https:api.sms.net.bd/sendsms?api_key={api_key}&msg={msg}&to={num}'
	success_msg='<h2> Your message was send </h2>'
	return HttpResponse(sucess_msg)


'''  
