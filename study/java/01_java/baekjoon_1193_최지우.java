package Java_01_test;

import java.util.*;

public class baekjoon_1193_최지우 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int X = sc.nextInt();
		sc.close();
		
		int i = 1;
		while (X > i) {
			X -= i;
			i += 1;
		}
		
		int a = i;
		int b = 1;
		
		while (X > 1) {
			a -= 1;
			b += 1;
			X -= 1;
		}
		
		if (i%2 == 0) {
			int tmp = b;
			b = a;
			a = tmp;	
		}
		
		System.out.print(a);
		System.out.print("/");
		System.out.print(b);
	}
}
