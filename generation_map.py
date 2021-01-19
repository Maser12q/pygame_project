import pygame

from random import choice, random

from entities.tile import Tile
from entities.player import Player
from config import TILE_SIZE


EMPTIES = ' .@MPElrtb'
BARRIERS = '1234567890-=BC'


# "0-9" + "-=" - Walls
# . - Floor
# r, t, l, b - Doors
# M - Mob (Monster)
# P - Player, start stairs
# C - Chest
# T - Torch
# E - End stairs
# B - Box/Barrel


# Карты комнат
START_ROOM = '''
03338t63339
5.........1
5.........1
5....T....1
8.........6
l..T.P.T..r
2.........4
5....T....1
5.........1
5.........1
-7772b4777=
'''

EVIL_ROOM_1 = '''
03338t63339
5.........1
5.M.....M.1
5..B.....C1
8.........6
l.........r
2...B.....4
5......T..1
5.M.....M.1
5.........1
-7772b4777=
'''

EVIL_ROOM_2 = '''
03338t63339
5.......MC1
5.47777777=
5.633333339
8....B...B6
l.........r
2.T.......4
-77777772.1
033333338.1
5CM.......1
-7772b4777=
'''

EVIL_ROOM_3 = '''
03338t63339
5........B1
5.........1
5..T.M....1
8.........6
l..M.C.M..r
2.........4
5....M....1
5...B.....1
5.........1
-7772b4777=
'''

EVIL_ROOM_4 = '''
03338t63339
5B........1
-2.....M.4=
08.......69
8........B6
l.........r
2B.....T..4
-2.M.....4=
08.......69
5.........1
-7772b4777=
'''

EVIL_ROOM_5 = '''
03338t63339
5.........1
5....M....1
5..47772..1
8..1   5..6
l..1   5..r
2..1   5..4
5..63338..1
5.T..M...B1
5.......BB1
-7772b4777=
'''

EVIL_ROOM_6 = '''
03338t6339 
5........69
5.........1
5.........1
8.........6
l....T....r
2.........4
5..M......1
5......B..1
-2.....BBB1
 -772b4777=
'''

EVIL_ROOM_7 = '''
03338t63339
5..M....BB1
5.........1
5M........1
8.........6
l...T.....r
2.........4
5.........1
5.B.......1
5......477=
-7772b4=   
'''

EVIL_ROOM_8 = '''
03908t69039
5.15..B15.1
5.68...68.1
5......M..1
8.........6
l....T....r
2.........4
5.........1
5.42...42.1
5B15...15.1
-7=-2b4=-7=
'''

EVIL_ROOM_9 = '''
 0338t6339 
08......B69
5........B1
5.........1
8.........6
l....T....r
2.........4
5.....M...1
5.........1
-2.......4=
 -772b477= 
'''

EVIL_ROOM_10 = '''
  038t639  
  5.....1  
038.....639
5B........1
8...472...6
l..T1 5...r
2...638...4
5.........1
-72.....47=
  5...BB1  
  -72b47=  
'''

EVIL_ROOM_11 = '''
03338t63339
5..B...B..1
5.BB......1
5...B.....1
8........B6
l....T....r
2......B..4
5..B......1
5.....B...1
5M.......M1
-7772b4777=
'''

EVIL_ROOM_12 = '''
03338t63339
5M.......M1
5.........1
5.........1
8.........6
l...BT.B..r
2....B.B.B4
5.BB.BBB.B1
5..BB...BB1
5B....BBBB1
-7772b4777=
'''

EVIL_ROOM_13 = '''
03338t63339
5B......BB1
5B........1
5.........1
8...M.....6
l...TCM...r
2...M.....4
5.........1
5.........1
5.........1
-7772b4777=
'''

EVIL_ROOM_14 = '''
03338t639  
5B......69 
5........69
5.........1
8.........6
l....T....r
2.........4
5B........1
-2B......M1
 -2.....MC1
  -72b4777=
'''

EVIL_ROOM_15 = '''
   08t69   
   -2.4=   
    5.1    
09  5.1  09
86338.63386
l.........r
24772.47724
-=  5.1  -=
    5.1    
   08.69   
   -2b4=   
'''

