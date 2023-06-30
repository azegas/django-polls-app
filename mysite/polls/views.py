from django.shortcuts import render, HttpResponse

# Create your views here.


# first the user is going to http://127.0.0.1:8000/polls/99/ for example in the browser
# since he asks to go to polls/ it gets redirected to polls.urls
# when we are in polls.urls we see that there is <int:question_id> goes right after polls/
# user has specified that 99 is the <int:question_id>
# since there is nothing else after <int:question_id> , it means that urls will redirect us to views.detail view
# detail view as you can see here TAKES request and question_id(we got it from user - > urls -> views)
# now we just render the page with some text and question_id at the back
# In this specific example, %s is used as a placeholder for the question_id variable. 
# When the string response is formatted using the % operator, the %s is replaced with the value of question_id.

def index(request):
    return HttpResponse("Hello world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)