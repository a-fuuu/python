'''
배열을 입력받아 output[i]가 
자신을 제외한 나머지 수들의 곱이 되도록 하여 출력하시오
나눗셈을 하지말고 O(n) 으로 풀이하시오
'''

def product_except_self(num_arr : list):
    right_prod = []
    
    acml_prod = 1
    for num in num_arr:
        right_prod.append(acml_prod)
        acml_prod = acml_prod * num
    
    acml_prod = 1
    for i in range(len(num_arr) - 1, 0 - 1, -1):
        right_prod[i] = right_prod[i] * acml_prod
        acml_prod = acml_prod * num_arr[i]
        
    
    return right_prod

if __name__ == '__main__':
    print(product_except_self([1,2,3,4,5]))