import xxhash

n = int(input('Bucket amount: '))
#s = int(input('Size of a bucket: '))
for i in range(n): #creating n buckets [temporary as a list]
    globals()[f"b{i}"] = []

stop = 0
while (not stop): #temporary EOF alternative
    string = input("Please enter the string: ")
    hash_object = xxhash.xxh64(string.encode())
    hash_value = hash_object.intdigest()

    bucket = hash_value%n

    print('String arranged into bucket', bucket)
    globals()[f"b{bucket}"].append(string) #appending string into corresponding bucket

    stop=input('Stop? ') #type to exit/enter to continue

for i in range(n):
    print(i, globals()[f"b{i}"])