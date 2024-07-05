from pathlib import Path
from pytest import CaptureFixture
from pytest import mark

from src.coolang import load_cool_program

test_path = Path("./tests/coolang")
test_output_path = Path("./tests/coolang/output")

@mark.parametrize("file_path", list(test_path.glob("*.cl")))
def test_load_cool_program_output(file_path, capsys: CaptureFixture[str]):
    file_path = Path(file_path)
    with open(file_path) as f:
        load_cool_program(f.read())
    
    captured = capsys.readouterr()
    
    with open(test_output_path / file_path.name.removesuffix(".cl")) as out:
        assert captured.out == out.read()