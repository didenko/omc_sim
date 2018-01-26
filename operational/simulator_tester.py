# -*- coding: utf-8 -*-

"""Tests for `exchange_sim` package."""

import pytest

from functools import wraps
from Queue import Queue, Empty
from subprocess import Popen, PIPE

from operational.line_reader import LineReader


@pytest.fixture
def exchange_sim():
    """Instantiate the exchange simulator runner"""

    proc = Popen('./bin/exchange-sim', stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=1)

    q_out = Queue()
    q_err = Queue()

    LineReader(proc.stdout, q_out).start()
    LineReader(proc.stderr, q_err).start()

    return proc, q_out, q_err


def check_process(func):

    @wraps(func)
    def wrapper(name, use_cases, timeout, proc, matches, errors):
        __tracebackhide__ = True
        try:
            return func(name, use_cases, timeout, proc, matches, errors)

        except IOError as e:
            pytest.fail("can not communicate with the exchange simulator")

        finally:
            exit_code = proc.poll()
            if exit_code is None:
                proc.terminate()
            elif exit_code < 0:
                pytest.fail("exchange simulator terminated by signal %d" % -exit_code)
            elif exit_code > 0:
                pytest.fail("exchange simulator errored with code %d" % exit_code)

    return wrapper


@check_process
def batch(name, use_cases, timeout, proc, matches, errors):
    __tracebackhide__ = True

    for idx, (order, trade, err) in enumerate(use_cases[name]):

        proc.stdin.write(order + '\n')

        if trade:
            match_expect(idx, name, trade, matches, timeout)
        else:
            match_none(idx, name, matches, timeout)

        if err:
            err_expect(idx, name, err, errors, timeout)
        else:
            err_none(idx, name, errors, timeout)


def match_expect(idx, uc_name, hope, src, timeout):
    try:
        trade = src.get(True, timeout).strip()
        if trade != hope:
            pytest.fail(
                "Case %s index %d:\nExpected trade: %s\nReceived trade: %s"
                % (uc_name, idx, hope, trade))
    except Empty:
        pytest.fail("Case %s index %d: missing trade %s" % (uc_name, idx, hope))


def match_none(idx, uc_name, src, timeout):
    try:
        trade = src.get(True, timeout).strip()
        pytest.fail("Case %s index %d: unexpected trade %s" % (uc_name, idx, trade))
    except Empty:
        pass


def err_expect(idx, uc_name, err, src, timeout):
    try:
        src.get(True, timeout)
        # Detection should go here once we know potential errors
    except Empty:
        pytest.fail("Case %s index %d: missing error %s" % (uc_name, idx, err))


def err_none(idx, uc_name, src, timeout):
    try:
        complaint = src.get(True, timeout).strip()
        pytest.fail("Case %s index %d: unexpected error %s" % (uc_name, idx, complaint))
    except Empty:
        pass
