from shutil import copytree, make_archive
import os
import grp
import logging
import itertools
import numpy as np
import time
from tqdm import tqdm

#create a log file
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    filename="backup.log", level=logging.DEBUG)


class GroupMembersFiles:
    """
    This program 
    locates all files owned by the members of a group and moved them to an archive folder 
    """

    def __init__(self):
        grp_names = input("enter group name/(s): ")
        self.grp_names = grp_names.split(" ")
        logging.info("input group name {}".format(str(self.grp_names)))
        print("generating group info")

    def get_grp_infos(self):

        for grp_name in self.grp_names:

            try:
                self.group_info_ = grp.getgrnam(grp_name)
                print("{}".format(str(self.group_info_)))
                logging.info("{}".format(str(self.group_info_)))

            except KeyError:
                print("input group name {} does not exist!".format(grp_name))
                logging.warning(
                    "input group name {} does not exist!".format(grp_name))
                exit(1)
                logging.info(
                    "exit status 1 {} does not exist".format(grp_name))

    def get_unique_users(self):
        """"
        This function;
        - creates a unique list of all users, incase a user belongs to multiple groups
        """

        self.grp_mem_ = list()
        for grp_name in self.grp_names:
            self.grp_name = grp_name
            self.grp_mem_.append(grp.getgrnam(self.grp_name).gr_mem)

        self.grp_members = np.unique(
            list(itertools.chain.from_iterable(self.grp_mem_)))  # gets unique list of group members to avoid duplicate backup
        logging.info("generating unique users list from group name/(s)")

        return self.grp_members

    def get_confirmation(self):
        """"
        This function;
        - Gets backup confirmation from admin.
        """
        self.get_con = input(
            "Do you want to continue to back up files for all group users above? yes/no\n")

        if self.get_con == "yes":
            self.con_exit = 0
            logging.info("back up permission granted {}".format(
                str(self.con_exit)))

        elif self.get_con == "no":
            self.con_exit = 1
            logging.info("back up permission not granted {}".format(
                str(self.con_exit)))
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
            return 1
        else:
            return self.os_dir

    def create_new_target_dir(self, os_dir):
        self.new_dir = os.mkdir(os_dir)
        return self.new_dir

    def backup_group_user_files(self):
        """
        This function;
        - copys members all files to an archive directory
        """

        grp_names_ = self.grp_names  # get group names from as input from terminal

        # get group informations
        group_info_ = self.get_grp_infos()
        grp_users = self.get_unique_users()
        logging.info(
            "names of users to be backuped: {}".format(str(grp_users)))
        print(grp_users)

        self.get_confirmation()  # assert back up permission

        # get back up directory as input from terminal
        backup_target = input("enter target backup directory: ")
        logging.info("get target directory name from terminal")

        # check if directory exists, otherwise create target backup directory automatically
        target_dir = self.check_backup_dir(backup_target)

        if target_dir == 1:
            print(backup_target, "does not exist.")
            self.get_con_ = input(
                "do you want this program to create {}? yes/no\n".format(backup_target))

        if self.get_con_ == "yes":
            print("creating new backup directory {}".format(backup_target))
            target_dir = self.create_new_target_dir(backup_target)
        else:
            exit(1)

        # copy members files to an archive directory
        for user_name in tqdm(grp_users, desc='creating archive'):
            path_dir = "/home/"
            logging.info("starting backup of {} files".format(user_name))
            res_dir = copytree(path_dir+user_name, str(backup_target)+"/"+user_name)

            # create gzip’ed tar-file archive
            archive_name = os.path.expanduser(os.path.join(str(backup_target), user_name))
            root_dir = os.path.expanduser(os.path.join(path_dir, user_name))
            res_tar = make_archive(archive_name, 'gztar', root_dir)

            logging.info(
                "created gzip’ed tar-file backup of {}".format(user_name))
            logging.info(
                "backup of {} files successful".format(user_name))
            logging.info("exit status = 0")
            
            time.sleep(3)


def gufs():
    group_names_input = GroupMembersFiles()
    group_names_input.backup_group_user_files()
    print("backup process completed")


if __name__ == "__main__":
    try:

        gufs()

    except KeyError:

        print("Backup process failed, something went wrong!!!")

