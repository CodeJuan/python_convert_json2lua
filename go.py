#/usr/bin/python

import sys
import simplejson as json


def printSubItem(key, value, prefix):
    #print '{}11111111111'.format(key)
    local = 'local ' + key + ' = {}'
    print local
    parseJson(value, key+'.')
    print '{}{} = {}'.format(prefix, key, key)
    #print '{}22222222222'.format(key)

def printArray(key, value, prefix):
    elements = '{'
    for i in value:
        elements += '"{}",'.format(i)
    elements = elements[:-1]
    elements += '}'

    print '{}{}{}{}'.format(prefix, key, ' = ', elements)

def printValue(key, value, prefix, substring):
    left = '{}{}{}'.format(prefix, key, ' = ')
    right = ''
    if 'None' in substring:
        right = 'gLuaNULL.null'
    elif 'True' in substring:
        right = 'true'
    else:
        right = '"{}"'.format(value)
    print '{}{}'.format(left, right)

def parseJson(jsonData, prefix):
    for key,value in jsonData.items():
        substring = '{}'.format(value)
        if '{' in substring:
            printSubItem(key, value, prefix)
        elif '[' in substring:
            printArray(key, value, prefix)
        else:
            printValue(key, value, prefix, substring)

def main(argv):
    file_name = argv[1]
    f = open(file_name)
    data = json.load(f)
    f.close()
    print 'local msg = {}'
    parseJson(data, 'msg.')

if __name__ == '__main__':
    main(sys.argv)


