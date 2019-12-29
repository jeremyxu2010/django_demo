# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from test_app.models import Question


def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'index.html', context)


def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    context = {'question': q}
    return render(request, 'detail.html', context)