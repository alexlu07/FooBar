import java.io.*;
import java.util.*;

public class Solution {
    public static int[] solution(int[] pegs) {
        int[] distance = new int[pegs.length-1];
        for (int i = 0; i < pegs.length-1; i++) {
            distance[i] = pegs[i+1] - pegs[i];
        }

        int x = 0;
        for (int i = 0; i < distance.length; i++) {
            x += (i % 2 == 0) ? distance[i] : -distance[i];
        }

        int[] result = (pegs.length % 2 == 0) ? new int[]{ x * 2, 3 } : new int[]{ x * 2, 1 };

        double a = x * ((pegs.length % 2 == 0) ? 2.0/3 : 2);
        double[] gears = new double[pegs.length];
        gears[0] = a;
        for (int i = 1; i < gears.length; i++) {
            gears[i] = distance[i-1] - gears[i-1];
        }

        for (int i = 0; i < gears.length; i++) {
            if (gears[i] < 1) {
                result = new int[]{ -1, -1 };
            }
        }

        System.out.println(Arrays.toString(gears));
        return result;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{ 4, 30, 50 })));
    }
}
