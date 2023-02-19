'''
    thanks to 'solvers & BB 
'''
import random

runes = ["ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚻ", "ᚾ", "ᛁ", "ᛂ", "ᛇ", "ᛈ", \
"ᛉ", "ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛝ", "ᛟ", "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", \
"ᛠ"]

rune_to_index ={"ᚠ": 0, "ᚢ": 1, "ᚦ": 2, "ᚩ": 3, "ᚱ": 4, "ᚳ": 5, "ᚷ": 6, \
"ᚹ": 7, "ᚻ": 8, "ᚾ": 9, "ᛁ": 10, "ᛂ": 11, "ᛇ": 12, "ᛈ":13, "ᛉ":14, "ᛋ": 15, "ᛏ": 16, "ᛒ": 17, "ᛖ": 18,
                "ᛗ":19, "ᛚ":20, "ᛝ": 21, "ᛟ": 22, "ᛞ": 23, "ᚪ": 24, "ᚫ":25, "ᚣ": 26, "ᛡ": 27, "ᛠ": 28}

latin2rune_dict = {'F': 'ᚠ', 'U': 'ᚢ', 'TH': 'ᚦ', 'O': 'ᚩ', 'R': 'ᚱ', 'C': 'ᚳ', 'G': 'ᚷ', 'W': 'ᚹ', 'H': 'ᚻ', 'N': 'ᚾ', 'I': 'ᛁ',
     'J': 'ᛂ', 'EO': 'ᛇ', 'P': 'ᛈ', 'X': 'ᛉ', 'S': 'ᛋ', 'T': 'ᛏ', 'B': 'ᛒ', 'E': 'ᛖ', 'M': 'ᛗ', 'L': 'ᛚ', 'ING': 'ᛝ',
     'OE': 'ᛟ', 'D': 'ᛞ', 'A': 'ᚪ', 'AE': 'ᚫ', 'Y': 'ᚣ', 'IA': 'ᛡ', 'EA': 'ᛠ', 'IO': 'ᛡ', 'K': 'ᚳ', 'NG': 'ᛝ', 'Z': 'ᛋ',
     'Q': 'ᚳ', 'V': 'ᚢ'}
rune2latin_dict = {
    'ᚠ': 'F',    'ᚢ': 'U',    'ᚦ': 'TH',    'ᚩ': 'O',    'ᚱ': 'R',    'ᚳ': 'C',
    'ᚷ': 'G',    'ᚹ': 'W',    'ᚻ': 'H',    'ᚾ': 'N',    'ᛁ': 'I',    'ᛂ': 'J',
    'ᛇ': 'EO',    'ᛈ': 'P',    'ᛉ': 'X',    'ᛋ': 'S',    'ᛏ': 'T',    'ᛒ': 'B',
    'ᛖ': 'E',    'ᛗ': 'M',    'ᛚ': 'L',    'ᛝ': 'ING',    'ᛟ': 'OE',    'ᛞ': 'D',
    'ᚪ': 'A',    'ᚫ': 'AE',    'ᚣ': 'Y',    'ᛡ': 'IA',    'ᛠ': 'EA',
}
runes = list(rune2latin_dict.keys())
BIGRM  = ['TH', 'EO', 'NG', 'OE', 'AE', 'IA', 'IO', 'EA']
TRGRAM = 'ING'

def latin2rune(char):
    return latin2rune_dict.get(char, char)

def translate_to_gematria(word):
    '''
        convert word standard english to runes (Latin)
    '''
    res = []
    skip = 0
    WORD = word.upper().replace("QU", "KW")
    WORD = WORD.replace("Q", "K")
    for i, val in enumerate(WORD):
        if skip:
            skip -= 1
            continue
        if WORD[i:i + 3] == TRGRAM:
            res.append(TRGRAM)
            skip += 2
            continue
        if WORD[i:i + 2] in BIGRM:
            res.append(WORD[i:i + 2])
            skip += 1
            continue
        if WORD[i] == '\'':
            res.append('\'')
            continue
        if WORD[i] == '"':
            res.append('"')
            continue
        res.append(val)
    return ''.join([latin2rune(r) for r in res])

def sentence_to_gematria(sent):
    return ' '.join([translate_to_gematria(x) for x in sent.split()])

def rune_to_latin(rune_string):
    return [" " if x == " " else rune2latin_dict[x] for x in rune_string]

def randomRune(num, rune_omit = ""):
    l = runes
    if rune_omit != "":
        assert rune_omit in runes
        l = [x for x in runes if x != rune_omit]
    r = random.choices(l, k =num)
    return r




