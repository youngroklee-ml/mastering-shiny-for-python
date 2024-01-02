import pandas as pd
from plotnine import ggplot, geom_freqpoly, aes, coord_cartesian
from scipy.stats import ttest_ind
import numpy as np

def freqpoly(x1, x2, binwidth=0.1, xlim=(-3, 3)):
    df = pd.DataFrame({
        "x": np.concatenate([x1, x2]),
        "g": ["x1"] * len(x1) + ["x2"] * len(x2)
    })

    res = (ggplot(df, aes("x", colour="g"))
           + geom_freqpoly(binwidth=binwidth, size=1)
           + coord_cartesian(xlim=xlim))
    
    return res

def t_test(x1, x2):
    test = ttest_ind(x1, x2)
    return f"p value: {test.pvalue:.3f}\n[{test.confidence_interval().low:.2f}, {test.confidence_interval().high:.2f}]"

x1 = np.random.normal(0, 0.5, size=100)
x2 = np.random.normal(0.15, 0.9, size=200)

freqpoly(x1, x2)
print(t_test(x1, x2))

