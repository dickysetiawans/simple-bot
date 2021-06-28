import re
import long_responses as longg


def message_probability(user_message, recognised_word, singel_response=False, required_words=[]):
    message_certainty = 0
    has_required_word = True

    for word in user_message:
        if word in recognised_word:
            message_certainty += 1
    percentage = float(message_certainty) / float(len(recognised_word))

    for word in recognised_word:
        if word not in user_message:
            has_required_word = False
            break

    if has_required_word or singel_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def resposnse(bot_response, list_of_word, singel_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_word, required_words)

        # Response----------------------------------------------------
    resposnse('Hello',['hello,','hi','hey', 'bro', 'heyo'], singel_response=True)
    resposnse('You can call me kyBot', ['what', 'your', 'name', 'bot'], required_words=['your', 'name'])
    resposnse('I\'m doing fine', ['how','doing'], required_words=['how'])
    resposnse('I\'m bot, no have age', ['how', 'old', 'age'], required_words=['old'])    
    resposnse('Thank you!, byee', ['i','love','palace', 'byee','see you'], required_words=['love', 'byee', 'see you'])

    # respon like
    resposnse(longg.EATING, ['Like', 'eat', 'food'], required_words=['like', 'eat', 'food'])
    #response have somthing
    resposnse(longg.HAVE, ['have'], required_words=['have'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    
    return longg.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s+', user_input.lower())
    resposnse = check_all_messages(split_message)
    return resposnse

print('kyBot: Hello, welcome guys!! english pleace :>')
# TESTING REPONSE SYTEM
run = True
while run:
    print('kyBot: ' + get_response(input('You: ')))