from django.shortcuts import render

from .forms import CreatePollForm
from .models import Poll, PollsQuestion, PollsAnswers


def home(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'polls/home.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    questions = PollsQuestion.objects.filter(poll_id_id=poll_id)
    context = {
        'poll': poll,
        'questions': questions,
    }
    return render(request, 'polls/vote.html', context)


def vote_detail(request, vote_id):
    question = PollsQuestion.objects.get(pk=vote_id)
    answers = PollsAnswers.objects.filter(question_id_id=vote_id)
    context = {
        'question': question,
        'answers': answers,
    }
    return render(request, 'polls/vote_detail.html', context)


def results(request, poll_id):
    context = {}
    return render(request, 'polls/results.html', context)


# def create(request):
#     form = CreatePollForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'polls/create.html', context)
