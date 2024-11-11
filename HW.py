dict={"Codingal":3,'is':5,'the':9,'best':7,'for':8,'coding':1}
K=int(input("Enter a value between 1 and 9:"))
res=0
for key in dict:
    if (dict[key]==K):
        res=res+1
print(K)
print("the frequency of K is:",res)