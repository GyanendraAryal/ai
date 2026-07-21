import pandas as pd
dd = pd.read_clipboard("../datasets/daraz_dataset.csv")
print(dd)



# print(dd[(dd["Category"]=="Electronics") & (dd["Rating"]==5)])
