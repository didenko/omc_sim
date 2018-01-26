#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_data.fields import USE_CASES, REPLY_TIMEOUT

from operational.simulator_tester import batch, exchange_sim


def test_exchange_sim_no_sep(exchange_sim):
    batch("NO_SEPARATORS", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_chars_in_price(exchange_sim):
    batch("CHARS_IN_PRICE", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_missing_field(exchange_sim):
    batch("MISSIMG_FIELD", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_wrong_sides(exchange_sim):
    batch("WRONG_SIDES", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_extra_fields(exchange_sim):
    batch("EXTRA_FIELDS", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_extra_padding(exchange_sim):
    batch("EXTRA_PADDING", USE_CASES, REPLY_TIMEOUT, *exchange_sim)
