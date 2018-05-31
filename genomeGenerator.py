"""

takes lines of text and converts them into a genome and translation table,
which are then converted into code.
{} indicates that the next line should be inserted into the current code block.

For instance:

for {} in {}:
x
range({})
10
print {}
{},{}
"{}"
Num:
x

would translate to (with codon length 3):
translation = {'001':'for {} in {}', '002':'x', '003':'range({})', '004':'10',
    '005':'print {}', '006':'{},{}', '007':'"{}"', '008':'Num:', '009':'x'}

genome = '001002003004005006007008009'

The reproduction framework would then translate the genome to:

for x in range(10):
    print "Num:",x

When converting a genome into code, the indentation level is automatically
increased whenever a line ends with a colon, but dedentation must be
manually specified by a line 'dedent'

"""

"""
Takes a dictionary and returns a new dictionary with the keys and values flipped
Called by: list2dicts
"""
def reverseDict(input_dict):
    output_dict = {}
    for key in input_dict:
        output_dict[input_dict[key]] = key
    return output_dict


"""
Takes a list of codons and assigns a string value to each, of length codon_length
Returns two dictionaries: one string value -> code block, and the other block -> string value
Called by: makeOrganism
"""
def list2dicts(gene_list, codon_length=3):
    codon_count = 0
    code2str_dict = {}
    for node in gene_list:
        node = node.strip()
        if node not in code2str_dict:
            codon = str(codon_count)
            codon = (codon_length - len(codon))*'0' + codon
            code2str_dict[node] = codon
            codon_count += 1
    str2code_dict = reverseDict(code2str_dict)
    return code2str_dict, str2code_dict


"""
Outputs the lines of a text file in a list
Called by: makeOrganism
"""
def txt2list(file_name='genomeAST.txt'):
    gene_list = []
    while not gene_list:
        try:
            genome_file = open(file_name, 'r')
            gene_list = genome_file.readlines()
        except Exception as e:
            print e
            file_name = raw_input('Which text file has the genome AST?')
    return gene_list


"""
Takes a list of codons and dictionary of code block -> string value and returns the concatenated string values
Called by: makeOrganism
"""
def list2str(gene_list, gene_dict):
    genome_str = ''
    for gene in gene_list:
        gene = gene.strip()
        genome_str += gene_dict[gene]
    return genome_str


"""
Based on a position on a string, a dictionary of string value -> code block, 
and string length to evaluate, returns a complete line of code with gaps filled in
Called by: str2list, getTree
"""
def getTree(position, genome_str, gene_dict, codon_length=3):
    codon = genome_str[position:position + codon_length]
    node = gene_dict[codon]
    position += codon_length
    node_list = []
    if node != '{}':
        for i in range(node.count('{}')):
            subnode, position = getTree(position, genome_str, gene_dict, codon_length)
            node_list.append(subnode)
        node = node.format(*node_list)
    return node, position


"""
Takes a string, string value -> code block dictionary, and string length, and returns a list of lines of code.
Called by: str2code
"""
def str2list(genome_str, gene_dict, codon_length):
    code_list = []
    position = 0
    while position < len(genome_str):
        value, position = getTree(position, genome_str, gene_dict, codon_length)
        code_list.append(value)
    return code_list


"""
Writes a list of code lines to a string that can be pasted into a file and then run
Called by: str2code
"""
def list2code(gene_list):
    output = ''
    indent = 0
    for line in gene_list:
        if len(line) == 0:
            output += '\n'
        elif line[-1] == ':':
            output += '\n' + ' ' * (4*indent) + line
            indent += 1
        elif line == 'dedent':
            indent -= 1
            indent = max(indent,0)
        else:
            output += '\n' + ' ' * (4*indent) + line
    return output


"""
Converts a string, string value -> code block dictionary, and string length of each block into executable code
Called by: makeOrganism
"""
def str2code(genome_str, gene_dict, codon_length=3):
    code_list = str2list(genome_str, gene_dict, codon_length)
    return list2code(code_list)


"""
Takes a genome string, string to code dictionary, file contents, and name parts and creates a file
Called by: makeOrganism
"""
def makeOrganismFile(genome_str, gene_dict, organism_code, location_id='000', unique_id='aaaaaaaa'):
    organism_name = location_id + '_' + unique_id + '.py'
    organism = open(organism_name, 'w')
    organism.write('translation = ' + str(gene_dict))
    organism.write('\n' + 'genome = \'' + genome_str + '\'')
    organism.write(organism_code)
    organism.close()


"""
Takes a file with code contents, string length for translation, and organism location and name
Creates a file named [location]_[name].py with the code contents
Called by: main
"""
def makeOrganism(ast_file, codon_length, location_id, unique_id):
    gene_list = txt2list(ast_file)
    code2str_dict, str2code_dict = list2dicts(gene_list, codon_length)
    genome_str = list2str(gene_list, code2str_dict)
    organism_code = str2code(genome_str, str2code_dict, codon_length)
    makeOrganismFile(genome_str, str2code_dict, organism_code, location_id, unique_id)

if __name__ == '__main__':
    makeOrganism('genomeAST.txt', 3, '000', 'aaaaaaaa')
