import numpy as np
from scipy import stats

## ht 1

## Null: p-bar <= 0.56
#3 Alternate p-bar > 0.56 Business vs Business (national)

p_bar1 = 0.70
p_not1 = 0.56
q_not1 = 1 - p_not1
n = 90
alpha = 0.05

z = (p_bar1 - p_not1) / np.sqrt((p_not1 * q_not1) / n)
pval_1 = stats.norm.sf(z)


def hypthesis_1(x,y):
    if x > y:
        print("Reject the null. Bayview has a prolblem compared to the national rate of cheating with other business students.")
    else:
        print("Failed to reject the null. Business students at Bayview are okay versus their national average of cheating!")


## ht 2 

## Null: p-bar <= 0.47
#3 Alternate p-bar > 0.47 Business vs Non Business(national)

p_not2 = 0.47
q_not2 = 1 - p_not2

z2 = (p_bar1 - p_not2) / np.sqrt((p_not2 * q_not2) / n)
pval_2 = stats.norm.sf(z2)

def hypthesis_2(x,y):
    if x > y:
        print("Reject the null. Bayview has a prolblem compared to the national rate of cheating with non-business students.")
    else:
        print("Failed to reject the null. Business students are okay at Bayview compared to a national sample of non-business student cheating rates!")


hypthesis_1(pval_1, alpha)
hypthesis_2(pval_2 , alpha)


