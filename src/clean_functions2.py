import numpy as np
import pandas as pd



def featuring_cleaning(data):

    """1 - Drops "id" column from dataframe.
       2 - Convert categorial columns to numerical values "get_dummies".
       3 - Replace "x", "y", "z" zero values by "cut", "color","clarity" median.
       4 - Creates a new column named "volume" which is the multiplication of x, y and z.
       5 - Drops "x", "y", "z" "table" and "depth" columns.
    """
    

    diamond_df = data.drop(["id"], axis=1)

    diamond_df["z"] = diamond_df.groupby(["cut", "color","clarity"])["z"].apply(lambda x: x.replace(0, x.median()))
    diamond_df["x"] = diamond_df.groupby(["cut", "color","clarity"])["x"].apply(lambda x: x.replace(0, x.median()))
    diamond_df["y"] = diamond_df.groupby(["cut", "color","clarity"])["y"].apply(lambda x: x.replace(0, x.median()))
    diamond_df['volume'] = diamond_df['x']*diamond_df['y']*diamond_df['z']
    # diamond_df = diamond_df.drop(["x", "y", "z"], axis=1)
    diamond_df = diamond_df.drop(["table","depth"], axis=1)
    diamond_df = pd.get_dummies(diamond_df, drop_first=True)
    return diamond_df

  
    