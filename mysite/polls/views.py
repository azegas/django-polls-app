from django.shortcuts import render, HttpResponse
from django.http import Http404

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        # try to fetch a question from db with an id of question_id(we inputted in url)
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        # raise http404 error if it does not exist
        raise Http404("Question does not exist")
    # if the question is found, pass question content to the template
    # in template we will display this question content with {{ question }}
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)