import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as spst

# 두 변수의 관계 분석(이변량 분석): 범주 -> 숫자 (범주 2개)
def eda2_nc2(data, var1, var2):
    # 수치화: t-test
    print(spst.ttest_ind(data[var1], data[var2]))

    # 시각화: barplot
    sns.barplot(x=var1, y=var2, data=data)
    plt.grid()
    plt.show()