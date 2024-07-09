glossary = {
    'string': ' A sequence of characters.',
    'list': ' A series of items in a consecutive order.',
    'variable': ' A "container" for storing data values.',
    'integer': ' An integer is a whole number.',
    'float': " A float is a function or code in Python that converts values into floating point numbers.",
    }

#print each word and its meaning as neatly formatted output
#print the word followed by a colon and then its meaning
word = 'string'
print("\n" + word.title() + ":" + glossary[word])

word = 'list'
print("\n" + word.title() + ":" + glossary[word])

word = 'variable'
print("\n" + word.title() + ":" + glossary[word])

word = 'integer'
print("\n" + word.title() + ":" + glossary[word])

word = 'float'
print("\n" + word.title() + ":" + glossary[word])
