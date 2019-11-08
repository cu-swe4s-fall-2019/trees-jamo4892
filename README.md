Assignment 9: Trees

This assignment is largely incomplete. I did not have time to finish it.

`binary_tree.py` is a Python script that creates a class that defines a binary tree. It contains functions that inserts keys into the tree, and searches the tree for a specified key.

`insert_key_value_pairs.py` is a Python script that is supposed to take keys and a data structure type as inputs and time how long it takes to search the specficied data structure for the specified keys. I only completed the section of the 'main' function that determines the inputs. The script does not do anything.

`generate_key_value.sh` is a shell script that generates lists of keys- 1 list with random values, 1 list with values listed in sequence.

`binary_tree.py` and `insert_key_value_pairs.py` do not have any unit or functional tests. The only tests in .travis.yml are to test the Python scripts with pycodestyle, and to verify the shell script writes the text files.

Because the above scripts are incomplete, there is no information in this repo analyzing the performance of the trees as a data structure. Additionally, the AVL tree submodule is not tested or used at all. I did not incorporate my hash table repo as a submodule because I don't know if the hash table code is working properly.