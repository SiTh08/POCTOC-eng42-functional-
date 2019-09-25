from pop_toc_functions import *

# we will need to import our functions

# Play the game and while loop here.
user_input = ' '
while user_input != 'p':
    user_input = int(input('SHOW ME WHAT YOU GOT (in integer)').strip())
    if div3(user_input) and div5(user_input):
        print('POPTOC')
    elif div5(user_input):
        print('TOC')
    elif div3(user_input):
        print('POP')
    else:
        print(user_input)