#dictionary sort
def dictionary_sort():
    my_dict = {
     "B" : "#1",
     "C" : "#3",
     "A" : "#5",
     "D" : "#2"
    }

    sort_dict = sorted(my_dict)
    print(sort_dict)

    for ch in sort_dict:
        print(ch, my_dict[ch])


def quick_sorting(list):
    if len(list) <= 1:
        return list

    pivot = list[-1]
    left = []
    right = []

    for x in list[:-1]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sorting(left) + [pivot] + quick_sorting(right)

def quick_sort():
    my_list = [3, 6, 8, 10, 1, 2, 1, 10, 12]
    sorted_list = quick_sorting(my_list)
    print(sorted_list)

def swap(list):
    #number of swapping
    n = 0
    #use index
    size = len(list) #count no.of elements & store in variable size
    counter = 0
    while counter < (size - 1):
        #use to iterate through the list until your reach the last number in size
        #print (list[counter+1])
        if list[counter] > list[counter+1]:
            #swap
            temp = list[counter + 1]
            #storing the value of the next element in a variable called temp.
            list[counter + 1] = list[counter]
            #swaps the next element with the current element, putting the smaller element in the correct position.
            list[counter] = temp
            #This assigns the value of temp (which was the value of the next element) to the current element, completing the swap.
            n += 1
            #print(list)
            #if no. is not greater, it skips and counter += 1
        counter += 1
    return n

def bubble_sorting(list):
    n = swap(list)
    print(list)
    while int(n) > 0:
        n = swap(list)
        print(list)

def bubble_sort():
    list1 = [6,5,7,8,9,3,4]
    print(list1)
    bubble_sorting(list1)

def run():
   #dictionary_sort()
   #quick_sort()
   bubble_sort()


def walk(steps):
    if steps == 0:
        return
    print(f"You take step #{steps}")
    walk(steps - 1)



# Optimized Python program for implementation of Bubble Sort
# Bubble Sort from website


'''def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if (swapped == False):
            break


# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")'''