# import necessary libraries
import random
import string  # to process standard python strings
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings('ignore')
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('popular', quiet=True)  # for downloading packages

# uncomment the following on the first time running
# nltk.download('punkt') # first-time use only
# nltk.download('wordnet') # first-time use only

# with open("json") as file:
#     data = json.load(file)

# Reading in the corpus
with open('H:\Honours-project\chatbot.txt', 'r', encoding='utf8', errors='ignore') as fin:
    data = fin.read().lower()

mylistofwords = []

# TOkenisation
sent_tokens = nltk.sent_tokenize(data)  # converts to list of sentences

# Preprocessing
lemmer = WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


# return a list of lemmatized lower case words after removing punctuations
def LemNormalise(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


# Word matching for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    user_response = user_response.lower()
    bot_response = ''
    sent_tokens.append(user_response)
    # Create the TfidfVectorizer Object
    tfidfVec = TfidfVectorizer(tokenizer=LemNormalise, stop_words='english', analyzer='word')
    # Convert the list of sentences to a matrix of TF-IDF features
    tfidf = tfidfVec.fit_transform(sent_tokens)
    # grab the measurement of similarity (similarity scores)
    vals = cosine_similarity(tfidf[-1], tfidf)
    # Get the index of the most similar text/sentence to the users response
    idx = vals.argsort()[0][-2]
    # Reduce the dimensionality of vals into a 1d array
    flat = vals.flatten()
    # sort into ascending order
    flat.sort()
    # Get the most similar score to the users responsea
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        bot_response = bot_response + "I am sorry! I don't understand you"
        return bot_response
    else:
        bot_response = bot_response + sent_tokens[idx]
        return bot_response


flag = True
print("BOT: My name is bot. Hello there")
while flag:
    user_response = input()
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            flag = False
            print("BOT: You are welcome..")
        else:
            if greeting(user_response) is not None:
                print("BOT: " + greeting(user_response))
            else:
                print("BOT: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("BOT: Bye! take care..")
