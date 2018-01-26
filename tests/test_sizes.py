#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_data.sizes import USE_CASES, REPLY_TIMEOUT

from operational.simulator_tester import batch, exchange_sim


def test_exchange_sim_float_size(exchange_sim):
    batch("FLOATING_SIZE", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_negative_size(exchange_sim):
    batch("NEGATIVE_SIZE", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_extreme_size(exchange_sim):
    batch("EXTREME_SIZES", USE_CASES, REPLY_TIMEOUT, *exchange_sim)

