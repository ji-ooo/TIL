package Java_02_hw;

import java.util.*;
import java.io.*;

public class baekjoon_24511_최지우 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];
        LinkedList<Integer> que = new LinkedList<>();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<n; i++) {
			if (arr[i] == 1) {
				st.nextToken();
				continue;
			}
			que.offer(Integer.parseInt(st.nextToken()));
		}
		
		int m = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<m; i++) {
			que.offerFirst(Integer.parseInt(st.nextToken()));
			sb.append(que.pollLast());
			sb.append(" ");
		}
		
		System.out.println(sb.toString());
	}
}
