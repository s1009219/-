Ｘ = [5,1,4,8,7,3,2]
print("Element X[2] = ", X[2])
print()

# 新增了一個元素 : 6
X.append(6)
print(X)
print()

# 我們把 X[4] 也就是 7 給刪除
# 把 X[4] 之後的都往前移動
for i in range(5,len(X)):
    X[i-1] = X[i]
print(X)
# 再把最後一個給刪除
X.pop(-1)
print(X)
print()

# 複製 X 給 Y
Y = []
for ele in X:
    Y.append(ele)
print(Y)
print()

