def min_size(N, W,H):   # N - the number of leaves W - Width of leaf H - height of leaf
    if not 1 <= N <= 1012 or not 1 <= W <= 109 or not 1 <= H <= 109:
        return None

    left = 1
    right = 1012
    min_size_of_board = -1

    while left <= right:
        mid = (left + right) // 2
        row = mid // W
        col = mid // H

        total_leaf = row * col

        if total_leaf >= N:
            min_size_of_board = mid
            right = mid - 1

        else:
            left = mid + 1

    return min_size_of_board




