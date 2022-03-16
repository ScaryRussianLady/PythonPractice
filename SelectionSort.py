''' 
Pseudocode for SELECTION SORT:
SELECTION_SORT(A)
  FOR i TO length(A)-1
      min ← i
      FOR j ← i + 1 TO length(A)
          IF A[j] < A[min]
              min ← j
      SWAP (A, i, min)
  RETURN A

Author: Annija Balode

Algorithm: Selection Sort
'''

#A function to execute the main steps of selection sort.
def Selection_Sort(listA):
    #Iterates over the entire list to find the minimum value.
    for i in range(len(listA)):
        minimumIndex = i
        #Then if the number next to the current value is less, set this to the new minimum value.
        for j in range(i+1, len(listA)):
            if listA[j] < listA[minimumIndex]:
                minimumIndex = j

        #Swap the elements around to sort the list (minimum value is swapped with the first value)/
        listA[i], listA[minimumIndex] = listA[minimumIndex], listA[i]

    print(listA)

listA = [45,2,1,5,7,3]
Selection_Sort(listA)
