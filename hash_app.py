import xxhash

n = int(input('Bucket amount: '))
s = int(input('Size of a bucket: '))
for i in range(n): #creating n buckets [temporary as a string]
    globals()[f"b{i}"] = ""

stop = 0
while True: #EOF loop
    try:
        string = input("Please enter the string: ")
        hash_object = xxhash.xxh64(string.encode())
        hash_value = hash_object.intdigest()

        bucket = hash_value%n

        print('String arranged into bucket', bucket)

        if (len(globals()[f"b{bucket}"]) + len(string) <= s): #size restriction
            globals()[f"b{bucket}"] += string #appending string into corresponding bucket
    except EOFError :
        break

for i in range(n):
    print(i, globals()[f"b{i}"])