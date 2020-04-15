#!/usr/bin/env python3

#import sys
#sys.path.insert(0, '/home/isabella/Documentos/Insper/9oSemestre/OpenDev/pacote_exemplo/dev_aberto/')
from dev_aberto import hello
#import dev_aberto

if __name__ == '__main__':
    date, name = hello()
    print('Último commit feito em:', date, ' por', name)
