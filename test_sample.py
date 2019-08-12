from __future__ import print_function

import mock
import sys
from group_backup import GroupMembersFiles

if sys.version_info >= (3, 0):
    ips = 'builtins.input'
    #input = input
else:
    ips = '__builtin__.raw_input'
    input = raw_input


def something():
    print("test")
    x = input('\nEnter stuff\n')
    print("s")
    return x


def test_something():
    with mock.patch(ips, return_value='newUsers'):

        assert GroupMembersFiles() == "newUsers"


