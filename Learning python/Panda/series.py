# Pandas Series is like a column in a table and one-dimensional array holding data of any type

import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

#output

0    1
1    7
2    2
dtype: int64

#  label can be used to access a specified value
import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar[0])
#output
1

