## Step-by-step example on [0.72, 0.17, 0.39, 0.26, 0.55, 0.81, 0.03] with 4 buckets:

# Range [0, 1) split into 4 buckets: [0, 0.25), [0.25, 0.5), [0.5, 0.75), [0.75, 1.0)

# Distribute:
#   Bucket 0 [0.00 – 0.25): [0.17, 0.03]
#   Bucket 1 [0.25 – 0.50): [0.39, 0.26]
#   Bucket 2 [0.50 – 0.75): [0.72, 0.55]
#   Bucket 3 [0.75 – 1.00): [0.81]

# Sort each bucket:
#   Bucket 0: [0.03, 0.17]
#   Bucket 1: [0.26, 0.39]
#   Bucket 2: [0.55, 0.72]
#   Bucket 3: [0.81]

# Concatenate: [0.03, 0.17, 0.26, 0.39, 0.55, 0.72, 0.81]

def bucket_sort(arr, num_buckets=None):
    if not arr:
        return arr
    
    n = len(arr)
    num_buckets = num_buckets or n

    min_val, max_val = min(arr), max(arr)
    # Avoid division by zero for uniform arrays
    range_val = (max_val - min_val) or 1

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for val in arr:
        if val == max_val:
            idx = num_buckets - 1
        
        else:
            idx = int((val- min_val) / range_val * num_buckets)
        buckets[idx].append(val)

    # Sort each bucket and collect
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))   # insersion_sort(bucket) for intergers
    return result


# Fload example (ideal use case)
floats = [0.72, 0.17, 0.39, 0.26, 0.55, 0.81, 0.03]
print(bucket_sort(floats))   # [0.03, 0.17, 0.26, 0.39, 0.55, 0.72, 0.81]

# Integer example
ints = [42, 17, 89, 23, 55, 3, 78]
print(bucket_sort(ints, num_buckets=5))  # [3, 17, 23, 42, 55, 78, 89]




# Key points:

# - Runs in O(n + N) where N is the number of buckets; approaches O(n) when N ≈ n.
# - Works best when data is uniformly distributed across a known range.
# - Performance degrades to O(n²) in the worst case if all elements land in the same bucket.