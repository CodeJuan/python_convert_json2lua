#/usr/bin/python

import sys
import simplejson as json


def parseJson(jsonData, prefix):
    for key,value in jsonData.items():
        substring = '{}'.format(value)
        if '{' in substring:
            print value
        elif '[' in substring:
            print value
        else:
            print value

def main(argv):
    file_name = argv[1]
    f = open(file_name)
    data = json.load(f)
    f.close()
    parseJson(data, 'msg.')

if __name__ == '__main__':
    main(sys.argv)