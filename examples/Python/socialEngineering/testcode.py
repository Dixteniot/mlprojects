# testcode.py

import abbreviation as word

if __name__ == '__main__':
    words = [{'Languege', 'symbols', 'signs'},
        {'Local', 'localized', 'localization'},
        {'Global', 'globalized', 'globilization'},
        {'International', 'internationalized', 'internationalization'},
        {'Internal', 'internalized', 'internalization'},
        {'National', 'nationalized', 'nationalization'},
        {'Regional', 'regionalized', 'regionalization'},
        {'Civil', 'civilized', 'civilization'},
        {'Social', 'socialized', 'socialization'},
        {'Engine', 'engineering'},
        {'Philosophy', 'philosophical'},
        {'0', '1', '2', '3', '...', '999'},
        {'a', 'bc', 'def', 'ghij', '0123456789', '+,-,*,/,%,=,.,&,?,!,@'},
    ]

    for x in words:
        for y in x:
            print('%s: %s'%(y, word.abbreviation(y)))
