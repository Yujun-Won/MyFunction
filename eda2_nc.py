import matplotlib.pyplot as plt
import seaborn as sns

# 두 변수의 관계 분석(이변량 분석): 숫자 -> 범주
def eda2_nc(data, col1, col2):
    # 시각화 1: kdeplot
    plt.figure(figsize=(8, 10))
    plt.subplot(2,1,1)
    sns.kdeplot(x=col1, data=data, hue=col2, common_norm = False)

    plt.subplot(2,1,2)
    sns.kdeplot(x=col1, data=data, hue=col2, multiple='fill')
    plt.axhline(data[col2].mean(), color = 'r')
    plt.show()