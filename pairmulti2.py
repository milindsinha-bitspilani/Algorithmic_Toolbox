def max_pairwise_product(n, numbers):
        max_index=-1
        max=0
        for i in range(0,n):
            if numbers[i]>=max:
                max_index=i
                max=numbers[i]
        max_index2=-1
        max=0
        for i in range(0,n):
            if numbers[i]>=max and i!=max_index:
                max_index2=i
                max=numbers[i]
        return numbers[max_index]*numbers[max_index2]
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_n, input_numbers))
