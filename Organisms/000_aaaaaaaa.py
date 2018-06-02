translation = {'098': 'genome = \\"', '099': '\\"', '126': 'python', '090': '_', '091': '.py', '092': 'offspring', '093': 'open', '094': 'w', '095': 'write', '096': 'translation = ', '097': 'str', '010': 'global {}', '132': 'stderr', '131': 'stdout', '013': 'selfName', '014': 'world', '136': 'communicate', '016': '{} = {}', '134': 'True', '018': '3', '019': '{}[{}]', '139': 'acting_organism', '138': 'dict', '127': '{}={}', '120': 'otherName', '121': 'interact', '027': '-1', '123': 'getMessage', '021': '{}.{}', '125': 'Popen', '023': '0', '022': 'argv', '128': 'bufsize', '129': 'stdin', '029': 'getcwd', '028': '/', '133': 'universal_newlines', '011': 'metabolism', '012': 'codonLength', '130': 'PIPE', '137': 'parsedResponse', '015': 'sightDistance', '135': 'fullResponse', '017': '0.5', '089': 'offspringName', '115': 'tryToMove', '114': 'rename', '117': '100', '039': 'translation', '111': 'move', '110': '1000', '113': 'newName', '112': 'distance', '032': 'getTree', '033': 'position', '030': '300', '031': 'dedent', '036': '{}:{}', '118': 'initiateInteraction', '034': 'codon', '035': 'genome', '051': 'value', '108': '({}%{})', '109': 'int', '148': 'organismLocation', '049': 'count', '048': 'range', '102': 'name', '103': 'intToString', '100': 'close', '084': 'makeOffspring', '043': 'if {}:', '042': '[{}]', '104': 'num', '040': '{} += {}', '055': 'return {}', '076': 'letters', '077': 'chars', '153': 'raw_input', '047': 'i', '075': 'kind', '058': 'code_list', '059': 'while {}:', '046': 'for {} in {}:', '054': '*{}', '155': 'loads', '056': 'translate', '057': 'output', '050': '({})', '045': '{{}}', '052': 'append', '053': 'format', '044': '{} != {}', '070': '1', '106': 'getNewPosition', '073': 'getRandomString', '156': 'except {}:', '107': 'direction', '041': 'newContainer', '105': '({}-{})', '061': 'len', '060': '{} < {}', '063': 'line', '062': 'indent', '065': ':', '064': '{} == {}', '067': '({}*{})', '066': '\\n', '069': '5', '068': ' ', '160': 'print {}', '038': 'aacid', '116': 'uniform', '151': '{} > {}', '150': 'abs', '074': 'length', '152': 'startConditions', '072': '{} -= {}', '154': 'try:', '157': 'type', '071': 'else:', '159': 'None', '158': 'get', '078': 'abcdefghijklmnopqrstuvwxyz', '079': 'numbers', '088': 'alphanumeric', '119': 'organisms', '037': '({}+{})', '101': 'splitName', '146': 'location', '147': 'nearby', '144': '-3', '145': 'findNearbyOrganisms', '142': 'organism', '143': 'listdir', '140': 'dumps', '141': 'getAllOrganisms', '083': 'choice', '082': 'string', '081': '0123456789abcdefghijklmnopqrstuvwxyz', '080': '0123456789', '087': '8', '086': 'uniqueID', '085': 'locationID', '149': '({} or {})', '003': 'random', '002': 'sys', '001': '{},{}', '000': 'import {}', '007': 'def {}({}):', '006': 'subprocess', '005': 'json', '004': 'os', '009': '', '008': 'getTraits', '025': "'{}'", '024': 'split', '122': 'message', '026': '\\\\', '124': 'otherOrganism', '020': '{}({})'}
genome = '000001002001003001004001005006007008009010011010012010013010014010015016011017016012018016013019020021019020021019021002022023024025026027024025028027016014020021004029009016015030031007032033016034019035036033037033012016038019039034040033012016041042009043044038025045046047020048020021038049025045016050001051033020032033020021041052051031016038020021038053054041031055050001038033031007056009016057025009016058042009016033023059060033020061035016050001051033020032033020021058052051031016062023046063058043064019063027025065040057037037025066067025068067069062063040062070031071043064063025031072062070031071040057037037025066067025068067069062063031031031055057031007073001074075043064075025076016077025078031071043064075025079016077025080031071016077025081031031016082025009046047020048074040082020021003083077031055082031007084009016085020073001018025079016086020073001087025088016089037037037085025090086025091016092020093001089025094020021092095037025096020097039020021092095037037037025066025098035025099020021092095020056009020021092100009031007101102055020021102024025090031007103001104074016104020097104046047020048105074020061104016104037025023104031055104031007106001033107055108037020109033107110031007111112010013016050001033086020021013024025090043060021003003017016107070031071016107027031046047020048112016033020103001020106001033107018016113037037033025090086020021004114001013113016013113031031007115009043060020021003003009011016112020109067011020021003116001070117020111112031031007118119016120020021003083119020121120031007121120016122020123009016124020021006125001042001025126120001127128070001127129021006130001127131021006130001127132021006130127133134016135020021124136122016137019135023031007123009016122020138009016019122025139013055020021005140122031007141014016119042009046142020021004143014043064019142036144009025091020021119052142031031055119031007145119016146020109019020101013023016147042009046142119043044142013016148020109019020101142023043149060020150105148146015151020150105148146105110015020021147052142031031031055147031020008009016152020153009154016152020021005155152031156009016152020138009031043044020157152138016152020138009031043064020021152158025139159020115009016119020141014016147020145119043147020118147031020084009031071020115009160020123009031'
import sys,random,os,json,subprocess
def getTraits():
    global metabolism
    global codonLength
    global selfName
    global world
    global sightDistance
    metabolism = 0.5
    codonLength = 3
    selfName = sys.argv[0].split('\\')[-1].split('/')[-1]
    world = os.getcwd()
    sightDistance = 300
