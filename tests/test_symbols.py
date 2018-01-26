#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_data.symbols import USE_CASES, REPLY_TIMEOUT

from operational.simulator_tester import batch, exchange_sim


def test_exchange_sim_absent_symbol(exchange_sim):
    batch("ABSENT_SYMBOL", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_invalid_chars(exchange_sim):
    batch("INVALID_CHARS", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_long_symbol(exchange_sim):
    batch("LONG_SYMBOL", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_lower_case(exchange_sim):
    batch("LOWER_CASE", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_unicode(exchange_sim):
    batch("UNICODE", USE_CASES, REPLY_TIMEOUT, *exchange_sim)
