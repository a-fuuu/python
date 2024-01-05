import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask1 = (products.low_fats == 'Y') & (products.recyclable == 'Y')
    return products.loc[mask1, ['product_id']]

'''
pandas dataframe 에서 .loc 메소드를 활용하여 컬럼 선택을 하기 위해서는 [] 안에 string 형태로 열 이름을 넣어야한다.
'''