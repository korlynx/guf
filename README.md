# gufs

Python program that locates all files owned by the members of a group and move the to an archive (a folder and a gzip’ed tar-file) directory.

# parameters

* The program takes the name of a group or names groups as input from linux shell promt.

* input can be just a name of a group or names of different groups seperated by space.

* It takes also target directory as input from the promt.

* If the tagert directory does not exist, it creates a new directory for the backup using.

# compactaility

This program is compactable with python 3 only.

# dependencies

* python
* tqdm