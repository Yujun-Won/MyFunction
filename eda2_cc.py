import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as spst
from statsmodels.graphics.mosaicplot import mosaic

# 두 변수의 관계 분석(이변량 분석): 범주 -> 범주
def eda2_cc(data, col1, col2):
    # 수치화: crosstab
    table = pd.crosstab(data[col1], data[col2])
    print(table)
    print('-' * 50)
    
    # 시각화 1: 모자이크
    mosaic(data, [col1, col2])
    plt.axhline(1- data[col2].mean(), color = 'r')
    
    # 시각화 2: Stacked bar
    temp = pd.crosstab(data[col1], data[col2], normalize = 'index')
    temp.plot.bar(stacked=True)
    plt.axhline(1-data[col2].mean(), color = 'r')
    plt.xticks(rotation=0)
    plt.show()