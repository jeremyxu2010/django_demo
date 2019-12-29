import unittest
from datetime import datetime

from django.utils import timezone

# noinspection PyUnresolvedReferences
import test_app.django_setup
from test_app.models import Question


class TestModelsCase(unittest.TestCase):
    def test_question_model(self):
        q = Question.objects.create(question_text="xxxx", pub_date=timezone.now())
        q2 = Question.objects.get(pk=q.id)
        self.assertIsInstance(q2, Question, "yyy")
        self.assertTrue(Question.is_valid_question(question_text="xxxx"), "xxxx")
        self.assertIsInstance(Question.get_pub_date(question_text="xxxx"), datetime)


if __name__ == '__main__':
    unittest.main()
