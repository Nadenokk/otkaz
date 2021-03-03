f=open('nn.txt','r')
for line in f:
    nums = line.replace("\n",";")
    print(nums, end=' ')