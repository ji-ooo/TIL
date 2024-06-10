package Java_02_hw;

import java.util.*;
import java.io.*;

public class baekjoon_1021_최지우 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        LinkedList<Integer> que = new LinkedList<>();
        
        for (int i = 1; i <= n; i++) {
            que.offer(i);
        }
        
        st = new StringTokenizer(br.readLine());
        
        int result = 0;
        for (int t = 0; t < m; t ++) {
        	int target = Integer.parseInt(st.nextToken());
        	int targetIdx = que.indexOf(target);
        	int left = targetIdx;
        	int right = que.size() - targetIdx;
        	
        	if (left <= right) {
        		for (int i = 0; i < left; i++) {
        			que.offer(que.pollFirst());
        		}
        		result += left;
        	} else {
        		for (int i = 0; i < right; i++) {
        			que.offerFirst(que.pollLast());
        		}
        		result += right;
        	}
        	que.pollFirst();
        }
        
        System.out.println(result);
    }
}
