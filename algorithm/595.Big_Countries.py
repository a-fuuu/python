import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    mask1 = (world.area >= 3000000) | (world.population >= 25000000)
    return world.loc[mask1, ['name', 'population', 'area']]

'''
mask를 활용하여 pandas dataframe에 filtering을 걸 수 있음
'''