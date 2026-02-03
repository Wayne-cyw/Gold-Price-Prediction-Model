"""
Gold Price Prediction model using Random Forest Regressor.
This script loads gold price data, preprocesses it, trains a Random Forest Regressor model,
and evaluates its performance on a test dataset.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics


