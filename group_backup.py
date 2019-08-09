
import grp
import subprocess
import os
import logging
import itertools
import numpy as np

#create a log file for the archived group members
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    filename="backup.log", level=logging.DEBUG)

class getGroupMembersFiles(object):

    def __init__(self):
        self.grp_names = input("enter group name/(s): ").split(" ")
        logging.info("input group name {}".format(str(self.grp_names)))
        

    def get_and_check_grp_info(self):
        """"
        This function;
        - gets and prints out group infomations
        - create a unique list of users incase if one user belongs to multiple groups
        """

        self.grp_mem_ = list()

        for grp_name in self.grp_names:
            self.grp_name = grp_name
            try:
                self.group_info_ = grp.getgrnam(self.grp_name)
                print("{}".format(str(self.group_info_)))
                logging.info("{}".format(str(self.group_info_)))

            except KeyError:
                print("input group name {} does not exist!".format(self.grp_name))
                logging.warning(
                    "input group name {} does not exist!".format(self.grp_name))
                exit(1)
                logging.info(
                    "exit status 1 {} does not exist".format(self.grp_name))
            self.grp_mem_.append(self.group_info_.gr_mem)

        
        # gets unique list of group members to avoid duplicate backup
        self.grp_members = np.unique(
            list(itertools.chain.from_iterable(self.grp_mem_)))
        logging.info("generating unque users list from group name/(s)")
        return self.grp_members


    def get_confirmation(self):
        """"
        This function;
        - Gets backup confirmation from admin.
        """
        self.get_ans = input(
            "Do you want to continue to back up files for all group members? yes/no\n")

        if self.get_ans == "yes":
            self.con_exit = 0
            logging.info("back up permission granted {}".format(str(self.con_exit)))

        elif self.get_ans == "no":
            self.con_exit = 1
            logging.info("back up permission not granted {}".format(str(self.con_exit)))
            exit(1)

        else:
            logging.error("enter yes or no to confirm back up permission")
            print("answer with yes or no")
            self.get_confirmation()


    def check_backup_dir(self, os_dir):
        """
        This function;
        - checks if target backup directory exists
        - otherwise it creates target backup directory automatically
        """
        self.os_dir = os_dir
        if not os.path.exists(self.os_dir):
            print(self.os_dir, "does not exist.")

            self.get_con_ = input(
                "Do you want this program to create {}? yes/no\n".format(self.os_dir))

            if self.get_con_ == "yes":
                print("creating new backup directory {}".format(str(self.os_dir)))
                
                self.new_dir = os.mkdir(self.os_dir)
                logging.info("new directory {} created".format(str(self.new_dir)))
                return self.new_dir
            else:
                
                logging.warning(
                    "exit status 1 {} does not exist".format(self.os_dir))
                exit(1)
        return self.os_dir

        
    def backup_group_user_files(self):
        """
        This function;
        - copys members all files to an archive directory
        """
        # get group names from as input from terminal
        grp_names_ = self.grp_names

        # get group informations
        group_info_ = self.get_and_check_grp_info()
        logging.info(
            "list of users file to be archived: {}".format(str(group_info_)))

        # assert back up permission
        self.get_confirmation()

        # get back up directory as input from terminal
        self.backup_target = input("enter target backup directory: ")
        logging.info("get target directory name from terminal")
        # check if directory exists, otherwise create target backup directory automatically
        target_dir = self.check_backup_dir(self.backup_target)

        # copy members files to an archive directory
        for self.user_name in group_info_:
            self.res = subprocess.call(["cp", "-rf", "/home/"+self.user_name, target_dir])

            if self.res == 0:
                logging.info(
                    "back up {} files to an archive directory successful".format(str(self.user_name)))
                logging.info("exit status = {}".format(str(self.res)))
            else:
                logging.info(
                    "back up {} files to an archive directory failed".format(str(self.user_name)))
                logging.warning("exit status = {}".format(str(self.res)))
        print("back up completed succesfully")

try:

    group_names_input = getGroupMembersFiles()
    group_names_input.backup_group_user_files()

except KeyError:

    print("program failed to complete back up process")
    logging.error("back up process failed exit status 1")
