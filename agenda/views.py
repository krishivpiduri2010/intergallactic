from django.shortcuts import render
from .models import Object


# Create your views here.
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j].to_time < arr[j + 1].from_time:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def home(request):
    arr=[]
    for obj in Object.objects.all():
        arr.append(obj)
    print(arr)
    bubbleSort(arr)
    return render(request, 'agenda/home.html',{'agenda':arr})
