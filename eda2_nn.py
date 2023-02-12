import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as spst

# 두 변수의 관계 분석(이변량 분석): 숫자 -> 숫자
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