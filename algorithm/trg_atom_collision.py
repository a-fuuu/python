
def check_same(lst):
    first_element = lst[0]
    for element in lst:
        if first_element * element < 0 :
            return False
    return True

def collision(atom_list):
    result = []

    if result == []:


if __name__ == '__main__':
    at = [100,5,4,4,-6,1,2,5]
    print(collision(at))