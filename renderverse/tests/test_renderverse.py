"""
Unit and regression test for the renderverse package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import renderverse


def test_renderverse_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "renderverse" in sys.modules
