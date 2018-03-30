from matplotlib import pyplot as plt
from matplotlib import pyplot as plt1
import pandas as pd
import numpy as np

data = pd.DataFrame()

data = pd.read_csv('python.csv')
print(data['terms'])

objects = ('negative','positive')
negcount = 0
poscount = 0
# neucount = 0
for item in data['terms']:
    if(item == 'neg'):
        negcount = negcount+1
    else:
        poscount=poscount+1
    # else:
    #     neucount=neucount+1
observation = [float(negcount),float(poscount)]
