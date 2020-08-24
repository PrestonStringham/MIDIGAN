import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from Parser import Parser

parsed = Parser('songs/')
parsed.parse()