EVIL_ROOM_16 = '''
03338t63339
5.........1
5....M....1
5..47772..1
8..10338..6
l..15C....r
2..1-772T.4
5..63338..1
5....MB...1
5.........1
-7772b4777=
'''

EVIL_ROOM_17 = '''
   08t69   
  08...69  
 08.....69 
08.......69
8B........6
l....T....r
2.........4
-2.......4=
 -2M...M4= 
  -2...4=  
   -2b4=   
'''

EVIL_ROOM_18 = '''
   08t69   
  08...69  
 08....B69 
08.....B.69
8.....B...6
l....T....r
2.........4
-2.......4=
 -2M...M4= 
  -2B..4=  
   -2b4=   
'''

EVIL_ROOM_19 = '''
   08t69   
  08...69  
 08.....69 
08.......69
8.........6
l.........r
2BB.......4
-2.T.....4=
 -2M...M4= 
  -2B..4=  
   -2b4=   
'''

EVIL_ROOM_20 = '''
   08t69   
  08...69  
 08.....69 
08.......69
8......B..6
l.....BB..r
2...T.....4
-2......C4=
 -2M...M4= 
  -2...4=  
   -2b4=   
'''

EVIL_ROOM_21 = '''
03338t63339
5.........1
-7772.4777=
    5.69   
33338.C6333
l...MT....r
77772.47777
    5M1    
03338.63339
5.........1
-7772b4777=
'''

EVIL_ROOM_22 = '''
03338t63339
-7772.4777=
    5.1    
    5.69   
33338.C6333
l.........r
77772.47777
    5.69   
03338.C6339
5.M.T.....1
-7772b4777=
'''

EVIL_ROOM_23 = '''
    5t1    
03338.63339
5.BB......1
5..B.BB.B.1
8B...B....6
l.B....B..r
2..T.B.BBB4
5...B.B...1
5.......B.1
-7772.4777=
    5b1    
'''

EVIL_ROOM_24 = '''
    5t1    
 0338.6339 
 5......B1 
 5.......1 
38.M.....63
l....T....r
72.......47
 5..M...C1 
 5.B..B.B1 
 -772.477= 
    5b1    
'''

EVIL_ROOM_25 = '''
    5t1    
    5.1    
  038.639  
  5....B1  
338M...C633
l....T....r
772.....477
  5M....1  
  -72.47=  
    5.1    
    5b1    
'''

EVIL_ROOM_26 = '''
03338t639  
5.......639
5MBBT.....1
5..B......1
8BBB...M..6
l.........r
2.........4
5........B1
5B..M.....1
-72......B1
  -72b4777=
'''

EVIL_ROOM_27 = '''
03338t69   
5.B...B6339
5.M.......1
5B........1
8.........6
l....T....r
2.........4
5......B.M1
5.B.....B.1
-772....BC1
   -2b4777=
'''

EVIL_ROOM_28 = '''
    5t1    
    5.1    
    5.1    
   08.69   
3338M..6333
l....T....r
7772..M4777
   -2.4=   
    5.1    
    5.1    
    5b1    
'''

EVIL_ROOM_29 = '''
    5t1    
    5.1    
    5.1    
    5.1    
33338.63333
l.........r
77772.47777
    5.1    
    5.1    
    5.1    
    5b1    
'''

EVIL_ROOM_30 = '''
   08t69   
  08...69  
 08.....69 
08.......69
8......B..6
l.....BB..r
2...T.M...4
-2......C4=
 -2M....4= 
  -2...4=  
   -2b4=   
'''

DOUBLE_EVIL_ROOM_1 = '''
03338t6333903338t63339
5.........68.........1
-2...............B..4=
08.42B....42C....42.69
8..68..T..68..T..68..6
l....................r
2B.42..T..42..T..42..4
-2.68.....68B...B68.4=
08..................69
5.........42.........1
-7772b4777=-7772b4777=
'''

DOUBLE_EVIL_ROOM_2 = '''
 0338t6333903338t6339 
08........68........69
5.....B...M...B......1
5..M.............M...1
8.......T...T........6
l..B.....C.C.....B...r
2.......T...T........4
5..M.............M...1
5.....B...M...B......1
-2........42........4=
 -772b4777=-7772b477= 
'''

