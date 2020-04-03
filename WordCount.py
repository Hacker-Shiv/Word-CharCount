import string
file = open('test.txt', 'w+')
with open('Words.txt','r') as text:
    d = dict()
    for line in text:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] = d[word]+1
            else:
                d[word]=1
    for key in sorted(d):
        file.write("%s: %s" % (key, d[key]))
        print("%s: %s" % (key, d[key]))
