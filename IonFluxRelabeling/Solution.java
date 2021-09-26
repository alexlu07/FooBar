import java.util.HashMap;
import java.util.Arrays;
import java.util.stream.IntStream;
class Node {
    public Node parent;
    public int value;
    public Node[] children = new Node[2];

    public Node(int[] values, Node p, HashMap<Integer, Node> n) {
        // System.out.println(Arrays.toString(values) + ((values.length-1)/2) + " " + ((values.length-1)/2+1) + " " + (values.length-1));

        parent = p;
        value = values[values.length-1];

        n.put(value, this);
        if (values.length > 1) {
            // System.out.println(values.length);
            if (!n.containsKey( values[(values.length-1)/2-1] )) {
                children[0] = new Node(Arrays.copyOfRange(values, 0, (values.length-1)/2), this, n);
            }
            if (!n.containsKey( values[values.length-2] )) {
                children[1] = new Node(Arrays.copyOfRange(values, (values.length-1)/2, values.length-1), this, n);
            }
        }

    }
}
public class Solution {
    public static int[] solution(int h, int[] q) {
        // HashMap<Integer, Integer> index = new HashMap<Integer, Integer>();
        // for (int i = 0; i < q.length; i++) {
        //     index.put(q[i], i);
        // }

        int max = Arrays.stream(q).max().getAsInt();
        int root = (int) Math.pow(2, 32-Integer.numberOfLeadingZeros( (max+1 < Math.pow(2, h) - 1) ? max+1 : (int) Math.pow(2, h) - 1 ));
        System.out.println(root);

        HashMap<Integer, Node> nodes = new HashMap<Integer, Node>();
        new Node(IntStream.range(1, root).toArray(), null, nodes);

        // System.out.println(nodes);
        int[] p = new int[q.length];
        for (int i = 0; i < q.length; i++) {
            p[i] = (nodes.get(q[i]).parent != null) ? nodes.get(q[i]).parent.value : -1;
        }

        return p;

    }
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(3, new int[]{ 7, 3, 5, 1 } )));
    }
}
