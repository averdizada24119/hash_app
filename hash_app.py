import xxhash
import os
import sys

n = int(sys.argv[1])
s = int(sys.argv[2])

while True: #EOF loop
    try:
        string = input("Please enter the string: ")
        hash_object = xxhash.xxh64(string.encode())
        hash_value = hash_object.intdigest()

        bucket = hash_value%n + 1

        print(f"{string} added to {bucket}.txt")

        file_path = f"{bucket}.txt" #file bucket creation
        if os.path.exists(file_path): #current size comes from the file itself
            with open(file_path, 'r') as file:
                curr_length = len(file.read())
        else:
            curr_length = 0

        if (curr_length + len(string) <= s): #size restriction
            with open(file_path, 'a') as file:
                file.write(string) #appending strings into files

    except (EOFError, KeyboardInterrupt): #exiting with ctrl+c 
        break