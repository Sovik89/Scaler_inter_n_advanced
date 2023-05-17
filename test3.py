from functools import cmp_to_key

array=[  [1, 2, 50],[3, 5, 20],[2, 100, 200],[6, 19, 100]  ]


array=sorted(array,key=lambda x:x[1])


print(array)