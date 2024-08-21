#any pytest file should start withb test_
#any function/method in pytest file we define should start with test_
import py
import pytest


def test_firstprogram():
    print("hullo")
def test_sfirstprogramcredircard():
    print("hullo")

#if i mark some testcase as smoke so for this one write this command first
@pytest.mark.smoke
def test_sfirstprogredircard():
    print("hulloss")
#@pytest.xfail  with using this the testcase will run but in output you cant see it is pass or fail
# @pytest.mark.skip  it is used for skipping in one specific test case
