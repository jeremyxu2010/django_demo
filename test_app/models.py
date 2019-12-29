# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import namedtuple

from django.db import connection
from django.db import models
from django.utils import timezone


# Create your models here.


class Question(models.Model):
    question_text = models.CharField(name='question_text', verbose_name='question text', max_length=200, db_column='question_text')
    pub_date = models.DateTimeField(name='pub_date', verbose_name='date published', default=timezone.now, db_column='pub_date')

    class Meta:
        db_table = "question"

    @classmethod
    def is_valid_question(self, question_text):
        return len(Question.objects.filter(question_text=question_text)) > 0

    @classmethod
    def get_pub_date(self, question_text):
        with connection.cursor() as cursor:
            cursor.execute("SELECT pub_date FROM question WHERE question_text=%s", [question_text])
            results = Question.namedtuplefetchall(cursor)
        if results is not None and len(results) > 0:
            return results[0].pub_date
        return None

    @classmethod

    def namedtuplefetchall(self,  cursor):
        "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        db_table = "choice"
