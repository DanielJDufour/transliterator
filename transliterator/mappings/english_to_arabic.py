d = {}

d[' '] = ['_', ' ','']
d['-'] = ['_', ' ','']
d['_'] = ['_', ' ','']

# note: sometimes a disappears when in middle of word because short vowel
#            alif   alif-hamza   3ayn   ta-marbuta alif-maqsura
d['a'] = [u'\u0627',u'\u0623',u'\u0639',u'\u0629',u'\u0649','']

#             ba
d['b'] = [u'\u0628']

#             dal     dal with space after
d['d'] = [u'\u062f',u'\u062f ']

#            alif   alif-hamza    ya
d['e'] = [u'\u0627',u'\u0623',u'\u064a','']

#            fa
d['f'] = [u'\u0641']

#            g/jim
d['g'] = [u'\u062c']

#           heavy-ha, soft he
d['h'] = [u'\u062d',u'\u0647','']

#                  ya     alif kasra
d['i'] = [u'\u064a', u'\u0625','']

#           gim/jja
d['j'] = [u'\u062c']

#             lam
d['l'] = [u'\u0644']

#             mim
d['m'] = [u'\u0645']

#                noon
d['n'] = [u'\u0646','']

#                waw
d['o'] = [u'\u0648','']

#             ra     # sometimes r-repeated like hurriya
d['r'] = [u'\u0631',u'']

#             sin     shim    elided-lam   saad
d['s'] = [u'\u0633',u'\u0634',u'\u0644',u'\u0635']

#             shim
d['sh'] = [u'\u0634']

#         tar-mabuta  deep-taa
d['t'] = [u'\u0629',u'\u0637']

#             waw      alif
d['u'] = [u'\u0648',u'\u0627','']

#             waw
d['w'] = [u'\u0648']

#             ya
d['y'] = [u'\u064a']

#             za
d['z'] = [u'\u0632','']

#for key, values in d.iteritems():
#    d['key'] = values + [ v+" " for v in values]

english_to_arabic = d
