import random
import sys

def process_line(line):
    '''
    Process a line of text to extract (state, new_word) pairs.
    Note that we remove uppercase letters in this example, though
    you don't have to.

    Example:
    process_line("In winter I get up at night") =
    [('BEGIN', 'in'),
     ('in', 'winter'),
     ('winter', 'i'),
     ('i', 'get'),
     ('get', 'up'),
     ('up', 'at'),
     ('at', 'night'),
     ('night', 'END')]

    We add the BEGIN and END keywords so that we can initialize the
    sentence and know when the line ends.
    '''

    # YOUR CODE HERE #

    pass

def process_textfile(filename):
    '''
    Creates a dictionary with transition pairs
    based on a file provided

    For the first part of the assignment, we use a
    placeholder text that you will have to replace
    at some point.

    Based on the placeholder text, the dictionary
    should contain the following key-value pairs:

    'blue,': ['END']
    'by': ['yellow', 'day.', 'day?']
    'still': ['hopping', 'going']
    '''
    d = {}

    # Placeholder until we add File I/O in part two
    # Overwrite the following lines with your code:
    f = '''In winter I get up at night
And dress by yellow candle-light.
In summer quite the other way,
I have to go to bed by day.

I have to go to bed and see
The birds still hopping on the tree,
Or hear the grown-up people's feet
Still going past me in the street.

And does it not seem hard to you,
When all the sky is clear and blue,
And I should like so much to play,
To have to go to bed by day?
'''.split('\n')
    # text from http://www.bygosh.com/Features/082000/rhymes.htm

    # YOUR CODE HERE #

    return d

def generate_line(d):
    '''
    Generates a random sentence based on the dictionary
    with transition pairs

    Note that the first state is BEGIN but that we
    obviously do not want to return BEGIN

    Some sample output based on the placeholder text:
    'i have to go to go to go to go to play,'

    Hint: use random.choice to select a random element from a list
    '''

    # YOUR CODE HERE #

    pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('ERROR: Run as python markov.py <filename>')
        exit()

    d = process_textfile(sys.argv[1])
    print(generate_line(d))
