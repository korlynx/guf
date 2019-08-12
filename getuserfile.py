#!/bin/python

import grp
#import operator
import subprocess
import os
import logging

# 
def check_backup_dir(os_dir):
    """
    This function;
    - checks if target backup directory exists
    - otherwise it creates target backup directory automatically
    """

    if not os.path.exists(os_dir):
        print(os_dir, "does not exist.")
        
        
        get_con_ = input(
            "Do you want this program to create {} ?  yes/no\n".format(os_dir))

        if get_con_ == "yes":
            print("creating", os_dir)
            os.mkdir(os_dir)
        else:
            exit(1)


def get_confirmation():
    """"
    This function;
    - Gets backup confirmation from admin.
    """
    get_ans = input(
        "Do you want to continue to back up files for all group members? yes/no\n")

    if get_ans == "yes":
        con_exit = 0
        return con_exit
    elif get_ans == "no":
        exit(1)
    else:
        print("answer with yes or no")
    get_confirmation()


def check_group():
    """
    This function;
    -checks if group exist
    -prints out group information
    """
    
    grp_name = input("enter group name: ")
    try:
        group_info_ = grp.getgrnam(grp_name)
        print("{}".format(str(group_info_)))

        # confirm if admin wants to continue with back up
        get_confirmation()

    except KeyError:
        print("input group name {} does not exist!".format(grp_name))
        exit(1)
    
    return grp_name


def backup_group_user_files():
    """
    This function;
    - creates a log file
    - copys members all files to an archive directory
    """
    # get group name from as input from terminal  
    grp_name = check_group()

    # get back up directory as input from terminal
    backup_target = input("enter target backup directory: ")

    # check if directory exists, otherwise create target backup directory automatically
    check_backup_dir(backup_target)

    #create a log file for the archived group members
    logging.basicConfig(format='%(asctime)-15s: %(levelname)s: %(message)s',
                        filename= "backup.log", level=logging.DEBUG)

    # get group informations
    group_info_ = grp.getgrnam(grp_name)

    if group_info_:
        logging.info("{}".format(str(group_info_)))
    else:
        logging.warning("group name {} does not exit".format(str(grp_name)))

    # get members in the input group
    grp_members = group_info_.gr_mem
    logging.info("group members {}".format(str(grp_members)))

    # copy member files to an archive directory
    for user_name in grp_members:
        res = subprocess.call(["cp", "-rf", "/home/"+user_name, backup_target])

        if res == 0:
            logging.info(
                "back up {} files to an archive directory successful".format(str(user_name)))
            logging.info("exit status = {}".format(str(res)))
        else:
            logging.info(
                "back up {} files to an archive directory failed".format(str(user_name)))
            logging.warning("exit status = {}".format(str(res)))
    print("back up is succesful")


def main():
    backup_group_user_files()



if __name__ == "__main__":
    main()
