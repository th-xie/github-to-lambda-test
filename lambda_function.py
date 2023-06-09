import pandas as pd
#from datetime import *

def lambda_handler(event, context):
    d = {'col1' : [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1')
    print('tTry something else')
