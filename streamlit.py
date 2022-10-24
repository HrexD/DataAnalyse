import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
#import numpy as np
import warnings
import streamlit as st

warnings.filterwarnings('ignore')

df=pd.read_csv(r'.\Twitch_game_data.csv',encoding='cp1252')
df