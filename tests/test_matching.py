#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_data.matching import USE_CASES, REPLY_TIMEOUT

from operational.simulator_tester import batch, exchange_sim


def test_exchange_sim_match(exchange_sim):
    batch("MATCH", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_cross_wide(exchange_sim):
    batch("CROSS_WIDE", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_cross_narrow(exchange_sim):
    batch("CROSS_NARROW", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_junk_stock(exchange_sim):
    batch("JUNK_STOCK", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_example(exchange_sim):
    batch("EXAMPLE", USE_CASES, REPLY_TIMEOUT, *exchange_sim)


def test_exchange_sim_partials(exchange_sim):
    batch("PARTIALS", USE_CASES, REPLY_TIMEOUT, *exchange_sim)
