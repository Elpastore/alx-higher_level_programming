#!/usr/bin/python3
def multiple_returns(sentence):

    len_tuple = len(sentence)

    return (len_tuple, sentence[0] if len_tuple > 0 else None)
