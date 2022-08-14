#!/usr/bin/env python3

def first_with_given_key(iterable, key=lambda y: y):

    iter_keys = []

    for i in iterable:
        if key(i) not in iter_keys:
            iter_keys.append(key(i))
            yield i



