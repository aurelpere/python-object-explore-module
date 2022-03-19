#!/usr/bin/python3
# coding: utf-8
"""
this is objectexplore.py module
"""
import types
import builtins

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
            print(type(__builtins__))
            if isinstance(obj, types.BuiltinFunctionType) or obj in builtins.__dict__.values():
                print('builtin object,class or function: cf shorturl.at/bhtA2 (stackoverflow)')
                print(type(obj))
                return 1
            print(f'le code se trouve dans le module {obj.__module__}')
            print(type(obj))
        except:
            print('chemin non trouvé')
    return 1
