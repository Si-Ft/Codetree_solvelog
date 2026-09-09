n = int(input())
person = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    person.append((name_value, address_value, region_value))

# Please write your code here.
person.sort()
print('name', person[-1][0])
print('addr', person[-1][1])
print('city', person[-1][2])