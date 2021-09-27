import numpy as np
import pandas as pd


def featuring_cleaning(data):
    """1 - Drops "id" column from dataframe.
       2 - Converts categorial columns to numerical values (manually).
       3 - Replaces "x", "y", "z" zero values by "cut", "color","clarity" median.
       4 - Creates a new column named "volume" which is the multiplication of x, y and z.
       5 - Drops "x", "y", "z" "table" and "depth" columns.
    """

    # Feature Encoding (handmade)
    dic_cut = {
    'Premium': 5,
    'Very Good': 4,
    'Good': 3,
    'Fair': 2,
    'Ideal': 1,}


    dic_color = {
        'D': 2,
        'E': 1,
        'G': 3,
        'F': 4,
        'H': 5,
        'I': 6,
        'J': 7,}


    dic_clarity = {
        'SI2': 8,
        'I1': 7,
        'VS2': 6,
        'VS1': 5,
        'SI1': 4,
        'VVS2': 3,
        'VVS1': 2,
        'IF':1}


    # diamond_df = data
    diamond_df = data.drop(["id"], axis=1)
    diamond_df.cut = diamond_df.cut.map(dic_cut)
    diamond_df.color = diamond_df.color.map(dic_color)
    diamond_df.clarity = diamond_df.clarity.map(dic_clarity)
    diamond_df["z"] = diamond_df.groupby(["cut", "color","clarity"])["z"].apply(lambda x: x.replace(0, x.median()))
    diamond_df["x"] = diamond_df.groupby(["cut", "color","clarity"])["x"].apply(lambda x: x.replace(0, x.median()))
    diamond_df["y"] = diamond_df.groupby(["cut", "color","clarity"])["y"].apply(lambda x: x.replace(0, x.median()))
    diamond_df['volume'] = diamond_df['x']*diamond_df['y']*diamond_df['z']
    diamond_df = diamond_df.drop(["x", "y", "z"], axis=1)
    diamond_df = diamond_df.drop(["table","depth"], axis=1)
    return diamond_df


  
    # dic_cut = {
    # 'Premium': 5,
    # 'Very Good': 4,
    # 'Good': 3,
    # 'Fair': 2,
    # 'Ideal': 1,}


    # dic_color = {
    #     'D': 2,
    #     'E': 1,
    #     'G': 3,
    #     'F': 4,
    #     'H': 5,
    #     'I': 6,
    #     'J': 7,}


    # dic_clarity = {
    #     'SI2': 8,
    #     'I1': 7,
    #     'VS2': 6,
    #     'VS1': 5,
    #     'SI1': 4,
    #     'VVS2': 3,
    #     'VVS1': 2,
    #     'IF':1}