"""Smoke tests for the console entry point."""

import pytest

from route_tester import __version__
from route_tester.cli import build_parser


def test_parser_exposes_the_package_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        build_parser().parse_args(["--version"])

    assert exit_info.value.code == 0
    assert __version__ in capsys.readouterr().out
