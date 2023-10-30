from django.shortcuts import render
from chatapp.models import Qna
#author roman
# Create your views here.


def chat(request):
	return render(request, 'chat.html')

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




'''
def chat(request):
	if request.method == 'POST':
		message = request.POST['message'] #message type str
		#print(type(msg)) #str
		questi = "This is default question"
		question = message 
		allqna = Qna.objects.all()
		qlist=[]
		pklist =[]
		for o in allqna:
			qlist.append(o.question)
			pklist.append(o.id)

'''