import lab6q2
from io import StringIO
from sys import stderr

def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('testing\n54\n48\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q2.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'50') != -1
    assert captured_stdout.strip().find(f'49') != -1
    assert captured_stdout.strip().find(f'48') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab6q2.py") as tf:
    head = [next(tf) for _ in range(23)]
    s = tf.read()
    assert(s.find("for") != -1 )
    assert(s.find("range") != -1 )

