import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

files = os.listdir('parsed_songs')

df = pd.read_csv('parsed_songs/' + files[0])

print(df.head)