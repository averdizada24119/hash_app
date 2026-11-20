import xxhash
import os
import sys

n = int(sys.argv[1])
s = int(sys.argv[2])

while True: #EOF loop
    try:
        string = input("Please enter the string: ")

        if len(string) > s:
            print(f"String exceeds the maximum size of {s} characters.")
            continue

        hash_object = xxhash.xxh64(string.encode())
        hash_value = hash_object.intdigest()

        bucket = hash_value%n + 1

        i=0
        file_name=f"{bucket}"
        while os.path.exists(f"{bucket}-{i+1}.txt"): #walk the chain to the last file
            i+=1
            file_name=f"{bucket}-{i}"

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
            i+=1
            file_name=f"{bucket}-{i}"
            file_path = f"{file_name}.txt"
            with open(file_path, 'a') as file:
                file.write(string)
        
        print(f"{string} added to {file_name}.txt")

    except (EOFError, KeyboardInterrupt): #exiting with ctrl+c 
        break