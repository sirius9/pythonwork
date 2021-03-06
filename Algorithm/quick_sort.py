# -*- coding: utf-8 -*-

'''
퀵정렬
 : pivot값을 지정 후 그 값을 기준으로 정렬을 수행
 : 정렬이 되면 pivot 의 왼쪽에는 pivot값보다 작은 값이, 오른쪽에는 pivot 값보다 큰 값이 온다.
시간복잡도
 best : O(nlog(n)), worst : O(n^2)
'''


def quick_sort(arr):
    if len(arr) > 1:
        pivot = arr[len(arr) - 1]
        left, mid, right = [], [], []

        print("pivot value : " + str(pivot))
        for i in range(len(arr) - 1):
            if arr[i] < pivot:
                left.append(arr[i])

            elif arr[i] >= pivot:
                right.append(arr[i])

        print("based pivot left value : " + str(left))
        print("based pivot right value : " + str(right))

        mid.append(pivot)

        return quick_sort(left) + mid + quick_sort(right)
    else:
        return arr


if __name__ == "__main__":
    arr = [4, 1, 7, 5, 10, 9, 15, 20, 15, 30]
    print(quick_sort(arr))
