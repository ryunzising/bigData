import csv, os
import pandas as pd

##test3是经过数据清洗的成品数据集
test_csv = csv.reader(open('./test3.csv'))
df = pd.read_csv('./test3.csv')


def selectGame(gamename):  # 选择某项游戏单独制表
    out = open('%s.csv' % gamename, 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    for line in test_csv:
        if gamename in line:
            csv_write.writerow(line)


def getPlaySheet():  # success
    readCsv = csv.reader(open('./test3.csv'))
    out = open('./result/SheetWithoutPurchase.csv', 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    for line in readCsv:
        if 'purchase' not in line:
            csv_write.writerow(line)  # 删除purchase的行


def getPurchaseSheet():  # 得到购买情况表
    readCsv = csv.reader(open('./test3.csv'))
    out = open('./result/SheetWithoutPlay.csv', 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    for line in readCsv:
        if 'play' not in line:#删除play的行
            csv_write.writerow(line)


def totalPurchase():  # 计算总购买数
    df1 = pd.read_csv('./result/SheetWithoutPlay.csv')
    df_sum = df1.groupby('Name')['Value'].sum()
    df_sum.to_csv('./result/totalPurchase.csv')


def maxPurchase():  # 计算销量最高者
    df1 = pd.read_csv('./result/totalPurchase.csv')
    df1 = df1.sort_values(by='Value', ascending=False)
    print(df1)
    df1.to_csv('./result/PurchaseDescending.csv')


def totalGameTime():  # 计算总游戏时间
    df = pd.read_csv('./result/SheetWithoutPurchase.csv')
    df_sum = df.groupby('Name')['Value'].sum()
    df_sum.to_csv('./result//totalGameTimeSheet.csv')


def maxGameTime():  # 最大游戏时间
    df = pd.read_csv('./result/totalGameTimeSheet.csv')
    df1 = df.sort_values(by='Value', ascending=False)
    print(df1)
    df1.to_csv('./result/GameTimeDescending.csv')



