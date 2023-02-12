import matplotlib.pyplot as plt
import seaborn as sns

# 범주형 변수의 단변량 분석
def eda1_c(data, var):
    # 기초 통계량: 절대값과 비율
    print(data[[var]].value_counts())
    print(data[[var]].value_counts()/data.shape[0])

    # 도수 분포표
    sns.countplot(x=var, data=data)
    plt.show()