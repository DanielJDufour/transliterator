#-*- coding: utf-8 -*-
arabic_to_english = {}

#tha, ha, ba, sin, ra, qaf, lam, nun
consonants_ar = [u'\u062b', u'\u062d', u'\u0628', u'\u0633',u'\u0631', u'\u0642', u'\u0644', u'\u0646']

#alif, wa, ya
vowels_ar = [u'\u0627',u'\u0648',u'\u064a']

#consonants_en = ['b','c','d','f','g','h','

#blank space
arabic_to_english[u' '] = [u'',' ']

#alif
arabic_to_english[u'\u0627'] = [u'a',u'o']

#alif hamza
arabic_to_english[u'\u0623'] = [u'a']

#alif hamza with hamza at bottom
arabic_to_english[u'\u0625'] = [u'i']

#ba
arabic_to_english[u'\u0628'] = ['b']

# ta
arabic_to_english[u'\u062a'] = [u't']

# tha
arabic_to_english[u'\u062b'] = [u'th']

#ja/ga
arabic_to_english[u'\u062c'] = ['j','g','ja','ga']

# ha'
arabic_to_english[u'\u062d'] = [u'h',u'ha',u'he']

# dal
arabic_to_english[u'\u062f'] = [u'd']

# ghayn
arabic_to_english[u'\u063a'] = [u'gh']

#ra
arabic_to_english[u'\u0631'] = [u'r',u'ra']

# za
arabic_to_english[u'\u0632'] = [u'z',u'zz']

#sin
arabic_to_english[u'\u0633'] = [u's','sa']

#shin connected
arabic_to_english[u'\u0634'] = [u'sh',u'shu',u'sha']

#sad
arabic_to_english[u'\u0635'] = [u's',u'sa']

#deep ta
arabic_to_english[u'\u0637'] = [u't',u'ta']

# ayn
arabic_to_english[u'\u0639'] = [u'3',u'a',u'']

# fa
arabic_to_english[u'\u0641'] = [u'f',u'fa']

#qaf
arabic_to_english[u'\u0642'] = [u'q',u'qu']

#kaf
arabic_to_english[u'\u0643'] = [u'k',u'ka']

##lam
arabic_to_english[u'\u0644'] = [u'l',u'l-',u'l ',u's',u's-',u's ',u'sh',u'sh-','sh ',u't',u't-',u't ',u'th',u'th-',u'th ','la',u'li']

#mim solo
arabic_to_english[u'\u0645'] = ['m','ma','mu']

#nun
arabic_to_english[u'\u0646'] = [u'n', u'na']

#tar ma-buta
arabic_to_english[u'\u0629'] = [u'a',u'at']

#light ha/he
arabic_to_english[u'\u0647'] = ['','h','ha','he']

#wa
arabic_to_english[u'\u0648'] = [u'u',u'o','w','wa']

# ya, said ee
arabic_to_english[u'\u064a'] = [u'y',u'i',u'iyy',u'yyi','ee']

#hamza solo
arabic_to_english[u'\u0621'] = [u""]

#hamza on ya
arabic_to_english[u'\u0626'] = ['i',"'i"]

#left-to-right mark
arabic_to_english[u'\u200e'] = ['']
