import binary_tree
import os
import sys
import argparse
import time
# Import modules.

if __name__ == '__main__':
    """
    Main function. Details to be added later.
    """
    parser = argparse.ArgumentParser(description='Trees',
                                     prog='insert_key_value_pairs.py')
    parser.add_argument('--structure', type=str, required=True,
                        help='Hash, AVL or Tree to use')

    parser.add_argument('--data', type=str, required='True',
                        help='File with data to use')
    parser.add_argument('--pairs', type=int, required='True',
                        help='Amount of keys/values to use')
    args = parser.parse_args
    # Define input parameters.
