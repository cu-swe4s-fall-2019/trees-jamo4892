#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle binary_tree.py
assert_no_stdout
run test_style pycodestyle insert_key_value_pairs.py
assert_no_stdout
# Verify pycodestyle formatting in all Python scripts.

run test_txt_output bash generate_key_value.sh
assert_exit_code 0
# Verify text files of key/value pairs are generated successfully.