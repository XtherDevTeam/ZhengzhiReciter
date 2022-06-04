# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import difflib
import json

import requests

import Pickers
import Source
import sys
import os

MeaninglessWords = ['，', '。', '：', '、', '！', '（', '）', ',', '.', ':', '!', '(', ')', '*', '`']
ErrorCount = 0


def SayHelloToUser():
    Response = requests.get('https://v1.hitokoto.cn/?c=a')
    Response = json.loads(Response.content.decode(encoding='utf-8'))
    print("早安，内卷人！")
    try:
        print(f"{Response['hitokoto']} -- {Response['from']}")
        return "Done"
    except Exception as e:
        return str(e)


def Check(s1, s2):
    for Word in MeaninglessWords:
        s1.replace(Word, '')
        s2.replace(Word, '')
    return 1 - difflib.SequenceMatcher(None, s1, s2).quick_ratio()


def Recite(Problems, PickerFunc):
    global ErrorCount
    Picked = 0
    for r in range(len(Problems)):
        Picked = PickerFunc(len(Problems), Picked)
        WholeProblemPercent = 1

        while WholeProblemPercent >= 0.2:
            print('--- 现在是', r + 1, '/', len(Problems), '个问题 ---')
            print('当前问题: ' + Problems[Picked - 1]['title'])
            print('答案为:')
            for Point in Problems[Picked - 1]['points']:
                print('-', Point)
            print('\n')
            input('(背诵完成后按任意键继续)')

            for NMSL in range(1145):
                print('\n')

            print('--- 现在是', r + 1, '/', len(Problems), '个问题 ---')
            print('当前问题: ' + Problems[Picked - 1]['title'])
            print('请回答:')

            FellPoints = 0

            for Point in Problems[Picked - 1]['points']:
                Text = input('- ')
                Percent = Check(Point, Text)
                print('此点错误率为', Percent * 100)
                if Percent > 0.2:
                    FellPoints += 1

            WholeProblemPercent = FellPoints / len(Problems[Picked - 1]['points'])
            print('此问题错误率为', WholeProblemPercent)
            if WholeProblemPercent >= 0.2:
                ErrorCount += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Result = []

    print('蒸痔背书硝铸獸 Developed by Jerry Chou')
    print('-----------------------------------')
    SayHelloToUser()
    print('-----------------------------------')
    print('请拖入 知识点源文件(Markdown) 或粘贴 文件的路径 至程序，当输入完成时键入 End 以退出输入')
    print('(文件名) ', end='')
    for line in sys.stdin:
        if line == 'End\n':
            break

        Temp = Source.LoadSource(line[0:-1])
        for i in Temp:
            print('导入知识点 ', i['title'], ' 成功!')
            Result.append(i)
        print('成功从 ', line[0:-1], ' 中导入 ', len(Temp), ' 个知识点!')
        print('(文件名) ', end='')

    print('-----------------------------------')
    print('知识点导入完成! 当前题库共有', len(Result), '个知识点')

    print('请选择默写模式:')
    print('1 - 按题目顺序进行默写')
    print('2 - 随机抽取题目进行默写')

    Input = int(input('(模式编号) '))

    Picker = Pickers.OrderPicker
    match Picker:
        case 1:
            Picker = Pickers.OrderPicker
        case 2:
            Picker = Pickers.RandomPicker

    Recite(Result, Picker)

    input('(背诵任务完成)')