def getTree(position):
    codon = genome[position:(position+codonLength)]
    aacid = translation[codon]
    position += codonLength
    newContainer = []
    if aacid != '{}':
        for i in range(aacid.count('{}')):
            (value,position) = getTree(position)
            newContainer.append(value)
        aacid = aacid.format(*newContainer)
    return (aacid,position)
def translate():
    output = ''
    code_list = []
    position = 0
    while position < len(genome):
        (value,position) = getTree(position)
        code_list.append(value)
    indent = 0
    for line in code_list:
        if line[-1] == ':':
            output += (('\n'+(' '*(5*indent)))+line)
            indent += 1
        else:
            if line == 'dedent':
                indent -= 1
            else:
                output += (('\n'+(' '*(5*indent)))+line)
    return output
def getRandomString(length,kind):
    if kind == 'letters':
        chars = 'abcdefghijklmnopqrstuvwxyz'
    else:
        if kind == 'numbers':
            chars = '0123456789'
        else:
            chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    string = ''
    for i in range(length):
        string += random.choice(chars)
    return string
def makeOffspring():
    locationID = getRandomString(3,'numbers')
    uniqueID = getRandomString(8,'alphanumeric')
    offspringName = (((locationID+'_')+uniqueID)+'.py')
    offspring = open(offspringName,'w')
    offspring.write(('translation = '+str(translation)))
    offspring.write(((('\n'+'genome = \"')+genome)+'\"'))
    offspring.write(translate())
    offspring.close()
def splitName(name):
    return name.split('_')
def intToString(num,length):
    num = str(num)
    for i in range((length-len(num))):
        num = ('0'+num)
    return num
def getNewPosition(position,direction):
    return ((int(position)+direction)%1000)
def move(distance):
    global selfName
    (position,uniqueID) = selfName.split('_')
    if random.random < 0.5:
        direction = 1
    else:
        direction = -1
    for i in range(distance):
        position = intToString(getNewPosition(position,direction),3)
        newName = ((position+'_')+uniqueID)
        os.rename(selfName,newName)
        selfName = newName
def tryToMove():
    if random.random() < metabolism:
        distance = int((metabolism*random.uniform(1,100)))
        move(distance)
def initiateInteraction(organisms):
    otherName = random.choice(organisms)
    interact(otherName)
def interact(otherName):
    message = getMessage()
    otherOrganism = subprocess.Popen(['python',otherName],bufsize=1,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
    fullResponse = otherOrganism.communicate(message)
    parsedResponse = fullResponse[0]
def getMessage():
    message = dict()
    message['acting_organism'] = selfName
    return json.dumps(message)
def getAllOrganisms(world):
    organisms = []
    for organism in os.listdir(world):
        if organism[-3:] == '.py':
            organisms.append(organism)
    return organisms
def findNearbyOrganisms(organisms):
    location = int(splitName(selfName)[0])
    nearby = []
    for organism in organisms:
        if organism != selfName:
            organismLocation = int(splitName(organism)[0])
            if (abs((organismLocation-location)) < sightDistance or abs((organismLocation-location)) > (1000-sightDistance)):
                nearby.append(organism)
    return nearby
getTraits()
startConditions = raw_input()
try:
    startConditions = json.loads(startConditions)
except :
    startConditions = dict()
if type(startConditions) != dict:
    startConditions = dict()
if startConditions.get('acting_organism') == None:
    tryToMove()
    organisms = getAllOrganisms(world)
    nearby = findNearbyOrganisms(organisms)
    if nearby:
        initiateInteraction(nearby)
    makeOffspring()
else:
    tryToMove()
    print getMessage()