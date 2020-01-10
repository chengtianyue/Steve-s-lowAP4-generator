import pandas as pd
import random

df = pd.read_csv(r'SteveslowAP4generator.csv')

def get_lists(df,phrase):
    return df[df[phrase].notnull()][phrase].tolist()

[bullshits,prefix_1,addings,examples,contrasts,prefix_2,suffix,author,saying] = [get_lists(df,i) for i in df.columns]


def sayings():
    xx = ''
    index= random.choice(range(len(saying)))
    if random.random() > 0.3:
        xx = author[index] + ' ' + random.choice(prefix_1) + saying[index] + ' ' +  random.choice(suffix).capitalize()
    else:
        xx = random.choice(prefix_2) + author[index] + ', ' + saying[index] + ' ' +  random.choice(suffix).capitalize()
    return xx

def paragraph():
    xx = ". "
    xx += "\r\n"
    xx += "      "
    return xx

def generator(theme,length):
    tmp = '    '
    counter = 0
    while (len(tmp) <= length):
        para = random.randint(0,100)
        if len(tmp) - counter >= 600:
            counter = len(tmp)
            tmp += paragraph()
        elif para < 20 :
            tmp += random.choice(examples)
            tmp += sayings()
        elif 20 <= para <= 65:
            tmp += random.choice(addings)
            tmp += random.choice(bullshits)
        else:
            tmp += random.choice(contrasts)
            tmp += random.choice(bullshits)
        tmp = tmp.replace("xx",theme)
    return tmp

def clean(a):
    a = a.replace('  ',' ').replace('. .','.').replace('? .','?').replace(', .',',').replace('..','.')
    lst = a.split(' ')
    for i in range(len(lst) - 1):
        if lst[i].endswith(',') or lst[i].endswith(':'):
            lst[i+1] = lst[i+1].lower()
    return ' '.join(lst)

word = str(input("Please enter the theme of the prompt:"))
tmp = generator(word,7000)
tmp = clean(tmp)
print(tmp)
