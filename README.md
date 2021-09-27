# Diamonds Price prediction


<img src="https://www.cornel1801.com/videosong/Gentlemen-Prefer-Blondes-Diamonds-Are-a-Girl-s-Best-Friend/1.jpg" width="900" height="600">


### Objective


Diamonds price prediction based on their cut, colour, clarity & other attributes with machine learning using Python programming language.
 
I have used a Diamonds dataset which contains the prices and other attributes of almost 54,000 diamonds. The dataset contains 10 variables. These are the variables:

- **Price** is in US dollars
- **Carat** weight of the diamond
- **Cut** quality of the cut (Fair, Good, Very Good, Premium, Ideal)
- **color** diamond colour, from J (worst) to D (best)
- **clarity** a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))
- **x** length in mm
- **y** width in mm
- **z** depth in m
- **depth:** The height of a diamond
- **table:** The width of the diamond’s table expressed as a percentage of its average diameter



### Methods


- Exploratory data analysis (EDA)
- Featuring engineering
- Train & test model


### STEPS

-  **1 - Exploring_Features.ipynb**:

    - Explores correlation between variables.
    - Explores missing and zero values of each variable
    - Explores more in depth correlation between each categorical variable and price variable using   boxplots
       




- **2 - Feature_engineering.ipynb**: 

    - Drops "id" column from dataframe.
    - Converts categorial columns to numerical values "get_dummies".
    - Replaces "x", "y", "z" zero values by "cut", "color","clarity" median.
    - Creates a new column named "volume" which is the multiplication of x, y and z.
    - Drops "x", "y", "z" "table" and "depth" columns.



- **3 - Modelling_Algorithms**:

   - Scales variables.
   - Prepares dataset for training.
   - Creates correspodent regressor model.
   - Trains the model to fit data
   - Test the model on validation data


<img src="https://github.com/maria-luisa-gomez/diamond_prices/blob/main/images/diamond_price_pred.png" width="900" height="500">



## Libraries


[seaborn](https://seaborn.pydata.org)

[matplotlib](https://matplotlib.org)

[scikit-learn](https://scikit-learn.org/stable/)

[get_dummies](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)

[StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

[train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

[GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)

[LinearRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

[DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html)

[RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)

[GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html)

[KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html)

[Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html)

