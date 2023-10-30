from django.shortcuts import render
from chatapp.models import Qna
#author roman
# Create your views here.


# chat(request):
	#return render(request, 'chat.html')

def qna(request):
	allqna =Qna.objects.all()
	context = {'allqna':allqna }
	return render(request, 'qna.html',context)

def addqnat(request):
	if request.method == 'POST':
		question = request.POST['question']
		answer = request.POST['answer']
		qnanew = Qna.objects.create(question=question,answer=answer)
		succes_msg = f'Saved : Qustion - {question} &  Answer- {answer}  '
		context = {'message': succes_msg}
		return render(request, 'addqna.html',context)
	else:
		return render(request, 'addqna.html')





def chat(request):
	if request.method == 'POST':
		message = request.POST['message'] #message type str
		#print(type(msg)) #str
		questi = "This is default question"
		questi = message 
		allqna = Qna.objects.all()
		qlist=[]
		pklist =[]
		for o in allqna:
			qlist.append(o.question)
			pklist.append(o.id)

		import requests

		API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
		headers = {"Authorization": "Bearer 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"}

		def query(payload):
			response = requests.post(API_URL, headers=headers, json=payload)
			return response.json()
		

		payload = {
			"inputs": {
				"source_sentence": questi,
				"sentences": qlist
			},}


		response = requests.post(API_URL, headers=headers, json=payload)
		#str(print(response.json()))
		rs = response.json()
		lar_value =rs [0]
		lar_index=0
		for index , val in enumerate(rs):
			if val >lar_value:
				lar_value=val
				lar_index=index

		modelpk=str(pklist[lar_index])
		objbypk= Qna.objects.get(pk=modelpk)
		ansfromdb = objbypk.answer		
		context = {'message': ansfromdb}
		return render(request , 'chat.html',context)
	else:
		return render(request , 'chat.html')	