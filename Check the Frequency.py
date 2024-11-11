test={'codingal':2,'is':2,'the':2,'best':2,'for':2,'coding':1}
print(str(test))
K=2
res=0
for key in test:
    if (test[key]==K):
        res=res+1
print(K)
print("the frequency of K is:",res)