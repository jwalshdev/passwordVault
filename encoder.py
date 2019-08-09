class coder():
    
    def __init__(self):
        self._encoding_dict = {
            'a': '00',
            'b': '11',
            'c': '22',
            'd': '33',
            'e': '44',
            'f': '55',
            'g': '66',
            'h': '10',
            'i': '01',
            'j': '21',
            'k': '12',
            'l': '32',
            'm': '23',
            'n': '43',
            'o': '34',
            'p': '54',
            'q': '45',
            'r': '65',
            's': '56',
            't': '20',
            'u': '31',
            'v': '02',
            'w': '42',
            'x': '13',
            'y': '53',
            'z': '24',
            '1': '64',
            '2': '35',
            '3': '46',
            '4': '30',
            '5': '41',
            '6': '52',
            '7': '03',
            '8': '63',
            '9': '14',
            '0': '25',
            '?': '40',
            "'": '50',
            '_': '60',
            '#': '51',
            ' ': '61',
            '$': '62',
            '@': '04',
            '"': '05',
            '.': '15',
            '\n': '06',
            '-': '16',
            ',': '26',
            '!': '36',
            '*': '80',
            '(': '81',
            ')': '82',
            '/': '83',
            '%': '84',
            '&': '85',
            '+': '86',
            ':': '88',
            ';': '08',
            '<': '18',
            '>': '28',
            '=': '38',
            '[': '48',
            ']': '58',
            '\\': '68',
            '^': '90',
            '`': '91',
            '{': '92',
            '}': '93',
            '|': '94',
            '~': '95'
            } #available: 96, 98, 99, x9 for x in range(9)
        self._decoding_dict = {y:x for x,y in self._encoding_dict.items()}
        
    @property    
    def edict(self):
        return self._encoding_dict

    @property
    def ddict(self):
        return self._decoding_dict

    def encode(self, string):
        encoding_dict = self.edict
        estring = ''
        for l in string:
            try:
                if l.isupper():
                    estring += '7'
                estring += encoding_dict[l.lower()]
            except KeyError:
                pass
        return(estring)

    def decode(self, estring):
        decoding_dict = self.ddict
        dstring = ''
        c = 0
        b = True
        while b:
            try:
                if '7' in estring[c:c+2]:
                    c += 1
                    dstring += decoding_dict[estring[c:c + 2]].upper()
                else:
                    dstring += decoding_dict[estring[c:c+2]]
                c += 2
            except:
                break
        return(dstring)
