#1. Biggie size
def biggie_size(arr):
    for i in range(0, len(arr), 1):
        if arr[i]>0:
            arr[i]="big"
    return arr
Biggie=biggie_size([-2,1,4,5,-4,-6])
print(Biggie)

#2. Count Positives
def count_positives(arr):
    counter=0
    for i in range(0, len(arr),1):
        if arr[i]>0:
            counter=counter+1
    arr[len(arr)-1]=counter
    return arr

CP=count_positives([-3,2,2,-6,1,-5,6])
print(CP)

#3. Sum total
def sum_total(arr):
    sum=0
    for i in range(0, len(arr), 1):
        sum=sum+arr[i]
    return sum
sumTotal=sum_total([-2, 3,4,5,-2])
print(sumTotal)

#4. Average
def avg(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    Avg=sum/len(arr)
    return Avg
totalofall=avg([2,3,4,5])
print(totalofall)

#5. Length
def lengthofarr(arr):
    LengthArr=0
    for i in range(len(arr)):
        LengthArr=LengthArr+1
    return LengthArr
number5=lengthofarr([4,3,5,2])
print(number5)

#6. Minimum
def minimumNum(arr):
    counter=0
    for i in range(0, len(arr),1):
        counter=counter+1
    if counter==0:
        return "false"
    smallestNumber=min(arr)
    return smallestNumber
num6=minimumNum([3,4,2,-6,-20,5])
print(num6)

#7. Return Max
def maximumNum(arr):
    counter=0
    for i in range(0, len(arr),1):
        counter=counter+1
    if counter==0:
        return "false"
    largestNumber=max(arr)
    return largestNumber
num6=maximumNum([])
print(num6)

#8. ultimate analysis
def ultAnalysis(arr):
    sumArr=0
    for i in range(len(arr)):
        sumArr=sumArr+arr[i]
    avgArr=sumArr/len(arr)
    minVal=min(arr)
    maxVal=max(arr)
    lengthArr=len(arr)
    return {'sum total':sumArr, 'average': avgArr, 'minimum': minVal, 'maximum':maxVal, 'length':lengthArr}

num8=ultAnalysis([1,2,14,24,5])
print(num8)

#9. Reverse list
def reverseList(arr):
    arr.reverse()
    return arr
num9=reverseList([1,2,3,4])
print(num9)

def beCheerful(name='', repeat=2): # set defaults when declaring the parameters
	print(f"good morning {name}\n" * repeat)
beCheerful() # output: good morning (repeated on 2 lines)
beCheerful("tim") # output: good morning tim (repeated on 2 lines)
beCheerful(name="john") # output: good morning john (repeated on 2 lines)
beCheerful(repeat=6) # output: good morning (repeated on 6 lines)
beCheerful(name="michael", repeat=5) # output: good morning michael (repeated on 5 lines)
#NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
beCheerful(repeat=3, name="kb") # output: good morning kb (repeated on 3 lines)
