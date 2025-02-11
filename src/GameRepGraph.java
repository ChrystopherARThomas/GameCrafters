
import java.util.HashMap;
import java.util.HashSet;

public class GameRepGraph {
    Node rootNode;

    public GameRepGraph(int root) {
        rootNode = new Node(root);
    }

    private class Node {
        /* used to keep track of nodes and their children */
        HashMap<Integer, Node> childGraph = new HashMap();

        /* every node has a label and arrows pointing to its children */
        int nodeLabel;

        private Node(int nodeLabel) {
            this.nodeLabel = nodeLabel;
        }
    }

    public void addNode(int start, HashSet<Integer> allValidMoves) {
        GameMechanics game = new GameMechanics(start);

        Node rootNode = new Node(start);


        // figuring out which nodes are missing; will have infinite label
        for (int i = 0; i < start; i++) {

        }


    }

}
