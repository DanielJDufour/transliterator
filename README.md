# transliterator
transliterator transliterates between Arabic and English

# Installation
```
pip install transliterator
```

# Use
```
from transliterator import get_transliteration_as_pattern
text = "Marhaban"
pattern = get_transliteration_as_pattern(text, from_="English", to_="Arabic")
print pattern
# prints u'(?:\u0645)(?:|\u0627|\u0623)(?:\u0631)(?:|\u062d)(?:|\u0627|\u0623)(?:\u0628)(?:|\u0627|\u0623)(?:|\u0646)'
```

# Features
| Languages Supported |
| ------------------- |
| Arabic |
| English |

# Testing
To test the package run
```
python -m unittest transliterator.tests.test
```
