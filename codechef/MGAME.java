import java.io.*;
import java.util.*;

class MGAME {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    sc.nextLine();

    for(int z = 0; z < t; z++) {
      String inp = sc.nextLine();
      String in[] = inp.split(" ");
      int n = Integer.parseInt(in[0]);
      int p = Integer.parseInt(in[1]);
      int i = 1, j = 1, k = 1;

      HashMap<Integer, Integer> maxVal = new HashMap<>();
      
      
      while(true) {
        int score = (((n%i)%j)%k)%n;
        System.out.println("( " + i + " , " + j + " , " + k + " )" + " = " + score);
        if(maxVal.get(score) == null) {
          maxVal.put(score, 1);
        } else {
          maxVal.put(score, maxVal.get(score) + 1);
        }
        k++;
        if(k > p) {
          if(j >= p) {
            if(i == p)
              break;
            i++;
            j = 1;
          }
          j++;
          k = 1;
        }
      }
      
      int intKey = 0;
      Collection<?> keys = maxVal.keySet();
      for(Object key: keys) {
        intKey = Integer.parseInt(key.toString());
      }
      System.out.println(maxVal);
      System.out.println(maxVal.get(intKey));


      int max = 0, maxNum = 0;
      for(int x = 1; x <= n; x++) {
        if(max < n%x) {
          max = n%x;
          maxNum = x;
        }
      }
      // System.out.println(max + " Number = " + maxNum);
      // System.out.println("P: " + p);
      // System.out.println("N: " + n);
      // System.out.println("Mod: " + max);
      // System.out.println(": " + p);
      System.out.println(((p-max)*(p-max) + (p-n)*(p-max) + (p-n)*(p-n)));

      // i = maxNum;
    }
  }
}