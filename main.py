from random import randint
import copy

story = (
    'One day me and my friend {} decide to go to the {} game in {}. '+
    'WE really wanted to see the {} play the {}. '+
    'We, our {} our {} down to the {} and bought some {}s. '+
    'We got into the game and it was lot of fun. '+
    'We ate some {} {}and drint some {} {} '+
    'We had a great time and we plan to go their again next year.'
)

word_dict = {
    'adjective':['Srijan','Vishal','Aditya','Richy','harsh','Roy'],
    'city name':['Delhi','Mumbai','Agra','Chenni','Ayodha','JAipur','Bnaglore','Chandighar'],
    'noun':['people','dog','music','map','ball','hotdog','salad','sandwiche'],
    'action verb':['run','fall','crawl','scurry','cry','watch','bounce','jump'],
    'sports noun':['ball','mit','puck','uniform','helmet','scoreboard','player'],
    'place':['park','desert','store','restuarant','waterfall']
}

def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective',local_dict),
        get_word('sports noun',local_dict),
        get_word('city name',local_dict),
        get_word('noun',local_dict),
        get_word('noun',local_dict),
        get_word('action verb',local_dict),
        get_word('noun',local_dict),
        get_word('place',local_dict),
        get_word('noun',local_dict),
        get_word('adjective',local_dict),
        get_word('noun',local_dict),
        get_word('adjective',local_dict),
        get_word('noun',local_dict)
    )

print('STORY 1:')
print(create_story())
print()
print('STORY 2:')
print(create_story())
