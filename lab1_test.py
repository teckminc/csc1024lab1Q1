import lab1
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('12\n12\n13\n13\n14\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{12.8}') != -1