# -*- coding: utf-8 -*-

REPLY_TIMEOUT = 0.1

# These are dirty data tests. Well-formed data pass through the matching and other tests.

USE_CASES = {

    "NO_SEPARATORS" : [
        ['AAABUY10.0010', None, '!'],
    ],

    "CHARS_IN_PRICE" : [
        ['A|BUY|1O.0|10', None, '!'],
        ['A|SELL|10.00-|10', None, '!'],
        ['A|SELL|10.00.|10', None, '!'],
        ['A|SELL|x10.00|10', None, '!'],
    ],

    "MISSIMG_FIELD" : [
        ['JUNK|SELL|10.00', None, '!'],
        ['HWP|SELL|10.15|', None, '!'],
    ],

    "WRONG_SIDES" : [
        ['A|sell|10.00|10', None, '!'],
        ['A|buy|10.00|10', None, '!'],
        ['A|SEL|10.00|10', None, '!'],
        ['A|8UY|10.00|10', None, '!'],
    ],

    "EXTRA_FIELDS" : [
        ['OMC|BUY|10.00|100|', None, '!'],
        ['OMC|BUY|10.00|100|comment|', None, '!'],
        ['OMC|SE|LL|10.00|10', None, '!'],
    ],

    "EXTRA_PADDING" : [
        ['ZVZZT |SELL|10.00|10', None, '!'],
        ['ZVZZT| BUY |10.00|10', None, '!'],
        ['ZVZZT|SELL| 10.00|10', None, '!'],
        ['ZVZZT|BUY|10.00| 10', None, '!'],
    ],
}
