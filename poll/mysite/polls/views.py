from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponse
from django.http import Http404

from .models import Question

def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : lastest_question_list}
    # output = ', '.join([q.question_text for q in lastest_question_list])
    # template = loader.get_template('polls/index.html')
    # return HttpReponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try: 
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question' : question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)