
assending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]

sound = list(map(int , input().strip().split()))

if sound == assending:
    print("ascending")
elif sound == descending:
    print("descending")
else:
    print("mixed")
    
