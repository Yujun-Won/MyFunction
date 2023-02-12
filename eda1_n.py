import matplotlib.pyplot as plt
import seaborn as sns

# 수치형 변수의 단변량 분석
def eda1_n(data, var, bins=20):
    # 기초 통계량
    print(data[[var]].describe().T)

    # 도수 분포표
    plt.subplot(2, 1, 1)
    sns.histplot(x=var, data=data, bins=bins, kde=True)

    plt.subplot(2, 1, 2)
    sns.boxplot(x=var, data=data)
    plt.grid()

    plt.tight_layout()
    plt.show()