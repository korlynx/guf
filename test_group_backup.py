import pytest
from group_backup import GroupMembersFiles


group_name = "newUser"
def test_check_groupname():
   #groupName = GroupMembersFiles()
   #if groupName == group_name:
   assert groupName.get_grp_infos(group_name) == dict()

