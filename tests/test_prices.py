#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_data.prices import USE_CASES, REPLY_TIMEOUT

from operational.simulator_tester import batch, exchange_sim


def test_exchange_sim_int_zero_price(exchange_sim):
    batch("INTEGER_ZERO_PRICE", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_int_price(exchange_sim):
    batch("INTEGER_PRICE", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_float_non_pos_price(exchange_sim):
    batch("FLOAT_NON_POSITIVE_PRICE", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_too_high_price(exchange_sim):
    batch("TOO_HIGH_PRICES", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_hires_price(exchange_sim):
    batch("FLOAT_HIRES_PRICE", USE_CASES, REPLY_TIMEOUT, *exchange_sim)
