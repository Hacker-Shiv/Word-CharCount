from collections import Counter
file = input ('Enter file name: ')
char = input('Enter the character to be counted: ').lower()
with open(file, 'rt', encoding="utf8") as text:
    a = Counter(text.read().lower())
    var = a[char]
    print('File', "'",file,"'", 'has', str(var), 'instances of letter', "'",char,"'")
