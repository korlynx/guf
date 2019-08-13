import pytest
from group_backup import GroupMembersFiles
from io import StringIO
import grp
import os


def test_double(monkeypatch):
   number_input = StringIO("l1 l2 l3")
   monkeypatch.setattr("sys.stdin", number_input)
   gm = GroupMembersFiles()
   assert gm.grp_names == ["l1", "l2", "l3"]


def testget_unique_users(monkeypatch):
   group1 = "newUsers"
   group2 = "foo"
   group_name_input = StringIO(group1+" "+group2)
   monkeypatch.setattr("sys.stdin", group_name_input)
   gm = GroupMembersFiles()
   #return gm.get_unique_users() == list()
   return gm.get_unique_users() == ["kait", "user1", "user2", "user3", "nonso"]



def test_check_backup_dir(monkeypatch):
   #os_dir = "/home/nonso/linux_project/"
   os_dir_input2 = "/home/nonso/backup"
   monkeypatch.setattr("sys.stdin", os_dir_input2)
   gm = GroupMembersFiles()
   return gm.check_backup_dir(os_dir_input2) == os.path.exists(os_dir_input2)
