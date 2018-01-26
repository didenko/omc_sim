# -*- coding: utf-8 -*-

REPLY_TIMEOUT = 0.1

# These are dirty data tests. Well-formed data pass through the matching and other tests.

USE_CASES = {

    "INTEGER_ZERO_PRICE" : [
        ['AAA|BUY|0|10', None, '!'],
    ],

    "INTEGER_PRICE" : [
        ['A|BUY|10|10', None, '!'],
        ['A|BUY|-10|10', None, '!'],
    ],

    "FLOAT_NON_POSITIVE_PRICE" : [
        ['JUNK|SELL|0.00|100', None, '!'],
        ['BBBB|SELL|-1.15|100', None, '!'],
    ],

    "FLOAT_HIRES_PRICE" : [
        ['BBBB|SELL|1.175494e-38|100', None, '!'],
        ['BBBB|SELL|1.175494|100', None, '!'],
        ['BBBB|SELL|.17549456|100', None, '!'],
    ],

    "TOO_HIGH_PRICES" : [
        ['OMC|SELL|18446744073709551615|100', None, '!'],
        ['OMC|BUY|184467440737095516.15|100', None, '!'],
    ],
}
