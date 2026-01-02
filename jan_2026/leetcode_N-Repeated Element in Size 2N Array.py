nums= [1,2,3,4,3]
def n_repeated(list):
    sorted_list=sorted(list)
    s=0
    for i in range(1,len(sorted_list)):
        if sorted_list[i]==sorted_list[i-1]:
            s=sorted_list[i]
    return s
print(n_repeated(nums))