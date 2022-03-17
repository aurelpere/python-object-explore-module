# python-object-explore-module
a python module to explore libraries callables and attributes...useful when the doc is scarce

usage:<br>
`diro(object)`<br>
>prints a list of object.callables() and a list of object.attributes 

`dirdoc(object)`<br>
>print recursively the callables and their doc<br>

to import automatically the functions in python :
1. find your modules path : type `print(sys.path)` in python interpreter
2. put objectexplore.py file in one of the modules path
3. add `from objectexplore import *` in ~/.python_shell_startup.py
4. add `export PYTHONSTARTUP=~/.python_shell_startup.py` in your ~/.bashrc or ~/.zshrc

