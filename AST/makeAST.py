import sys
import ast
from ast2txt import ast2txt

def pyToTxt(filename):
    if filename[-3:] == '.py':
        filename = filename[:-3] + '.txt'
    return filename

def getValidPyFile(filename=''):
    if filename:
        pass
    elif len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = raw_input('Please enter the filename of a python script: ')

    f = None
    while (True):
        try:
            f = open(filename)
        except:
            print 'Error opening file', filename
            filename = raw_input('Please enter another filename: ')
        else:
            break
    return f, filename

def removeGeneInfo(contents_list):
    contents_list = contents_list[2:]
    contents = '\n'.join(contents_list)
    return contents


if __name__ == '__main__':
    f, filename = getValidPyFile()
    contents_list = f.readlines()
    filetext = removeGeneInfo(contents_list)
    tree = ast.parse(filetext)
    astfilename = pyToTxt(filename)
    astfile = open(astfilename, 'w')
    ast_text = ast2txt(tree)
    astfile.write(ast_text)
