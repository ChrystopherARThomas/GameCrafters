
import java.util.*;

public class GameMechanics {
    int start;
    HashMap<Integer, Collection<Set<Integer>>>  moves = new HashMap<>(); // map current integer to all possible moves
    HashMap<Integer, HashSet<Integer>> allFoundNodes = new HashMap<>(); // maps nodes to their children
    HashMap<Integer, Integer> allDistances = new HashMap<>(); // maps node to its corresponding distance

    public GameMechanics(int start) {
        this.start = start;
    }

    public boolean isSolution(int pos) {
        return pos == 0;
    }

    /* returns whether current pos is valid and how many children (or valid moves) a node
    * must make based on modular arithmetic*/
    public int isValid(int pos) {
        if (pos % 3 == 0) {
            return 0;
        } else if (pos % 4 == 1) {
            return 1; // max 1 solution
        } else {
            return 2; // max 2 solutions
        }
    }

    /* generate all possible moves given a start position
    * this function assumes we never pass in the same number twice (potential overriding issues
    * if this ever changes oof*/
    public HashMap<Integer,Collection<Set<Integer>>> generateMoves(int pos, Set<Integer> currPaths, HashMap<Integer, HashSet<Integer>> nodes) {
        /* we start from current starting position --> I can either subtract 1 or 2
        Once I subtract, add both to my Collection where relationship w/ start position is clear
        Once I've done this I need to repeat this for all numbers until my current position is no
        longer valid, or I've reached 0 -- Dan... Dan... why... why make me do this am dumb
         */
        currPaths.add(pos);
        nodes.putIfAbsent(pos, new HashSet<>());

        if (isSolution(pos) || isValid(pos) == 0) {
            /*
            need my value for my mapping to be a collection of different current paths
             */
            if (this.moves.get(start) == null) {
                this.moves.put(start, new ArrayList<>());
            }
            this.moves.get(start).add(new HashSet<>(currPaths));
            return moves;
        }

        if (isValid(pos) == 1) { // you only have one valid move
            int nextPos1 = pos - 1;
            nodes.get(pos).add(nextPos1);
            nodes.putIfAbsent(nextPos1, new HashSet<>());
            nodes.get(nextPos1).add(pos);
            generateMoves(nextPos1, new HashSet<>(currPaths), nodes);

        } else if (isValid(pos) == 2) { // you potentially could have up to 2 valid moves
            int nextPos1 = pos - 1;
            int nextPos2 = pos - 2;
            nodes.get(pos).add(nextPos1);
            nodes.get(pos).add(nextPos2);

            nodes.putIfAbsent(nextPos1, new HashSet<>());
            nodes.putIfAbsent(nextPos2, new HashSet<>());

            nodes.get(nextPos1).add(pos);
            nodes.get(nextPos2).add(pos);
            generateMoves(nextPos1, new HashSet<>(currPaths), nodes);
            generateMoves(nextPos2, new HashSet<>(currPaths), nodes);
        }

        // done so I can use info found during calls outside of method
        this.allFoundNodes = nodes;
        return this.moves;
    }


    /* calculate distance by taking current node and its children
    if it has an invalid child, distance = inf
    if it's child = 0 don't add to distance
    otherwise current node's value = number of nodes you went through before you reached solution
    BFS guarantees shortest or best solution is found first
     */
    public HashMap<Integer, Integer> findDistance(HashMap<Integer, Integer> distances) {
        Queue<Integer> queue = new LinkedList();
        /*
        with an undirected graph, BFS destroys hierarchy of nodes by visiting the same node multiple times
        visited ensures nodes are only visited once
         */
        HashSet<Integer> visited = new HashSet<>();

        // we're traversing bottom up
        for (int currNode: allFoundNodes.keySet()) {
            if (currNode == 0) {
                distances.put(currNode, 0);
                queue.add(currNode);
                visited.add(currNode);
            }
        }

        while (!queue.isEmpty()) {
            int currentNode = queue.poll();
            Integer currDist = distances.get(currentNode);

            // iterating through all of the children of the current Node
            for (int neighbor : allFoundNodes.getOrDefault(currentNode, new HashSet<>())) {
                // if the parentNode is linked with the current node and the parent hasn't already been visited
                if (allFoundNodes.get(neighbor).contains(currentNode) && !visited.contains(neighbor)) {
                    // add to map with currDist incremented by 1
                    distances.put(neighbor, currDist + 1);
                    queue.add(neighbor);
                    visited.add(neighbor);
                }
            }
        }

        this.allDistances = distances;
        return distances;
    }

    public String generateDOT() {
        StringBuilder sb = new StringBuilder();
        sb.append("digraph G {\n");

        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();

        // Start from the root node (initial state)
        queue.add(this.start);
        visited.add(this.start);

        while (!queue.isEmpty()) {
            int node = queue.poll();

            int dist = allDistances.getOrDefault(node, Integer.MAX_VALUE);
            // Ternary operator (condition) ? (if true) : (if false); makes conditional statements more prettiful
            String label = (dist == Integer.MAX_VALUE) ? "∞" : String.valueOf(dist);
            String color = (node == 0) ? "#ff66a3" : (node == this.start) ? "#c084fc" : "#ffffff";

            sb.append(String.format("  \"%d,%s\" [shape=\"ellipse\" style=\"filled\" fillcolor=\"%s\"];\n",
                    node, label, color));

            for (int child : allFoundNodes.getOrDefault(node, new HashSet<>())) {
                if (!visited.contains(child)) {
                    queue.add(child);
                    visited.add(child);
                }
                int childDist = allDistances.getOrDefault(child, Integer.MAX_VALUE);
                String childLabel = (childDist == Integer.MAX_VALUE) ? "∞" : String.valueOf(childDist);

                sb.append(String.format("  \"%d,%s\" -> \"%d,%s\";\n", node, label, child, childLabel));
            }
        }

        sb.append("}\n");
        return sb.toString();
    }

}
