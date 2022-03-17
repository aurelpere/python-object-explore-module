# python-object-explore-module
a python module to explore libraries callables and attributes...useful when the doc is scarce

usage:
* diro(object) 
prints a list of object.callables() and a list of object.attributes and returns a tuple (list(callables),list(attributes))
*dirdoc(object)
print recursively the callables and their doc

to import automatically the functions in python :
* create a module object-explore with the object-explore.py file in this repo
* add from object-explore import * in ~/.python_shell_startup.py
* add export PYTHONSTARTUP=~/.python_shell_startup.py in your ~/.bashrc or ~/.zshrc

