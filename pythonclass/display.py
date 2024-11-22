def task_one(array):
    for count in range (len(array)):
        print(array[count],end=' ')
def duplicate(array):
    lst = []
    for count in range (len(array)):
        lst.append(array[count])
    for count in range (len(array)):
        print(lst.append(array[count]))
    div = len(lst)/2
    num = div + 1
    if(lst[div]==lst[num]):
        temp = lst[div]
        lst[div] = (lst[(div+1)]+lst[div])
    for count in range (len(array)):
        print(lst[count],end=' ')

def add(array,lst):
    for count in range (0,3,len(array)):
        lst.append(array[count])
    return lst
def add2(lst):
    div = len(lst) / 2
    sum = lst[0] + lst[div] + lst[len(lst)]
    return sum




