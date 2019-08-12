import app
from group_backup import GroupMembersFiles

def test_app():
    input_values = [2, 3]
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)
    app.input = mock_input
    app.print = lambda s: output.append(s)

    app.main()

    assert output == [
        'First: ',
        'Second: ',
        'The result is 5',
    ]


def test_init():
    input_grpname = "newUsers"
    output = []

    def mock_input(s):
        output.append(s)
        return input_grpname.pop(0)

    GroupMembersFiles().input = mock_input
    GroupMembersFiles().print = lambda s: output.append(s)
    GroupMembersFiles()

    assert output == ["newUsers"]

