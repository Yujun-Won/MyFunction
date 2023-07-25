import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as spst
from statsmodels.graphics.mosaicplot import mosaic


# 두 변수의 관계 분석(이변량 분석): 숫자 → 숫자
def eda2_nn(data, var1, var2):
    # 수치화: 상관분석
    print(spst.pearsonr(data[var1], data[var2]))

    # 시각화: 산점도
    plt.subplot(1, 2, 1)
    sns.scatterplot(x=var1, y=var2, data=data)

    plt.subplot(1, 2, 2)
    sns.regplot(x=var1, y=var2, data=data)

    plt.tight_layout()
    plt.show()


# 두 변수의 관계 분석(이변량 분석): 숫자 → 범주
def eda2_nc(data, col1, col2):
    # 시각화 1: kdeplot
    plt.figure(figsize=(8, 10))
    plt.subplot(2, 1, 1)
    sns.kdeplot(x=col1, data=data, hue=col2, common_norm=False)

    plt.subplot(2, 1, 2)
    sns.kdeplot(x=col1, data=data, hue=col2, multiple='fill')
    plt.axhline(data[col2].mean(), color='r')
    plt.show()


# 두 변수의 관계 분석(이변량 분석): 범주 → 범주
def eda2_cc(data, col1, col2):
    # 수치화: crosstab
    table = pd.crosstab(data[col1], data[col2])
    print(table)
    print('-' * 50)

    # 시각화 1: 모자이크
    mosaic(data, [col1, col2])
    plt.axhline(1 - data[col2].mean(), color='r')

    # 시각화 2: Stacked bar
    temp = pd.crosstab(data[col1], data[col2], normalize='index')
    temp.plot.bar(stacked=True)
    plt.axhline(1-data[col2].mean(), color='r')
    plt.xticks(rotation=0)
    plt.show()
