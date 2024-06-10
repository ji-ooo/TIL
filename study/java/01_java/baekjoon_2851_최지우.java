package Java_01_test;

import java.util.*;

public class baekjoon_2851_최지우 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int sum = 0;
		
		for (int i = 0; i < 10; i ++) {
			int k = sc.nextInt();
			
			if (sum + k <= 100) {
				sum += k;
				if (i == 9) {
					System.out.println(sum);
					break;
				}
			}
			
			else {
				if (100 - sum < sum + k - 100) {
					System.out.println(sum);
				}
				else {
					System.out.println(sum+k);
				}
				break;
			}
		sc.close();
		}
	}
}
