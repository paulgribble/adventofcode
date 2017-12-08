

def build_tower(lines):
	tower = {}
	for line in lines:
		parts = line.split('->')
		name, weight = parts[0].split()
		weight = int(weight.strip('()'))
		leaves = [] if len(parts) < 2 else [leaf.strip(',') for leaf in parts[1].split()]
		tower[name] = (weight, leaves)
	return tower

def compute_weight(root, tower):
	weight, leaves = tower[root]
	weights = []
	for leaf in leaves:
		w, _ = compute_weight(leaf, tower)
		weights.append(w)
	return weight + sum(weights), weights




lines = [line.strip('\n') for line in open("day7_input.txt")]
tower = build_tower(lines)

#root = "tknk"
root = "eqgvf"

prev_weight = 0
keepgoing = True
while keepgoing:
    root_weight, leaf_nodes = tower[root]
    # Compute weight of root and it's leaves
    weight, leaf_weights = compute_weight(root, tower)

    # Check if there's a leaf node with wrong weight
    unique_weights = set(leaf_weights)
    if len(unique_weights) > 1:
        # Find the wrong leaf node
        dupes = set(w for w in leaf_weights if leaf_weights.count(w) > 1)
        wrong = (unique_weights - dupes).pop()  # always len == 1 here
        # Update root and prev_weight for next iteration
        root = leaf_nodes[leaf_weights.index(wrong)]
        prev_weight = dupes.pop()
    else:
        # All leaf nodes have same weight, the problem is root
        w = prev_weight - sum(leaf_weights)
        print(root, w)
        keepgoing = False
