tamanho = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
soma = 0
consegue = True
for i in range(tamanho):
    if(soma < nums[i] - 1):
        print(soma + 1)
        consegue = False
        break
    soma += nums[i]
if(consegue):
    print(sum(nums) + 1)