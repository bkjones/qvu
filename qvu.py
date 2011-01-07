from __future__ import print_function
import pyclbr
import sys
import operator

if __name__ == '__main__':
    modname = sys.argv[2]
    methname = sys.argv[1]

    mod = pyclbr.readmodule(modname)
    for clsname, cls in mod.items():
        if methname in cls.methods:
            print("Method: {} in Class: {}".format(methname, clsname))
            methods = sorted(cls.methods.items(), key=operator.itemgetter(1))
            clsfile = open(cls.file, 'r')
            break

    for pair in methods:
        name, lineno = pair
        if name == methname:
            startline = lineno
            if methods.index(pair) == methods.index(methods[-1]):
                endline = None
            else:
                endline = methods[methods.index(pair) + 1][1]
            break

    src = clsfile.readlines()[startline-1:endline-1 if endline is not None else -1]
    for srcline in src:
        print(srcline, end='')




                
                

    

