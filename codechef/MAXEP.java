import java.util.*;
import java.lang.*;

class MAXEP {
	public static void main (String args[]) {
		Scanner sc = new Scanner(System.in);
		String in = sc.nextLine();
		String[] ins = in.split(" ");
		int n = Integer.parseInt(ins[0]);
		int c = Integer.parseInt(ins[1]);
		int begin = 1;
		int end = n;
		int mid = 0;
		int ci = 1000;
		int flag = 0;
		int step_size;
		if(n < 10) {
			step_size = 1;
		}
		else {
			step_size = n/10;
		}
		while(true) {
			// mid = (begin+end)/step_size;
			mid = begin + step_size;
			System.out.println("1 " + mid);
			System.out.flush();
			ci = ci - 1;
			int inp = sc.nextInt();
			if(inp == 0){
				begin = mid;
				flag = 0;
			}
			else if(inp == 1) {
				System.out.println("2");
				System.out.flush();
				ci = ci-c;
				end = mid;
				step_size = end/10;
				if(flag == 0) {
					mid = begin
				}
				flag = 1;
			}

			if(Math.abs(begin-end) == 1 || ci < 1){
				System.out.println("3 " + end);
				System.out.flush();
				break;
			}
		}
		// int temp = n;
		// int previous = n;
		// int current = 1;
		// while(true) {
		// 	System.out.println("1 " + temp);
		// 	int inp = sc.nextInt();
		// 	if(inp == 1 && Math.abs(begin-end) == 1){
		// 		System.out.println("2");
		// 		int small = begin < end ? begin : end;
		// 		System.out.println("3 " + small);
		// 		break;
		// 	}
		// 	if(current == 1){
		// 		if(inp == 0){
		// 			begin = end + n/10;
		// 			end = previous;
		// 			current = 0;
		// 			temp = begin;
		// 		}
		// 		else if(inp == 1){
		// 			System.out.println("2");
		// 			previous = end;
		// 			end = temp/2;
		// 			temp = temp/2;
		// 		}
		// 	}
		// 	else if(current == 0) {
		// 		if(inp == 0){
		// 			begin = begin + (n/10);
		// 			temp = begin;
		// 		}
		// 		else if(inp == 1){
		// 			System.out.println("2");
		// 			end = begin + (n%10);
		// 			current = 0;
		// 			temp = end;
		// 		}
		// 	}
		//}
	}
}