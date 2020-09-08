def is_isogram(n):
    n1 = [element.lower() for element in n] ; n
    a = 0
    for a in range(0,len(n)):
        if n1.count(n1[a]) > 1 :
            return False            
        a = a + 1
    return True    








print(is_isogram('moOse'))      
        