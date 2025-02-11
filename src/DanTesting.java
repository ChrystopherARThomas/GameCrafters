import org.junit.Test;

import java.util.HashMap;
import java.util.HashSet;
import java.util.TreeSet;


public class DanTesting {

    @Test
    public void testing() {

        HashMap<Integer, HashSet<Integer>> allFoundNodes = new HashMap<>();
        HashMap<Integer, Integer> distances = new HashMap<>();
        GameMechanics gm = new GameMechanics(10);

        gm.generateMoves(10, new HashSet<>(), allFoundNodes);
        gm.findDistance(distances);
        System.out.println(gm.allFoundNodes.keySet());
        String dotRepresentation = gm.generateDOT();
        System.out.println(dotRepresentation);
    }

}
