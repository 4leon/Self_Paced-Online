#!/usr/bin/env python3
# strformat_lab.py
# Coded by LouReis

# Task 1
# Write a format string that will take the following four element tuple:
#        ( 2, 123.4567, 10000, 12345.67)
#        and produce:
#        'file_002 :   123.46, 1.00e+04, 1.23e+04'

"file_{:0>3d}:  {:.2f}, {:.2e}, {:.2e}".format(2,123.4567, 10000, 12345.67)

# Task 2
# Write a format string that will take the following four element tuple:
