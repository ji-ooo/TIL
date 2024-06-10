package Java_01_test;

import java.util.Scanner;
import java.io.IOException;
import java.util.Arrays;

public class baekjoon_11653_최지우 {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		sc.close();
		if (n == 1) {
			System.out.println();
		}
		else {
			boolean[] prime = new boolean[n+1];
			Arrays.fill(prime, true);
			
			prime[0] = prime [1] = false;
			
			for (int i = 2; i*i < n; i++) {
				if (prime[i]) {
					for (int j = i*i; j <= n; j += i) {
						prime[j] = false;
					}
				}
			}
			
			while (n > 1) {
				for (int i = 2; i < n; i ++) {
					if (n%i == 0) {
						n /= i;
						System.out.println(i);
						break;
					}
				}
				
				if (prime[n]) {
					System.out.println(n);
					break;
				}
			}
		}
	}
}
