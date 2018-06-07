# ALife
Python 2.7

The beginnings of an artificial life experiment starting with a framework to convert a genome string into functional code.

genomeGenerator reads genomeAST.txt - a flattened Abstract Syntax Tree - and creates a genome and dictionary to translate that genome into code.  It then uses the genome and dictionary to write the code to a new Python file named 000_aaaaaaaa.py.

Organisms are named xxx_yyyyyyyy, where x is a random number, and y is a random alphanumeric. 
The first three characters are used to indicate location in an alphabetically-sorted directory, and the last eight are maintained as a unique organism name.

When the organism files are run, the organisms reproduce, copying their own genome into a new file, and attempt to travel in the directory by renaming themselves.

Organisms' code is saved as a text file with each line as a node, and curly brackets indicating a subnode. The code is then converted to a genome string and dictionary for converting that string into executable code.

For instance:

for {} in {}:
x
range({})
10
print {}
{},{}
'{}'
Num:
x

would translate to (with codon length 3):
translation = {'001':'for {} in {}', '002':'x', '003':'range({})', '004':'10',
    '005':'print {}', '006':'{},{}', '007':'"{}"', '008':'Num:', '009':'x'}

genome = '001002003004005006007008009'

The reproduction framework would then translate the genome to:

`for x in range(10):
    print "Num:",x`
    
makeAST can be used to automatically convert the code from a .py file to the flattened AST, and genomeGenerator translates that text file into the genome string and dictionary, which the organisms can translate back into the executable .py code.


