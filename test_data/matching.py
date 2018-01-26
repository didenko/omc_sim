# -*- coding: utf-8 -*-

REPLY_TIMEOUT = 0.1

USE_CASES = {

    "MATCH" : [
        ['AAPL|BUY|500.00|100', None, None],
        ['AAPL|SELL|500.00|100', 'AAPL|500.00|100', None],
        ['AAPL|SELL|500.00|100', None, None],
        ['AAPL|BUY|500.00|90', 'AAPL|500.00|90', None],
        ['AAPL|BUY|500.00|10', 'AAPL|500.00|10', None],
    ],

    "JUNK_STOCK" : [
        ['JUNK|BUY|0.02|100', None, None],
        ['JUNK|SELL|0.01|100', 'JUNK|0.02|100', None],
    ],

    "CROSS_NARROW" : [
        ['TSLA|BUY|337.64|100', None, None],
        ['TSLA|SELL|337.63|100', 'TSLA|337.64|100', None],
    ],

    "CROSS_WIDE" : [
        ['AAPL|BUY|500.00|100', None, None],
        ['AAPL|SELL|400.00|100', 'AAPL|500.00|100', None],
    ],

    "EXAMPLE" : [
        ['IBM|SELL|145.09|100', None, None],
        ['IBM|BUY|145.08|200', None, None],
        ['IBM|BUY|145.09|200', 'IBM|145.09|100', None],
        ['IBM|SELL|145.09|100', 'IBM|145.09|100', None],
    ],

    "PARTIALS" : [
        ['ZVZZT|SELL|200.00|100', None, None],
        ['ZVZZT|BUY|200.01|200', 'ZVZZT|200.00|100', None],
        ['ZVZZT|SELL|2000.00|100', 'ZVZZT|200.01|100', None],
    ],
}
