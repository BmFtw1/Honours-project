import random
import unittest
from unittest import mock
from unittest import TestCase
import SystemDirected

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


def greetings_test(sentence):
    assert SystemDirected.greeting(sentence) in GREETING_RESPONSES


class CreateTests(TestCase):
    sentence = random.choice(GREETING_INPUTS)

