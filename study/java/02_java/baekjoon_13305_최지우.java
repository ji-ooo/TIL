package Java_02_hw;

import java.util.*;
import java.io.*;
import java.math.BigInteger;

public class baekjoon_13305_최지우 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		
		BigInteger[] dist = new BigInteger[n-1];
		BigInteger[] cost = new BigInteger[n];
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i < n-1; i++) {
			dist[i] = new BigInteger(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i < n; i++) {
			cost[i] = new BigInteger(st.nextToken());
		}
		
		BigInteger tmp_dist = dist[0];
		BigInteger init_cost = cost[0];

		int idx = 1;
		BigInteger total = BigInteger.ZERO;
		
		while (idx < n-1) {
			if (init_cost.compareTo(cost[idx]) <= 0) {
				tmp_dist = tmp_dist.add(dist[idx]);
			} else {
				total = total.add(tmp_dist.multiply(init_cost));
				init_cost = cost[idx];
				tmp_dist = dist[idx];
			}
			idx += 1;
		}
		total = total.add(tmp_dist.multiply(init_cost));
		System.out.println(total);
	}
}
