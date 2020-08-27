import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from MagentaParser import MagentaParser

parsed = MagentaParser('songs/')
parsed.parse()
