import pandas as pd
# Creating series from list
ex_list = ['a',1,3,5,'c','d']
ex_series = pd.Series(ex_list)
print(ex_series)
# Creating dataframe from list of list
ex_list_of_list = [[1  , 'a', 'b' , 'c'],
                   [2.5, 'd', 'e' , 'f'],
		           [5  , 'g', 'h' , 'i'],
		           [7.5, 'j', 10.5, 'l']]
index = ['dq', 'lab', 'kar', 'lan']
cols = ['float', 'char', 'obj', 'char']
ex_df = pd.DataFrame(ex_list_of_list, index=index, columns=cols)
print(ex_df)