import random
import vlc
import os
import time

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

l = 30
def menu(l):
    q = input('Нажми \'н\', чтобы начать, или \'нстр\', чтобы открыть настройки:')
    if q == 'нстр':
        q = input('Нажми \'д\', чтобы изменить длину сессии, или русское \'х\', чтобы выйти из настроек:')
        if q == 'д':
            l = int(input('Введи количество слов в сессии:'))
            menu(l)
        elif q == 'х':
            menu(l)
        else:
            print('Некорректный ввод.')
            menu(l)
    elif q == 'н':
        init(l)
    else:
        print('Некорректный ввод.')
        menu(l)


def init(l):
    di = {}
    with open ('words.txt', 'r', encoding='utf-8') as words:
        rl = words.readlines()
        for i in rl:
            spl = i.split(',')
            di[int(spl[0])] = (spl[1]).strip()
    session(di, l)


def session(di, l):
    n = len(di)
    rnums = random.sample(range(n), l)
    for i in rnums:
        ask(di, i)
    q = input('Сессия окончена! Нажми \'м\', чтобы вернуться в меню.')
    if q == 'м':
        menu(l)


def ask(di, i):
    print('Введи нужное слово. Или введи букву "п", чтобы услышать слово ещё раз.')
    filename = 'audio/' + str(i) + '.mp3'
    vplay(filename)
    inword = input()
    if di[i] == inword:
        print('Молодец!')
    elif inword == 'п':
        ask(di, i)
    else:
        print('Wat? По идее ' + di[i] + ', а у тебя ' + inword + '.')


def vplay(filename):
    time.sleep(2)
    player = vlc.MediaPlayer(filename)
    player.play()


menu(l)