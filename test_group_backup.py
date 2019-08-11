import pytest
from io import StringIO
from group_backup import GroupMembersFiles

#number_inputs = StringIO('1234\n')
#def test_inputgroupname(monkeypatch):
   # monkeypatch.setattr('sys.stdin', number_inputs)
   # group_name = GroupMembersFiles()
   # assert group_name.__init__() == str()


group_name = GroupMembersFiles()
get_input = group_name.__init__()
def test_inputgroupname():
    assert get_input == str()