DOUBLE_EVIL_ROOM_3 = '''
03338t639    038t63339
5.......633338BB.....1
5.M....T......T......1
5........B...........1
8...M....4772..M.....6
l........1  5........r
2.....M.B6338....M...4
5........BBC.........1
5......T......T....M.1
5.......477772.......1
-7772b47=    -72b4777=
'''

DOUBLE_EVIL_ROOM_4 = '''
03338t6333333338t63339
5..M..............M..1
5.42.42.42..42.42.42.1
5.68.68.68..68.68.68.1
8..B...T......T......6
l....................r
2......T......T......4
5.42.42.42..42.42.42.1
5.68.68.68..68.68.68.1
5....M..........M....1
-7772b4777777772b4777=
'''

DOUBLE_EVIL_ROOM_5 = '''
03338t6333333338t63339
5....................1
5.472B.472..472..472.1
5.1 5..1 5..1 5..1 5.1
8.638..638.M638..638.6
l.......T....T.......r
2.472..472M.472..472.4
5.1 5..1 5..1 5..1 5.1
5.638..638..638B.638.1
5....................1
-7772b4777777772b4777=
'''

DOUBLE_EVIL_ROOM_6 = '''
03338t6333333338t63339
5M..................M1
5.BBBBBBBBBBBBBBBBBB.1
5.B.T..B....T........1
8.B.BB.BBBBB.BBBBBBB.6
l.B.B...T..B.B..T..B.r
2.B.BBBBBBBB.BBBBB.B.4
5.B..T........T....B.1
5.BBBBBBBBBBBBBBBBBB.1
5M..................M1
-7772b4777777772b4777=
'''

DOUBLE_EVIL_ROOM_7 = '''
03338t6333333338t63339
5.B.......B..........1
5..T..............T..1
5...............B....1
8...B..M.....CM......6
l....................r
2......MC.....M......4
5BB......B......B....1
5..T..............T..1
5.BB..........B......1
-7772b4777777772b4777=
'''

CHEST_ROOM_1 = '''
   08t69   
   5...1   
   -2.4=   
03908.69039
8.68...68B6
l.....T...r
2.42...42.4
-7=-2.4=-7=
   08.69   
   5...1   
   -2b4=   
'''

CHEST_ROOM_2 = '''
03338t63339
5.B.......1
5.........1
5B........1
8.....B...6
l..BCB....r
2...B..T..4
5........B1
5.........1
5.......BB1
-7772b4777=
'''

CHEST_ROOM_3 = '''
03338t639  
5C......639
-7772....B1
03395B....1
8..68.....6
l.........r
2T....42..4
5.....1-77=
5B....63339
-72......C1
  -72b4777=
'''

CHEST_ROOM_4 = '''
03338t63339
5.........1
5.........1
5......T..1
8.........6
l.........r
2.........4
5..T......1
5.........1
5.........1
-7772b4777=
'''

EMPTY_ROOM = '''           \n           \n           
           \n           \n           \n           
           \n           \n           \n           '''

END_ROOM = '''
03338t63339
5.........1
5.........1
5..T...T..1
8.........6
l....E....r
2.........4
5..T...T..1
5.........1
5.........1
-7772b4777=
'''

COVERT_ROOM_1 = '''
03333F33339
5.........1
5.........1
5..T...T..1
5....C....1
F...C.C...F
5....C....1
5..T...T..1
5.........1
5.........1
-7777F7777=
'''

COVERT_ROOM_2 = '''
03333F33339
5.........1
5.........1
5..T...T..1
5...C.C...1
F.........F
5...C.C...1
5..T...T..1
5.........1
5.........1
-7777F7777=
'''

COVERT_ROOM_3 = '''
03333F33339
5.........1
5.........1
5.........1
5.........1
F.........F
5.........1
5.........1
5........T1
5.......TC1
-7777F7777=
'''

