package Java_01_test;

import java.util.*;

public class baekjoon_4344_최지우 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int C = sc.nextInt();
		
		for (int i = 0; i < C; i ++) {
			int len = sc.nextInt();
			 
			int[] scores = new int[len];
			int total = 0;
			
			for (int idx = 0; idx < len; idx ++) {
				scores[idx] = sc.nextInt();
				total += scores[idx];
			}
			total /= len;
			
			int cnt = 0;
			for (int idx = 0; idx < len; idx ++) {
				if (scores[idx] > total) {
					cnt += 1;
				}
			}
			
			float per = (float)cnt * 100 / len;
			
			String result = String.format("%.3f", per) + '%';
			
			System.out.println(result);
		}
		sc.close();
	}
}
