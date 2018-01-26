# -*- coding: utf-8 -*-

REPLY_TIMEOUT = 0.1

# These are dirty data tests. Well-formed data pass through the matching and other tests.

USE_CASES = {

    "FLOATING_SIZE" : [
        ['ZVZZT|BUY|10.0|10.45', None, '!'],
    ],

    "NEGATIVE_SIZE" : [
        ['ZVZZT|BUY|10.0|-10.45', None, '!'],
        ['ZVZZT|SELL|10.0|-10.45', None, '!'],
    ],

    "EXTREME_SIZES" : [
        ['ZVZZT|BUY|10.0|18446744073709551615', None, '!'],
        ['ZVZZT|SELL|10.0|0', None, '!'],
    ],
}
