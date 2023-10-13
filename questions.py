import json
import random

f = open('questions.json')

questions_dict = json.load(f)
all_the_questions = list(questions_dict["questions_list"])


""" Fetch a random question array from the data  
    and return it """

# TODO - need to make this better
def getRandomQuestion(questions_list):
    random_num = random.randint(0, 13) 
    question_obj = questions_list[random_num]
    return question_obj


""" Plug the information from the random question array into
    the html and return it """


def printQuestion():
    # get random question
    random_question = getRandomQuestion(all_the_questions)

    return random_question


f.close()
