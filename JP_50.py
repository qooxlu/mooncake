from random import randint
from time import sleep
from os import system

letter = ['あ', 'い', 'う', 'え', 'お', 
    'か', 'き', 'く', 'け', 'こ', 
    'さ', 'し', 'す', 'せ', 'そ', 
    'た', 'ち', 'つ', 'て', 'と', 
    'な', 'に', 'ぬ', 'ね', 'の', 
    'は', 'ひ', 'ふ', 'へ', 'ほ', 
    'ま', 'み', 'む', 'め', 'も', 
    'や', 'ゆ', 'よ', 
    'ら', 'り', 'る', 'れ', 'ろ', 
    'わ', 'を',
    'ん']

letter1 = ['ア', 'イ', 'ウ', 'エ', 'オ',
    'カ', 'キ', 'ク', 'ケ', 'コ',
    'サ', 'シ', 'ス', 'セ', 'ソ',
    'タ', 'チ', 'ツ', 'テ', 'ト',
    'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
    'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
    'マ', 'ミ', 'ム', 'メ', 'モ',
    'ヤ', 'ユ', 'ヨ',
    'ラ', 'リ', 'ル', 'レ', 'ロ',
    'ワ', 'ヲ',
    'ン']

u = ['a', 'i', 'u', 'e', 'o',
    'ka', 'ki', 'ku', 'ke', 'ko',
    'sa', 'si', 'su', 'se', 'so',
    'ta', 'ti', 'tu', 'te', 'to',
    'na', 'ni', 'nu', 'ne', 'no',
    'ha', 'hi', 'hu', 'he', 'ho',
    'ma', 'mi', 'mu', 'me', 'mo',
    'ya', 'yu', 'yo',
    'ra', 'ri', 'ru', 're', 'ro',
    'wa', 'wo',
    'nn']

class CHpro():
    def __init__(self):
        self.left_counts = len(u)
        self.cha_list = [i for i in range(self.left_counts)]
        self.false = {}
        self.this_index = 0
        self.tend = '1'
    
    def print_50(self):
        for i in range(len(duan)):
            print('\n%s段: \n平假名\t片假名\t罗马音\n' % duan[i], "\n ".join(letter[j] + '\t' + letter1[j] + '\t' + u[j] for j in range(fend[i][0], fend[i][1])))
        input('请按任意键并回车后开始')
        system("cls")

    def project(self):
        # time.sleep(1)
        print('请输入该符号的发音: ', self.letter[self.this_index])
        user_type = input()
        # user_type = 'a'
        if user_type == u[self.this_index]:
            print('答案是: ', u[self.this_index])
            # time.sleep(1)
            print('您的回答正确!\n当前还有%d次机会' % self.life)

            self.cha_list.remove(self.this_index)
            self.left_counts -= 1
            if self.left_counts != 0:
                print('还剩下%d个发音' % self.left_counts)
        else:
            self.life -= 1
            if letter[self.this_index] +'\t'+ letter1[self.this_index] +'\t'+ u[self.this_index] in self.false:
                self.false[letter[self.this_index] +'\t'+ letter1[self.this_index] +'\t'+ u[self.this_index]] += 1
            else:
                self.false[letter[self.this_index] +'\t'+ letter1[self.this_index] +'\t'+ u[self.this_index]] = 1
            if self.life >= 1:
                print('回答错误!!!')
                # time.sleep(1)
                print('正确答案是: %s\n您当前有%d次机会' % (u[self.this_index], self.life))
                print('还剩下%d个发音' % self.left_counts)
            else:
                print('回答错误!!!')
                # time.sleep(0.3)
                print('正确答案是: %s' % u[self.this_index])
                # time.sleep(1)
                print('***\n你太菜了!!!\n***')
                # self.false = list(dict.fromkeys(self.false))
                print('所有的错误的发音为:\n平假名\t片假名\t罗马音\t错误次数')
                print("\n".join("{}\t{}".format(k, v) for k, v in self.false.items()))
                input("请按任意键并回车来继续")
        return
        
    def run(self):
        index = randint(0, self.left_counts - 1)
        self.this_index = self.cha_list[index]
        self.project()
        return

    def start(self):
        while self.life > 0:
            if self.left_counts > 0:
                self.run()
            else:
                if self.false == {}:
                    print('***\n侥幸全对!!!\n***')
                    self.tend = input("重新开始请输入1, 或者按任意键后回车退出")
                else:
                    print('***\n侥幸通过!!!\n***')
                    print('所有的错误的发音为:\n平假名\t片假名\t罗马音\t错误次数')
                    print("\n".join("{}\t{}".format(k, v) for k, v in self.false.items()))
                    self.tend = input("重新开始请输入1, 或者按任意键后回车退出")
                break
        else:
            self.tend = input('重新开始请输入1, 或者按任意键后回车退出')

    def re_choose(self):
        re_choose = True
        while re_choose:
            a = input('平假名请输入\'1\', 片假名请输入\'2\'')
            if a == '2':
                re_choose = False
                self.letter = letter1
            elif a == '1':
                re_choose = False
                self.letter = letter
            else:
                print('请仔细审题!!!')
        
    def re_chance(self):
        re_chance = True
        while re_chance:
            is_number = 1
            while is_number:
                life = input("你想要多少次机会, 请输入0~5内的整数:")
                try:
                    life = int(life)
                    is_number = 0
                except ValueError:
                    print('请输入数字!')
            if life < 0:
                print('不能是负数!!!')
            elif life > 5 and life != 46:
                print('次数太多啦!!!')
            elif life == 46:
                print('好叭')
                re_chance = False
            else:
                re_chance = False
        self.life = life
        # time.sleep(3)
            
            # sleep(2)
            # print('(σ｀д′)σ电脑爆炸倒计时: ')
            # for i in range(10, 0, -1):
            #     sleep(1)
            #     print(i)
            # sleep(1)
            # print('┗|｀O′|┛ 嗷~~')
            # sleep(2)

    def start_all(self):
        while self.tend == '1':
            self.tend_y = input('若需要看五十音图, 请输入1并回车, 否则请按任意键并回车')
            if self.tend_y:
                if self.tend_y == '1':
                    self.print_50()
            self.re_choose()
            self.re_chance()
            print('准备',)
            sleep(0.2)
            print('开始!')
            self.start()
    
print('这是一个辅助学习日语五十音图的程序')
print('作者: 昔笔小新')
print('请勿外传')

fend = [[0, 5], [5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35], [35, 38], [38, 43], [43, 45], [45, 46]]
# fend = [[0, 5], [5, 6]]
duan = ['a', 'k', 's', 't', 'n', 'h', 'm', 'y', 'r', 'w', '助词']
# duan = ['a', '助词']

# time.sleep(1)
print('视频推荐: https://www.bilibili.com/video/BV1Yk4y1y7K5')
input("请按下任意按键后回车来开始...")
# time.sleep(2)

GAME = CHpro()
GAME.start_all()