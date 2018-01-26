# -*- coding: utf-8 -*-

REPLY_TIMEOUT = 0.1

# These are dirty data tests. Well-formed data pass through the matching and other tests.

USE_CASES = {

    "ABSENT_SYMBOL" : [
        ['|BUY|10.0|10', None, '!'],
    ],

    "INVALID_CHARS" : [
        ['A=B|BUY|10.0|10', None, '!'],
        ['C D|BUY|-10.0|10', None, '!'],
        ['A=B|SELL|10.0|10', None, '!'],
        ['C D:>|SELL|-10.0|10', None, '!'],
    ],

    "LONG_SYMBOL" : [
        ['JUNKBUTAVERYLONGONE|SELL|10.00|100', None, '!'],
        ['EIGHTCHR|SELL|10.00|100', None, '!'],
        ['FIFTEENCHARACTR|SELL|10.00|100', None, '!'],
    ],

    "LOWER_CASE" : [
        ['ibm|SELL|10.00|100', None, '!'],
        ['a|SELL|10.00|100', None, '!'],
        ['msft|SELL|10.00|100', None, '!'],
    ],

    "UNICODE" : [
        ['ЖДЛО|SELL|10.00|100', None, '!'],
        ['ЙЦУКЕ|BUY|10.00|100', None, '!'],
        ['ждло|SELL|10.00|100', None, '!'],
        ['йцуке|BUY|10.00|100', None, '!'],
    ],
}
