package Java_01_test;

import java.util.*;
import java.math.BigInteger;

public class baekjoon_1010_최지우 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int i = 0; i < T; i ++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			BigInteger result = comb(N, M);
			System.out.println(result);
		}
		sc.close();
		
	}
	public static BigInteger comb(int N, int M) {
		if (N == M) {
			return BigInteger.ONE;
		}
		BigInteger n = BigInteger.ONE;
		BigInteger m = BigInteger.ONE;
		
		for (int i = 0; i < N; i ++) {
			n = n.multiply(BigInteger.valueOf(M-i));
			m = m.multiply(BigInteger.valueOf(i+1));
		}
		return n.divide(m);
	}
}
