package Java_02_hw;

import java.util.*;

public class baekjoon_15652_최지우 {
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		sc.close();
		
		StringBuilder sb = new StringBuilder();
		
		int[] arr = new int[m];
		solve(n, m, 0, 1, arr, sb);
		System.out.println(sb.toString());
	}
	
	public static void solve(int n, int m, int idx, int start, int[] arr, StringBuilder sb) {
		if (idx == m) {
			for (int num : arr) {
				sb.append(num).append(" ");
			}
			sb.append("\n");
			return;
		}
		
		for (int i = start; i <= n; i++) {
			arr[idx] = i;
			solve(n, m, idx+1, i, arr, sb);
		}
	}
}