# Группы комнат по использованию
STANDARD_ROOMS = {
      'E1': EVIL_ROOM_1,
      'E2': EVIL_ROOM_2,
      'E3': EVIL_ROOM_3,
      'E4': EVIL_ROOM_4,
      'E5': EVIL_ROOM_5,
      'E6': EVIL_ROOM_6,
      'E7': EVIL_ROOM_7,
      'E8': EVIL_ROOM_8,
      'E9': EVIL_ROOM_9,
      'E10': EVIL_ROOM_10,
      'E11': EVIL_ROOM_11,
      'E12': EVIL_ROOM_12,
      'E13': EVIL_ROOM_13,
      'E14': EVIL_ROOM_14,
      'E15': EVIL_ROOM_15,
      'E16': EVIL_ROOM_16,
      'E17': EVIL_ROOM_17,
      'E18': EVIL_ROOM_18,
      'E19': EVIL_ROOM_19,
      'E20': EVIL_ROOM_20,
      'E21': EVIL_ROOM_21,
      'E22': EVIL_ROOM_22,
      'E23': EVIL_ROOM_23,
      'E24': EVIL_ROOM_24,
      'E25': EVIL_ROOM_25,
      'E26': EVIL_ROOM_26,
      'E27': EVIL_ROOM_27,
      'E28': EVIL_ROOM_28,
      'E29': EVIL_ROOM_29,
      'E30': EVIL_ROOM_30,
      'C1': CHEST_ROOM_1,
      'C2': CHEST_ROOM_2,
      'C3': CHEST_ROOM_3,
      'C4': CHEST_ROOM_4,
}

DOUBLE_ROOMS = {
    'D1': DOUBLE_EVIL_ROOM_1,
    'D2': DOUBLE_EVIL_ROOM_2,
    'D3': DOUBLE_EVIL_ROOM_3,
    'D4': DOUBLE_EVIL_ROOM_4,
    'D5': DOUBLE_EVIL_ROOM_5,
    'D6': DOUBLE_EVIL_ROOM_6,
    'D7': DOUBLE_EVIL_ROOM_7
}

SECRET_ROOMS = {
    'C1': COVERT_ROOM_1,
    'C2': COVERT_ROOM_2,
    'C3': COVERT_ROOM_3
}


# Карты комнат в уровнях
LEVEL_1 = '''
  RR RRR RR  
 RSRR RRRR   
RRR RRRR RRE 
 RRRR RR RRRR
RRR RRRRR    
  RR R RRRRRC
'''      # 50

LEVEL_2 = '''
   R  RRR SR 
 RRRR R RRRRR
RRR RRRRR   R
RR RRR    RRR
 RRRRR RRRR C
RER RRRRR    
'''      # 50

LEVEL_3 = '''
 RR   R   RRC
  RRRRRRERR  
RRR  RRR  RRR
  RRR   RRR  
RRR  RRR  RRR
  RSRRRRRRR  
 RR   R   RR 
'''      # 50

LEVEL_4 = '''
RRRR RRR RS C
 R  R RRRRR R
RR RRR R RRRR
R R R  R  RR 
 RRRR  R RRRE
RRR RRRRRR  R
'''      # 50

LEVEL_5 = '''
CR   RR RRRER
 RR R RRR R  
  RRRRR RRR  
RRR  R R R RR
R R RRRRRRRR 
  RSR R   R  
   R  RRRRR  
'''      # 50

LEVEL_6 = '''
  RRR     
 RR RRRRRR
 R     R R
 RRRRR R S
  R    R  
RRR RR RR 
  R  RRR  
R RRRRR   
R R   RRR 
RRE  RR RC
'''      # 50

LEVEL_7 = '''
 E  RRRRRR
 RRRR   R 
  R RR  RR
  R  R   C
  RRRRRR  
  R    RRR
 RRRR  R  
 R  R RRR 
C  RRRR RR
RRRR  RR S
'''      # 50

LEVEL_8 = '''
   RRRRRRR
 ERR  R  R
 R    R  R
 R    R  R
RRRRR RRRR
 R  R  R  
RR  R  R  
 R  R RRRR
 R RRRR  R
CRRR     S
'''      # 50

LEVEL_9 = '''
 ER    RR
  R  RRR 
  RRRR   
RRR  RRRR
  R     R
 RRRR   R
  R R RRR
  R  RR  
 RR   RRR
  S  CR  
'''      # 50

LEVEL_10 = '''
  RRR  S  
    R  RRR
C   RRRR R
RR  R  RRR
 RRRR    R
    R   RR
 RRRR   R 
 R    RRRR
RR R RR  E
 RRRRR  RR
'''      # 50

