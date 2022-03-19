#!/usr/bin/python3
# coding: utf-8
"""
this is test_objectexplore.py
"""
import sys
import io
import numpy
import pandas as pd
from objectexplore import diro
from objectexplore import dirdoc
from objectexplore import dirpath

def test_diro():
    """test diro"""
    string_object = ''
    captured_output = io.StringIO()
    sys.stdout = captured_output
    diro(string_object)
    sys.stdout = sys.__stdout__
    for attr in dir(string_object):
        if callable(getattr(string_object, attr)):
            assert f'{attr}()' in captured_output.getvalue()
        else:
            assert str(attr) in captured_output.getvalue()
    return 1

def test_dirdoc():
    """test dirdoc"""
    string_object = ''
    captured_output = io.StringIO()
    sys.stdout = captured_output
    dirdoc(string_object)
    sys.stdout = sys.__stdout__
    for attr in dir(string_object):
        if callable(getattr(string_object, attr)):
            assert f'{attr}()' in captured_output.getvalue()
            assert str(attr.__doc__) in captured_output.getvalue()
    return 1

def test_dirpath():
    """test dirpath"""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    dirpath(str)
    sys.stdout = sys.__stdout__
    print(captured_output.getvalue())
    assert "cf shorturl.at/bhtA2" in captured_output.getvalue()
    captured_output = io.StringIO()
    sys.stdout = captured_output
    dirpath(numpy.where)
    sys.stdout = sys.__stdout__
    assert "site-packages/numpy/" in captured_output.getvalue()
    captured_output = io.StringIO()
    sys.stdout = captured_output
    dirpath(pd.DataFrame)
    sys.stdout = sys.__stdout__
    assert "module pandas.core.frame" in captured_output.getvalue()
    captured_output = io.StringIO()
    sys.stdout = captured_output
    dirpath(numpy.tan)
    sys.stdout = sys.__stdout__
    assert "chemin non trouvé" in captured_output.getvalue()
    return 1
