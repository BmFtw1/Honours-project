import random
import pytest

from app import SystemDirected
from app.SystemDirected import greeting

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


def test_greetings():
    assert SystemDirected.greeting("hello") in GREETING_RESPONSES


def test_lemnormalise():
    assert SystemDirected.LemNormalise("The striped bats are hanging on their feet for best") == ['the', 'striped',
                                                                                                  'bat', 'are',
                                                                                                  'hanging', 'on',
                                                                                                  'their', 'foot',
                                                                                                  'for', 'best']


def test_response_0():
    assert SystemDirected.response("asdasdasd") == "I am sorry! I don't understand you"


def test_response_1():
    assert (SystemDirected.response("What is a chatbot")) == ('design\n'
                                                              'the chatbot design is the process that defines the interaction between the '
                                                              'user and the chatbot.the chatbot designer will define the chatbot '
                                                              'personality, the questions that will be asked to the users, and the overall '
                                                              'interaction.it can be viewed as a subset of the conversational design.')
