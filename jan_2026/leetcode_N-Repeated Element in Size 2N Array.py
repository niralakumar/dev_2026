nums= [1,2,3,4,3]
def n_repeated(list):
    sorted_list=sorted(list)
    s=0
    for i in range(1,len(sorted_list)):
        if sorted_list[i]==sorted_list[i-1]:
            s=sorted_list[i]
    return s

# def n_repeated(nums: list[int]) -> int | None:
#     """Return the element repeated N times in a 2N array, or None if not found."""
#     seen = set()
#     for x in nums:
#         if x in seen:
#             return x
#         seen.add(x)
#     return None
# print(n_repeated([1,2,3,4,3]))