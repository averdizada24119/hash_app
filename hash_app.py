import xxhash

n = int(input('Bucket amount: '))
s = int(input('Size of a bucket: '))
for i in range(1, n+1):
    globals()[f"b{i}"] = ""

for i in range(1, n+1):
    file_path = f"{i}"
    with open(file_path, 'w') as file:
        file.write('')

while True: #EOF loop
    try:
        string = input("Please enter the string: ")
        hash_object = xxhash.xxh64(string.encode())
        hash_value = hash_object.intdigest()

        bucket = hash_value%n + 1

        print('String arranged into bucket', bucket)

        if (len(globals()[f"b{bucket}"]) + len(string) <= s): #size restriction
            globals()[f"b{bucket}"] += string #appending string into corresponding bucket
            with open(f"{bucket}", 'w') as file:
                file.write(globals()[f"b{bucket}"])

    except EOFError :
        break

for i in range(1, n+1):
    print(i, globals()[f"b{i}"])