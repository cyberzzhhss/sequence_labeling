import sys
def check_first_word(i, tokens):
    if i < 1:
        return False
    line = tokens[i - 1].strip()
    if len(line) == 0:
        return True
    return False

def check_last_word(i, tokens):
    if i > len(tokens) - 2:
        return False
    line = tokens[i + 1].strip()
    if len(line) == 0:
        return True
    return False

def get_prev_word(i, tokens):
    if check_first_word(i, tokens):
        return '<s>' # BEGIN-OF-SENTENCE
    elif i < 1:
        return '<s>'
    else:
        return tokens[i - 1].strip().split()[0]

def get_prev_pos(i, tokens):
    if check_first_word(i, tokens):
        return '<s>' # BEGIN-OF-SENTENCE
    elif i < 1:
        return '<s>'
    else:
        return tokens[i - 1].strip().split()[1]

def get_next_word(i, tokens):
    if check_last_word(i, tokens):
        return '</s>' # END-OF-SENTENCE
    elif i > len(tokens) - 2:
        return '</s>'
    else:
        return tokens[i + 1].strip().split()[0]

def get_next_pos(i, tokens):
    if check_last_word(i, tokens):
        return '</s>' # END-OF-SENTENCE
    elif i > len(tokens) - 2:
        return '</s>'
    else:
        return tokens[i + 1].strip().split()[1]

def check_cap_word(i, tokens):
    word = tokens[i].strip().split()[0]
    if word[0].isupper():
        return '1'
    else:
        return '0'

def check_prev_cap_word(i, tokens):
    if check_first_word(i, tokens):
        return '0'
    if i < 1:
        return '0'
    else:
        word = tokens[i - 1].strip().split()[0]
        if word[0].isupper():  
            return '1'
        else:
            return '0'

def check_next_cap_word(i, tokens):
    if check_last_word(i, tokens):
        return '0'
    elif i > len(tokens) - 2:
        return '0'
    else:
        word = tokens[i + 1].strip().split()[0]
        if word[0].isupper():
            return '1'
        else:
            return '0'


with open(sys.argv[1] ,'r') as f:
    with open('training.feature', 'w') as f2:
        tokens = f.readlines()
        for i, line in enumerate(tokens):
            line = line.strip()
            if len(line) == 0:
                f2.write('\n')
            else:
                cur_word, cur_pos, cur_bio = line.split()
                cur_cap    = 'cur_cap='   + check_cap_word(i, tokens)

                prev_word  = 'prev_word=' + get_prev_word(i, tokens)
                prev_pos   = 'prev_pos='  + get_prev_pos(i, tokens)
                prev_cap   = 'prev_cap='  + check_prev_cap_word(i, tokens)

                next_word  = 'next_word=' + get_next_word(i, tokens)
                next_pos   = 'next_pos='  + get_next_pos(i, tokens)
                next_cap   = 'next_cap='  + check_next_cap_word(i, tokens)

                pp_word = 'pp_word=' + get_prev_word(i - 1, tokens)
                pp_pos  = 'pp_pos='  + get_prev_pos(i - 1, tokens)
                pp_cap  = 'pp_cap='  + check_prev_cap_word(i - 1, tokens)

                nn_word = 'nn_word=' + get_next_word(i + 1, tokens)
                nn_pos  = 'nn_pos='  + get_next_pos(i + 1, tokens)
                nn_cap  = 'nn_cap='  + check_next_cap_word(i + 1, tokens)

                line = '\t'.join([cur_word, cur_pos, cur_cap, prev_word, \
                                  prev_pos, prev_cap, next_word, next_pos, \
                                  next_cap, pp_word, pp_pos, pp_cap, nn_word,\
                                  nn_pos, nn_cap, cur_bio])
                f2.write(line + '\n')

with open(sys.argv[2], 'r') as f:
    with open('test.feature', 'w') as f2:
        tokens = f.readlines()
        for i, line in enumerate(tokens):
            line = line.strip()
            if len(line) == 0:
                f2.write('\n')
            else:
                cur_word, cur_pos = line.split()
                cur_bio   = 'cur_bio=##'
                cur_cap   = 'cur_cap='     + check_cap_word(i, tokens)

                next_word = 'next_word='   + get_next_word(i, tokens)
                next_pos  = 'next_pos='    + get_next_pos(i, tokens)
                prev_word = 'prev_word='   + get_prev_word(i, tokens)
                prev_pos  = 'prev_pos='    + get_prev_pos(i, tokens)
                prev_cap  = 'prev_cap='    + check_prev_cap_word(i, tokens)
                next_cap  = 'next_cap='    + check_next_cap_word(i, tokens)

                pp_word = 'pp_word=' + get_prev_word(i - 1, tokens)
                pp_pos  = 'pp_pos='  + get_prev_pos(i - 1, tokens)
                pp_cap  = 'pp_cap='  + check_prev_cap_word(i - 1, tokens)

                nn_word = 'nn_word=' + get_next_word(i + 1, tokens)
                nn_pos  = 'nn_pos='  + get_next_pos(i + 1, tokens)
                nn_cap  = 'nn_cap='  + check_next_cap_word(i + 1, tokens)

                line = '\t'.join([cur_word, cur_pos, cur_cap, prev_word, \
                                  prev_pos, prev_cap, next_word, next_pos, \
                                  next_cap, pp_word, pp_pos, pp_cap, nn_word,\
                                  nn_pos, nn_cap, cur_bio])
                f2.write(line + '\n')