import xxhash

string = input("Please enter the string: ")

hash_object = xxhash.xxh64(string.encode())

print('Hash object:', hash_object)

#xxhash is the library, xxh64 is function inside the library that creates HASH OBJECT from data
#encode() method converts string into bytes.

hash_value = hash_object.intdigest()
print('Number representation of the hash object:', hash_value)

n = int(input('Bucket amount: '))
print('The object is inside bucket', hash_value%n)

#conceptual bucket rearranging