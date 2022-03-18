def diro(obj):
    callables=['{}{}'.format(str(attr),'()') for attr in dir(obj) if callable(getattr(obj, attr))]
    print('callables')
    print(callables)
    print('\n')
    print('attributes')
    attributes=['{}'.format(str(attr)) for attr in dir(obj) if not callable(getattr(obj, attr))]
    print(attributes)
    

def dirdoc(obj):
    for attr in dir(obj):
         if callable(getattr(obj, attr)):
             print('{}{}'.format(str(attr),'()'))
             if attr.__doc__:
                 print(attr.__doc__)
             print('\n\n')
             
def dirpath(obj):
    print(obj.__globals__['__file__'])