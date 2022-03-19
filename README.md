[![Test-Lint-Format](https://github.com/aurelpere/python-object-explore-module/actions/workflows/main.yml/badge.svg)](https://github.com/aurelpere/python-object-explore-module/actions/workflows/main.yml) ![test-coverage badge](./coverage-badge.svg) [![Maintainability](https://api.codeclimate.com/v1/badges/4bd58efebdf3a6ec0ac5/maintainability)](https://codeclimate.com/github/aurelpere/python-object-explore-module/maintainability) 

# python-object-explore-module
a python module to explore libraries callables and attributes...useful when the doc is scarce

usage:<br>
`diro(object)`<br>
>prints a list of object.callables() and a list of object.attributes 

`dirdoc(object)`<br>
>print recursively the callables and their doc<br>

`dirpath(obj):`<br>
>print the absolute path of the file in which obj is defined<br>

to import automatically the functions in python :
1. find your modules path : type `print(sys.path)` in python interpreter
2. put objectexplore.py file in one of the modules path
3. add `from objectexplore import *` in ~/.python_shell_startup.py
4. add `export PYTHONSTARTUP=~/.python_shell_startup.py` in your ~/.bashrc or ~/.zshrc

