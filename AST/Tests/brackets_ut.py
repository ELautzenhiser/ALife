test = {1:'one',2:'two'}
test_str = '{ this is {} a test }'

for key in test:
    print test[key]

for i in xrange(test_str.count('{}')):
    print i
