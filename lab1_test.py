import lab1
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('12\n12\n13\n13\n14\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{12.8}') != -1

def test_case2(monkeypatch, capsys):
    number_inputs = StringIO('12.1\n12.6\n13.3\n13.7\n14.1\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{13.16}') != -1

def test_case3(monkeypatch, capsys):
    number_inputs = StringIO('12.111\n12.6145\n13.378\n13.732\n14.111\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{13.19}') != -1