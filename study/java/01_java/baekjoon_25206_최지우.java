package Java_01_test;

import java.util.*;

public class baekjoon_25206_최지우 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        double total_score = 0;
        int total = 0;
        
        for (int i = 0; i < 20; i++) {
            String[] score = sc.nextLine().split(" ");
            double credit = Double.parseDouble(score[1]);
            String grade = score[2];
            
            if (grade.equals("P")) {
                continue;
            }
            
            double gradeValue = 0;
            switch (grade) {
                case "A+":
                    gradeValue = 4.5;
                    break;
                case "A0":
                    gradeValue = 4.0;
                    break;
                case "B+":
                    gradeValue = 3.5;
                    break;
                case "B0":
                    gradeValue = 3.0;
                    break;
                case "C+":
                    gradeValue = 2.5;
                    break;
                case "C0":
                    gradeValue = 2.0;
                    break;
                case "D+":
                    gradeValue = 1.5;
                    break;
                case "D0":
                    gradeValue = 1.0;
                    break;
                case "F":
                    gradeValue = 0.0;
                    break;
            }
            
            total_score += credit * gradeValue;
            total += credit;
        }
        
        double gpa = total_score / total;
        System.out.printf("%.6f\n", gpa);
        
        sc.close();
    }
}
