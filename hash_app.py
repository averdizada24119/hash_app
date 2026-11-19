import xxhash
import os
import sys

n = int(sys.argv[1])
s = int(sys.argv[2])

def create_bucket(bucket, string):
    file_name=str(bucket)
    print(f"{string} added to {file_name}.txt")
    i=1
    file_path = f"{file_name}.txt" #file bucket creation
    if os.path.exists(file_path): #current size comes from the file itself
        with open(file_path, 'r') as file:
                curr_length = len(file.read())
    else:
        curr_length = 0
    
    if (curr_length + len(string) <= s): #size restriction
       with open(file_path, 'a') as file:
            file.write(string) #appending strings into files
    else:
        file_name = f"{bucket}-{i}"
        i+=1
        create_bucket(file_name, string) #overflow

while True: #EOF loop
    try:
        string = input("Please enter the string: ")

        if len(string) > s:
            print(f"String exceeds the maximum size of {s} bytes.")
            continue

        hash_object = xxhash.xxh64(string.encode())
        hash_value = hash_object.intdigest()

        bucket = hash_value%n + 1

        create_bucket(bucket, string)

    except (EOFError, KeyboardInterrupt): #exiting with ctrl+c 
        break