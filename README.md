# hash_app

### xxhash

xxhash library and xxh64 method was used for this code

### Overflow Bucket Management

Overflow buckets are created when an existing bucket reaches size limit, and the string that the user inputs gets saved into a new overflow bucket having a format {bucket}-{i}.txt (where i represents the number of overlow bucket, for example 2-1.txt ). New strings always get stored into the last overflow bucket, even if previous has space.