# Группа уровней
FORMS = {
    'L1': LEVEL_1,
    'L2': LEVEL_2,
    'L3': LEVEL_3,
    'L4': LEVEL_4,
    'L5': LEVEL_5,
    'L6': LEVEL_6,
    'L7': LEVEL_7,
    'L8': LEVEL_8,
    'L9': LEVEL_9,
    'L10': LEVEL_10
}

SHORT_BLOCK_CHANCE = 45
LONG_BLOCK_CHANCE = 35


# Сама функция генерации
def generate_new_level(user_seed=None) -> [str, ..., str]:
    '''
    Создаёт список строк, каждый символ в строке означает определенный тайл
    Генерация происходит псевдорандомно, выбирая случайный шаблон уровня,
    а затем для каждого символа формы выбирает случайную комнату. 
    С некоторым шансом из двух комнат может быть создана одна большая.
    Вместо дверей ставится либо стена, либо, если возможно, с некоторым шансом, "блок".
    Если генерация уже происходила и у вас есть сид, вы можете передать его этой функции,
    тогда карта будет сгенерирована по тем же параметрам. 
    Совпадение будет по форме уровня, каждой комнате и блоках из стен в комнатах.
    '''
    level = []
    seed = []
    if user_seed:
        seed.append(user_seed[0])
        del user_seed[0]
    else:
        seed.append(choice(list(FORMS)))
    level_form = FORMS[seed[-1]]

    if true_with_chance(50, seed, user_seed):
        level_form = level_form.replace('S', '@').replace('E', 'S').replace('@', 'E')

    level_form = level_form.strip('\n').split('\n')
    doubled = False
    for i in range(len(level_form)):
        room_row = list(level_form[i])
        rooms = []
        for j in range(len(room_row)):
            if doubled:
                doubled = False
                continue

            if j + 1 < len(room_row):
                if room_row[j] == room_row[j + 1] == 'R' and true_with_chance(15, seed, user_seed):
                    room_row[j] = room_row[j + 1] = 'D'

            if room_row[j] == 'S':
                room = START_ROOM
            elif room_row[j] == 'E':
                room = END_ROOM
            elif room_row[j] == 'D':
                if user_seed:
                    seed.append(user_seed[0])
                    del user_seed[0]
                else:
                    seed.append(choice(list(DOUBLE_ROOMS)))
                room = DOUBLE_ROOMS[seed[-1]]
                doubled = True
            elif room_row[j] == 'R':
                if user_seed:
                    seed.append(user_seed[0])
                    del user_seed[0]
                else:
                    seed.append(choice(list(STANDARD_ROOMS)))
                room = STANDARD_ROOMS[seed[-1]]
            elif room_row[j] == 'C':
                if user_seed:
                    seed.append(user_seed[0])
                    del user_seed[0]
                else:
                    seed.append(choice(list(SECRET_ROOMS)))
                room = SECRET_ROOMS[seed[-1]]
            else:
                room = EMPTY_ROOM
            rooms.append(room.strip('\n').split('\n'))

        for number_row in range(len(rooms[0])):
            row = []
            for room_a in rooms:
                row += list(room_a[number_row])
            level.append(row)

    for i in range(len(level)):
        for j in range(len(level[i])):
            # Убираем фпальшивые двери там, где они не нужны
            if level[i][j] == 'F':
                if j == 0 or level[i][j - 1] == ' ':
                    level[i][j] = '5'
                elif j + 1 == len(level[i]) or level[i][j + 1] == ' ':
                    level[i][j] = '1'
                elif i == 0 or level[i - 1][j] == ' ':
                    level[i][j] = '3'
                elif i + 1 == len(level) or level[i + 1][j] == ' ':
                    level[i][j] = '7'

            if level[i][j] not in 'rtlb':
                continue

            # Убираем двери там, где они не нужны
            # И строим блоки из стен на их месте с некоторым шансом
            if level[i][j] == 'r':     # ДВЕРЬ СПРАВА
                if j + 1 >= len(level[i]) or level[i][j + 1] != 'l':
                    if level[i + 2][j - 2] == level[i - 1][j - 1] == '.' and \
                            (j + 1 == len(level[i]) or level[i][j + 1] != 'F') and \
                            true_with_chance(SHORT_BLOCK_CHANCE, seed, user_seed):
                        level[i - 1][j] = '='
                        level[i + 1][j] = '9'
                        level[i][j] = ' '

                        if true_with_chance(LONG_BLOCK_CHANCE, seed, user_seed) and \
                                level[i][j - 3] == '.' == level[i - 1][j - 3]:
                            level[i][j - 1] = ' '
                            level[i - 1][j - 1] = '7'
                            level[i + 1][j - 1] = '3'
                            level[i][j - 2] = '1'
                            level[i - 1][j - 2] = '4'
                            level[i + 1][j - 2] = '6'
                        else:
                            level[i][j - 1] = '1'
                            level[i - 1][j - 1] = '4'
                            level[i + 1][j - 1] = '6'
                    else:
                        level[i][j] = level[i - 1][j] = level[i + 1][j] = '1'
                        if level[i + 2][j] == ' ':
                            level[i + 1][j] = '='
                        if level[i - 2][j] == ' ':
                            level[i - 1][j] = '9'

            elif level[i][j] == 't':     # ДВЕРЬ СВЕРХУ
                if i == 0 or level[i - 1][j] != 'b':
                    if level[i + 2][j - 1] == '.' and level[i + 1][j + 1] == '.' and \
                            (i == 0 or level[i - 1][j] != 'F') and \
                            true_with_chance(SHORT_BLOCK_CHANCE, seed, user_seed):
                        level[i][j - 1] = '9'
                        level[i][j + 1] = '0'
                        level[i][j] = ' '

                        if true_with_chance(LONG_BLOCK_CHANCE, seed, user_seed) and \
                                level[i + 3][j + 2] == '.' and level[i + 2][j - 1] == '.' and \
                                level[i + 2][j + 1] == '.':
                            level[i + 2][j] = '3'
                            level[i + 2][j - 1] = '6'
                            level[i + 2][j + 1] = '8'
                            level[i + 1][j] = ' '
                            level[i + 1][j - 1] = '1'
                            level[i + 1][j + 1] = '5'
                        else:
                            level[i + 1][j] = '3'
                            level[i + 1][j - 1] = '6'
                            level[i + 1][j + 1] = '8'
                    else:
                        level[i][j] = level[i][j - 1] = level[i][j + 1] = '3'
                        if level[i][j + 2] == ' ':
                            level[i][j + 1] = '9'
                        if level[i][j - 2] == ' ':
                            level[i][j - 1] = '0'

            elif level[i][j] == 'l':     # ДВЕРЬ СЛЕВА
                if j == 0 or level[i][j - 1] != 'r':
                    if level[i + 2][j + 2] == '.' and level[i + 1][j + 1] == '.' and \
                            (j == 0 or level[i][j - 1] != 'F') and \
                            true_with_chance(SHORT_BLOCK_CHANCE, seed, user_seed):
                        level[i - 1][j] = '-'
                        level[i + 1][j] = '0'
                        level[i][j] = ' '

                        if true_with_chance(LONG_BLOCK_CHANCE, seed, user_seed) and \
                                level[i][j + 3] == '.':
                            level[i][j + 2] = '5'
                            level[i - 1][j + 2] = '2'
                            level[i + 1][j + 2] = '8'
                            level[i][j + 1] = ' '
                            level[i - 1][j + 1] = '7'
                            level[i + 1][j + 1] = '3'
                        else:
                            level[i][j + 1] = '5'
                            level[i - 1][j + 1] = '2'
                            level[i + 1][j + 1] = '8'
                    else:
                        level[i][j] = level[i - 1][j] = level[i + 1][j] = '5'
                        if level[i + 2][j] == ' ':
                            level[i + 1][j] = '-'
                        if level[i - 2][j] == ' ':
                            level[i - 1][j] = '0'

            elif level[i][j] == 'b':     # ДВЕРЬ СНИЗУ
                if i + 1 >= len(level) or level[i + 1][j] != 't':
                    if level[i - 2][j] == level[i - 2][j + 2] == '.' and level[i][j + 2] != ' ' and \
                            (i + 1 == len(level) or level[i + 1][j] != 'F') and \
                            true_with_chance(SHORT_BLOCK_CHANCE, seed, user_seed):
                        level[i][j + 1] = '-'
                        level[i][j - 1] = '='
                        level[i][j] = ' '

                        if true_with_chance(LONG_BLOCK_CHANCE, seed, user_seed) and \
                                level[i - 3][j + 2] == '.':
                            level[i - 2][j] = '7'
                            level[i - 2][j - 1] = '4'
                            level[i - 2][j + 1] = '2'
                            level[i - 1][j] = ' '
                            level[i - 1][j - 1] = '1'
                            level[i - 1][j + 1] = '5'
                        else:
                            level[i - 1][j] = '7'
                            level[i - 1][j - 1] = '4'
                            level[i - 1][j + 1] = '2'
                    else:
                        level[i][j] = level[i][j - 1] = level[i][j + 1] = '7'
                        if level[i][j + 2] == ' ':
                            level[i][j + 1] = '='
                        if level[i][j - 2] == ' ':
                            level[i][j - 1] = '-'

    # Возвращаем созданный уровень и сид
    return [''.join(i) for i in level], seed


