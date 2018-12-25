import java.util.*;
class Test {

	public static boolean satisfies(int a, int b, int k) {
		if(Math.min(a, b) > k)
			return true;
		else
			return false;
	}

	public static void main (String args[]) {
		Scanner sc = new Scanner(System.in);
		int test_cases = sc.nextInt();
		for (int k=0; k<test_cases; k++) {
			String in1 = sc.nextLine();
			String[] ok = in1.split(" ");
			int n = Integer.parseInt(ok[0]);
			int k = Integer.parseInt(ok[1]);
			String in2 = sc.nextLine();
			String[] ok2 = in2.split(" ");
			int[] arr = new int[n];
			for (int j=0; j<ok2.length; j++) {
				arr[j] = Integer.parseInt(ok2[j]);
			}
			int j=1;
			Arrays.sort(arr);
			for(int i=0; i<arr.length-1; i++) {
				while(satisfies(arr[i], arr[j], k)) {
					arr[i] = arr[i]-1;
					arr[j] = arr[j]-1;
				}
				j++;
			}
			int sum=0;
			for (int i=0; i<arr.length; i++) {
				sum+=arr[i];
			}
			System.out.println(sum);
		}
	}
}