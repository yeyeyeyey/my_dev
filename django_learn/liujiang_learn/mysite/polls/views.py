from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.http import Http404
from .forms import UploanFileForm
import csv

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
# def index(request):
#     return HttpResponse('hello ,this is a poll')
# class IndexView(generic,Lis)
def detail(request,question_id):
    # return HttpResponse('You are looking at question %s.'%question_id)
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404("question does not exist")
    # return render(request,'polls/detail.html',{'question':question})
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    response = "you are looking at the results of question %s"
    return HttpResponse(response %question_id)

def vote(request,question_id):
    # return HttpResponse("you are voting on question %s"%question_id)
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError,Choice.DoesNoeExit):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':'You donot select a choice',
        })
    else:
        selected_choice.votes +=1
        selected_choice.sace()
        return HttpResponseRedirect(reverse('polls:results',args=(
            question.id,)))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    output = ','.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request,'polls/index.html',context)

# def bad_request(request):
#     return render(request,'400.html')
#
# def permission_denied(request):
#     return render(request, '403.html')
#
#
# def page_not_found(request):
#     return render(request, '404.html')
#
#
# def error(request):
#     return render(request, '500.html')

def uploan_file(request):
    if request.mothod =='POST':
        form = UploanFileForm(request.POST,request.FILES)
        if form.is_valid():
            pass

def some(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment';
    writer = csv.writer(response)
    writer.writerow(['first row','a','b','c'])
    writer.writerow(['second row','1','2','3'])
    return response