# Функция, возвращающая случайное булевое значение с вводящимся шансом
def true_with_chance(percentage_chance: int = 50, seed: list = None, user_seed: list = None) -> bool:
    '''
    Функция принимает целое число и переводит в коэффицент, 0 <= k <= 1.
    Затем генерирует случайное число с помощью функции рандом.
    Если случайное число меньше либо равно коэффиценту, функция возвращает True.
    Получившееся значение записывается в переданный сид (в виде числа 1 или 0, для краткости).
    :param percentage_chance: шанс выпадания значения True, в процентах
    :param seed: в сид записывается полученное значение
    :param user_seed: если пользовательский сид передан, значение берётся из него
    :return: булевое значение (True/False)
    '''
    if user_seed and seed:
        seed.append(user_seed[0])
        del user_seed[0]
    else:
        is_true = [0, 1][round(random() * 100) <= percentage_chance]
        if seed:
            seed.append(str(is_true))
        else:
            seed = [str(is_true)]
    return bool(int(seed[-1]))


def initialise_level(level_map, all_sprites, barriers_group):
    """
    В ДУШЕ НЕ....
    :param level_map: В ДУШЕ НЕ....
    :param all_sprites: Группа со всеми спрайтами
    :param barriers_group: Группа для спрайтов с тайлами, сквозь которые нельзя ходить
    """
    new_player = None
    level_map = [list(i) for i in level_map]
    monsters = []
    for y in range(len(level_map)):
        for x in range(len(level_map[y])):
            if level_map[y][x] == 'P':
                Tile('.', x, y, all_sprites)
                if true_with_chance(15):
                    Tile(choice(['.0', '.1', '.2', '.3']), x, y, all_sprites)
                # Помещаем игрока в центр текущего тайла
                new_player = Player(x * TILE_SIZE + TILE_SIZE * 0.5,
                                    y * TILE_SIZE + TILE_SIZE * 0.5,
                                    barriers_group)
                Tile(level_map[y][x], x, y, all_sprites)

            elif level_map[y][x] in 'M':
                Tile('.', x, y, all_sprites)
                if true_with_chance(15):
                    Tile(choice(['.0', '.1', '.2', '.3']), x, y, all_sprites)
                # monsters.append(Monster(x * TILE_SIZE + TILE_SIZE * 0.5,
                #                         y * TILE_SIZE + TILE_SIZE * 0.5))

            elif level_map[y][x] in 'F.':
                Tile('.', x, y, all_sprites)
                if true_with_chance(15):
                    Tile(choice(['.0', '.1', '.2', '.3']), x, y, all_sprites)

            elif level_map[y][x] == 'B':
                Tile(('B', 'B1')[true_with_chance(30)], x, y, all_sprites, barriers_group)

            elif level_map[y][x] in '1234567890-=':
                Tile(level_map[y][x], x, y, all_sprites, barriers_group)

            elif level_map[y][x] in 'rbltT':
                Tile('.', x, y, all_sprites)
                if true_with_chance(15):
                    Tile(choice(['.0', '.1', '.2', '.3']), x, y, all_sprites)
                Tile(level_map[y][x], x, y, all_sprites)

            elif level_map[y][x] != ' ':
                Tile(level_map[y][x], x, y, all_sprites)
    # вернем игрока
    return new_player, monsters
