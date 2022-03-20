#!/usr/bin/python3
# coding: utf-8
"""
this is objectexplore.py module
"""
import types
import builtins
import os
import psutil

def diro(obj):
    "return callables and attributes of the object argument"
    callables = [
        f'{attr}()' for attr in dir(obj) if callable(getattr(obj, attr))
    ]
    print('callables')
    print(callables)
    print('\n')
    print('attributes')
    attributes = [
        f'{attr}' for attr in dir(obj) if not callable(getattr(obj, attr))
    ]
    print(attributes)
    return 1

def dirdoc(obj):
    "return docs of callables of the object argument"
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            print(f'{attr}()')
            if attr.__doc__:
                print(attr.__doc__)
            print('\n\n')
    return 1

def dirpath(obj):
    "return path of file wher the code of of the object argument is written"
    try:
        print(obj.__globals__['__file__'])
        print(type(obj))
    except:
        try:
            if isinstance(obj, types.BuiltinFunctionType) or obj in builtins.__dict__.values():
                print('builtin object,class or function: cf shorturl.at/bhtA2 (stackoverflow)')
                print(type(obj))
                return 1
            print(f'le code se trouve dans le module {obj.__module__}')
            print(type(obj))
        except:
            print('chemin non trouvé')
    return 1

def dirpid():
    pid = os.getpid()
    # have to go two levels up to skip calling shell and 
    # get to actual parent process
    parent = psutil.Process(pid).parent().parent()
    print (f'Parent {parent.name()} [PID = {parent.pid}]' )
    print ('        |')
    for child in parent.children(recursive=True):
        print ('        |')
        if child.pid != pid:
            print (f'        - Child {child.name()} [PID = {child.pid}]')
        else:
            print (f'        - Child {child.name()} [PID = {child.pid}] (Self)')
