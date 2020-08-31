# Layout:
# Generator and discriminator
# Generator uses random integer values to generate fake midi messages
# Discriminator is fed samples and compares them to generator results
# Penalize generator for "bad" messages.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from keras.models import Sequential

model = Sequential()
