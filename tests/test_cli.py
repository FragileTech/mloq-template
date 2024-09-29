import subprocess


def test_main():
    cmd_name = "mloq-template"
    output = subprocess.check_output([cmd_name, "foo", "foobar"], text=True)
    assert cmd_name in output or "foobar\n" in output
