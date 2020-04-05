import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plotFig(name):
    data = pd.read_csv("./version-0" + str(name) +  "-acc.csv")

    a = data["epoch"]
    b = data["loss"]
    c = data["train-acc"]
    d = data["test-acc"]
    m = d/c

    fig,ax2 = plt.subplots()
    ax1 = ax2.twinx()           # 做镜像处理
    lc, = ax1.plot(a,c,'g-')
    ld, = ax1.plot(a,d,'r-')
    lb, = ax2.plot(a,b,'b-')
    mm, = ax1.plot(a,m,color='coral')
     
    ax1.set_xlabel('epoch')     #设置x轴标题
    ax1.set_ylabel('acc')       #设置Y1轴标题
    ax2.set_ylabel('loss')      #设置Y2轴标题

    plt.legend(handles = [lb, lc, ld, mm], labels = ['loss', 'train-acc','test-acc', 'test/train'], bbox_to_anchor=(1.7 ,0.95))
    fig.subplots_adjust(right=0.6)  # 解决图例显示不完全
    plt.savefig("./version-0" + str(name) +  "-acc.jpg", dpi=600, box_inches='tight')
    # plt.show()
    
# 手动调版本范围
for i in range(5, 6):
    plotFig(i)