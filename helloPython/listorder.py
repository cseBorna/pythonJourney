numbers = [1, 5, 6, 7, 2, 4] 
for i in range(len(numbers)):
    min=i;
    
    for j in range(i,len(numbers)):
        if (numbers[j] < numbers[min]):
            min=j;
            
    temp=numbers[i]
    numbers[i]=numbers[min]
    numbers[min]=temp
    
print(numbers)