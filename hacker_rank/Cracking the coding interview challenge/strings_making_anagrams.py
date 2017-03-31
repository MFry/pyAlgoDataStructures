def number_needed(a, b):
    histogram_a, histogram_b = {}, {}
    for c in a:
        if c in histogram_a:
            histogram_a[c] += 1
        else:
            histogram_a[c] = 1
    for c in b:
        if c in histogram_b:
            histogram_b[c] += 1
        else:
            histogram_b[c] = 1
    all_bins = set(histogram_a.keys()).union(histogram_b.keys())
    diffs = 0
    for key in all_bins:
        val_a, val_b = 0, 0
        if key in histogram_a:
            val_a = histogram_a[key]
        if key in histogram_b:
            val_b = histogram_b[key]
        diffs += abs(val_a - val_b)
    return diffs


a = input().strip()
b = input().strip()

print(number_needed(a, b))