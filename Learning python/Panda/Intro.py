import pandas

# Example
import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)

# output
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2


#Pandas is usually imported under the pd alias.
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

#Checking Pandas Version
import pandas as pd

print(pd.__version__)














