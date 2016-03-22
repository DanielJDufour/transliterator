from distutils.core import setup

setup(
  name = 'transliterator',
  packages = ['transliterator'],
  package_dir = {'transliterator': 'transliterator'},
  package_data = {'transliterator': ['mappings/__init__.py','mappings/english_to_arabic.py','mappings/arabic_to_english.py','mappings/english_to_english.py','tests/__init__.py','tests/test.py']},
  version = '3.1',
  description = 'Transliterate text',
  author = 'Daniel J. Dufour',
  author_email = 'daniel.j.dufour@gmail.com',
  url = 'https://github.com/DanielJDufour/transliterator',
  download_url = 'https://github.com/DanielJDufour/transliterator/tarball/download',
  keywords = ['arabic','english','language','python'],
  classifiers = [],
)
