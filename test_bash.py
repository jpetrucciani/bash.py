import pytest


@pytest.fixture
def bash():
    from bash import Bash

    return Bash()


@pytest.fixture
def run():
    from bash import run

    return run


@pytest.fixture
def environ():
    return {"HELLO": "WORLD"}


def test_run(run):
    c = run("echo hi")
    assert c.ok
    assert "hi" in c.output


def test_environ(environ):
    from bash import Bash

    bash = Bash(environ=environ)
    env_proc = bash.command("env")
    assert env_proc.ok
    # assert "WORLD" in env_proc.output
