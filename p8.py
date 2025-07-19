def edit_distance(s1, s2):
    m = len(s1) + 1
    n = len(s2) + 1
    dist = {}

    # Initialize the first column
    for i in range(m):
        dist[i, 0] = i

    # Initialize the first row (✅ Corrected)
    for j in range(n):
        dist[0, j] = j

    # Fill in the distance table
    for i in range(1, m):
        for j in range(1, n):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 2
            dist[i, j] = min(
                dist[i, j - 1] + 1,     # insertion
                dist[i - 1, j] + 1,     # deletion
                dist[i - 1, j - 1] + cost  # substitution
            )

    return dist[m - 1, n - 1]

# Test
print(edit_distance("medium", "enum"))
