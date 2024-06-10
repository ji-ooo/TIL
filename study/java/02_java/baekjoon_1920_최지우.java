package Java_02_hw;

import java.util.*;
import java.io.*;

public class baekjoon_1920_최지우 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(st.nextToken());
		int[] nums = new int[n]; 
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(nums);
		st = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<m; i++) {
			int t = Integer.parseInt(st.nextToken());
			int in = Arrays.binarySearch(nums, t);
			if (in < 0) {
				sb.append(0);
				sb.append("\n");
			} else {
				sb.append(1);
				sb.append("\n");
				
			}
		}
		System.out.println(sb.toString());
	}
}
