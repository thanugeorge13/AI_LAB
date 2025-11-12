import math

pruned = []  # store pruned branches

def alpha_beta(node, depth, alpha, beta, maximizingPlayer, path):
    if isinstance(node, int):  # If leaf
        return node, path

    if maximizingPlayer:
        value = -math.inf
        best_path = None
        for i, child in enumerate(node):
            v, p = alpha_beta(child, depth+1, alpha, beta, False, path + [i])
            if v > value:
                value = v
                best_path = p
            alpha = max(alpha, value)
            if alpha >= beta:
                pruned.append(("MAX Prune at Depth", depth, "Remaining Children Indexes:", list(range(i+1, len(node)))))
                break
        return value, best_path
    else:
        value = math.inf
        best_path = None
        for i, child in enumerate(node):
            v, p = alpha_beta(child, depth+1, alpha, beta, True, path + [i])
            if v < value:
                value = v
                best_path = p
            beta = min(beta, value)
            if alpha >= beta:
                pruned.append(("MIN Prune at Depth", depth, "Remaining Children Indexes:", list(range(i+1, len(node)))))
                break
        return value, best_path



tree = [
    [   # Left Subtree of Root (MIN)
        [21, 5],
        [15, 11],
        [12, 8]
    ],
    [   # Middle Subtree of Root (MIN)
        [9, 13],
        [5, 12],
        [13, 12]
    ],
    [   # Right Subtree of Root (MIN)
        [13, 14],
        [7, 10]
    ]
]

# Run alpha-beta
value, path = alpha_beta(tree, 0, -math.inf, math.inf, True, [])

print("Root Node Value:", value)
print("Path taken (child indexes at each level):", path)
print("Pruned Branches:", pruned)
