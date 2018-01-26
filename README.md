## Tested cases (from email):

 Done    | Test case description
---------|-----------------------
 &#9745; | code should fail on integer prices
 &#9745; | varying symbols
 &#9745; | overflows
 &#9745; | underflows
 &#9745; | long string sequences
 &#9745; | floating order size
 &#9745; | wrong field composition
 &#9745; | error output
 &#9745; | specific process termination
 &#9745; | crash exceptions
 &#9745; | detect errors and crashes as unexpected behavior
 &#9745; | detect errors as expected reaction to a wrong input

## Structure:

* `bin` directory has the `exchange_sim` executable
* `tests` directory has the test invocations
* `test_data` directory has the relevant invocations
* `operational` directory has the test logic in it

The test data in `test_data` directory comtains grouped interaction scripts, where fields are (all required):

Field     | Description
----------|----------
Order     | *string*
Execution | *string* if expected, `None` if not
Error     | *string* if expected, `None` if not

The test logic is as following:

Test invocations start the `./bin/exchange_sim` process usin the `exchange_sim` test fixture. The fixture also starts two background threads which transfer the `exchange_sim` output to buffered queues.

After that the invocations feedthe use cases into the `batch` processor, which is decorated with the `check_process` function. The `check_process` function is responsible for all process-related issues, like IOErrors, crashes, and final cleanup (partially).

The `batch` function feeds the orders to simulator via `stdin` and after each order checks an expected outcome - both in trades and error feeds.

As errors were not specified in the spec, the tests only check for a presence of an error. Later error detection can be improved, including pattern matching.

Other improvements may be to merge test invocations in one method - currently not done as *pytest* Does not have a "mark failed and continue" behavior, which means that the batch of tests will stop after the first failure.

