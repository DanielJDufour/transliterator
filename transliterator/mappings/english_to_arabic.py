d = {}

d[' '] = ['','_', ' ']
d['-'] = ['','_', ' ']
d['_'] = ['','_', ' ']

# note: sometimes a disappears when in middle of word because short vowel
#            alif   alif-hamza
d['a'] = ['',u'\u0627',u'\u0623']

#             ba
d['b'] = [u'\u0628']

#             dal
d['d'] = [u'\u062f']

#              heavy-ha
d['h'] = [u'', u'\u062d']

#                  ya     alif kasra
d['i'] = [u'', u'\u064a', u'\u0625']

#             jja
d['j'] = [u'\u062c']

#             lam
d['l'] = [u'\u0644']

#             mim
d['m'] = [u'\u0645']

#             ra
d['r'] = [u'\u0631']

#             sin     shim
d['s'] = [u'\u0633',u'\u0634']

#             shim
d['sh'] = [u'\u0634']

#                noon
d['n'] = [u'',u'\u0646']

#             ya
d['y'] = [u'\u064a']

english_to_arabic = d
