import matplotlib.pyplot as plt
import seaborn as sns


# 범주형 변수의 단변량 분석
def univariate_EDA_categorical(data, var):
    # 1. 기초 통계량: 절대값과 비율
    print(data[[var]].value_counts())
    print(data[[var]].value_counts() / data.shape[0])

    # 2. 도수 분포표
    sns.countplot(x=var, data=data)
    plt.show()


# 수치형 변수의 단변량 분석
def univariate_EDA_numerical(data, var, bins=20):
    # 1. 기초 통계량
    print(data[[var]].describe().T)

    # 2. 도수 분포표
    plt.subplot(2, 1, 1)
    sns.histplot(x=var, data=data, bins=bins, kde=True)

    plt.subplot(2, 1, 2)
    sns.boxplot(x=var, data=data)
    plt.grid()

    plt.tight_layout()
    plt.show()
