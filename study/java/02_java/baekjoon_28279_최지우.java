package Java_02_hw;

import java.util.*;
import java.io.*;

public class baekjoon_28279_최지우 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int n = Integer.parseInt(br.readLine());
		LinkedList<Integer> deque = new LinkedList<>();
		
		for (int i=0; i<n; i++) {	
			st = new StringTokenizer(br.readLine());
			int com = Integer.parseInt(st.nextToken());
			switch (com) {
				case 1:
					deque.offerFirst(Integer.parseInt(st.nextToken()));
					break;
				case 2:
					deque.offerLast(Integer.parseInt(st.nextToken()));
					break;
				case 3:
					if (deque.size() > 0) {
						sb.append(deque.pollFirst());
					} else {
						sb.append(-1);
					}
					break;
				case 4:
					if (deque.size() > 0) {
						sb.append(deque.pollLast());
					} else {
						sb.append(-1);
					}
					break;
				case 5:
					sb.append(deque.size());
					break;
				case 6:
					if (deque.size() > 0) {
						sb.append(0);
					} else {
						sb.append(1);
					}
					break;
				case 7:
					if (deque.size() > 0) {
						sb.append(deque.peekFirst());
					} else {
						sb.append(-1);
					}
					break;
				case 8:
					if (deque.size() > 0) {
						sb.append(deque.peekLast());
					} else {
						sb.append(-1);
					}
					break;
			}
			if (com == 1 || com == 2) {
				continue;
			}
			sb.append("\n");
		}
		System.out.println(sb.toString());
	}
}
