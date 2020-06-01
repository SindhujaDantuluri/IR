import re
from collections import defaultdict, Counter
DATA = [
    {
        'title': 'Django',
        'description': 'Django is a high-level Python Web framework that '
            'encourages rapid development and clean, pragmatic design.  Built by '
            'experienced developers, it takes care of much of the hassle of Web '
            'development, so you can focus on writing your app without needing to '
            
    },
    {
        'title': 'Python',
        'description': 'Python is a programming language that lets you work '
            'more quickly and integrate your systems more effectively.'
    },
]

SPLIT_RE = re.compile(r'[^a-zA-Z0-9]')
def tokenize(text):
    yield from SPLIT_RE.split(text)

def text_only(tokens):
    for t in tokens:
        if t.isalnum():
            yield t

def lowercase(tokens):
    for t in tokens:
        yield t.lower()

def stem(tokens):
    for t in tokens:
        if t.endswith('ly'):
            t = t[:-2]
        yield t




def analyze(text):
    tokens = tokenize(text)
    for token_filter in (text_only, lowercase, stem):
        tokens = token_filter(tokens)
    yield from tokens

def index_docs(docs, *fields):
    index = defaultdict(lambda: defaultdict(Counter))
    for id, doc in enumerate(docs):
        for field in fields:
            for token in analyze(doc[field]):
                index[field][token][id] += 1
    return index



index = index_docs(DATA, 'title', 'description')
print(index)

