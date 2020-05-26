import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#Data
PurchaseDf=pd.read_csv('./result/PurchaseDescending.csv')
GameTimeDf=pd.read_csv('./result/GameTimeDescending.csv')
PurchaseName=PurchaseDf['Name'].head(5)
PurchaseRank=PurchaseDf['Value'].head(5)
GameTimeName=GameTimeDf['Name'].head(5)
GameTimeRank=GameTimeDf['Value'].head(5)
#Visualization
def Purchase():
    plt.figure(figsize=(10,10),dpi=80)
    N=5
    values=(PurchaseRank)
    index=np.arange(N)
    width=0.3
    p2=plt.bar(index,values,width,label="num",color="#87CEFA")
    plt.xlabel("Game")
    plt.ylabel("Purchase")
    plt.xticks(index,PurchaseName)
    plt.title("Top 5 purchase games in Steam")
    plt.legend(loc="upper right")
    plt.show()
def GameTime():
    plt.figure(figsize=(10, 10), dpi=80)
    N = 5
    values = (GameTimeRank)
    index = np.arange(N)
    width = 0.3
    p2 = plt.bar(index, values, width, label="num", color="#F47983")
    plt.xlabel("Game")
    plt.ylabel("Game time(hours)")
    plt.xticks(index, GameTimeName)
    plt.title("Top 5 in Steam")
    plt.legend(loc="upper right")
    plt.show()
Purchase()
GameTime()
