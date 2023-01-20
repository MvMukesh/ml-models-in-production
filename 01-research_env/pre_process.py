#for preprocessing

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class TemporalVariableTransformer(BaseEstimator, TransformerMixin):
    #Temporal elapsed time transformer
    def __init__(self, variables, reference_variable):
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        self.variables = variables
        self.reference_variable = reference_variable

    def fit(self, X, y=None):
        #need this step to fit sklearn pipeline
        return self

    def transform(self, X):
        #protect from over-write original dataframe
        X = X.copy()        
        for feature in self.variables:
            X[feature] = X[self.reference_variable] - X[feature]
        return X

# categorical missing value imputer
class Mapper(BaseEstimator, TransformerMixin):
    def __init__(self, variables, mappings):
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        self.variables = variables
        self.mappings = mappings

    def fit(self, X, y=None):
        # will need fit statement to accomodate sklearn pipeline
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.mappings)
        return 