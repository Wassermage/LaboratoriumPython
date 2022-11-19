# Zadanie 4

nums = []
nums.append(float(input("Podaj x: ")))
nums.append(float(input("Podaj y: ")))
nums.append(float(input("Podaj z: ")))

nMax = nums[0]
nMin = nums[0]

for n in nums:
    if n > nMax:
        nMax = n
    elif n < nMin:
        nMin = n

print(nums)
print(f"min: {nMin}")
print(f"max: {nMax}")
