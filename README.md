# gufs : group-users files

gufs after being called, takes input (name of a group or groups) from the command line and locates all the files owned by the members of the group or groups and move them to an archive (as gzip’ed tar-file) directory. It is written to work only with Linux base operating system.

## Usage

* First ensure you python version 3 and above running on your linux operating system.

* Clone the guf repo, cd into the guf directory and run the  gufs.py script on your linux terminal. Note, user needs a root previledge to completely backup other users files.

    ``` 
    $ cd ../guf

    $ sudo python3 gufs.py
    ```

* The program takes the name of a group or names of groups as input from linux shell promt.

* Input could be just a name of a group or names of different groups separated by space.

* It takes also target directory as input from the prompt. If the input target directory does not exist, it creates a target directory for the backup using the input target directory name.

### compactability

This program is compactable with python >= 3 only.

### dependency

* tqdm : generates progress bar.

```
$ pip install tqdm
```

## Contact

Writen by Chinonso Collins Unaichi

email: unaichi.chinonso@gmail.com
