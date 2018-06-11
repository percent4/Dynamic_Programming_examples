package DP_example;

import java.util.Date;
import java.math.BigInteger;

public class DP_change_sum {
    // 主函数
    public static void main(String[] args) {
        Date start_time =  new Date(); //开始时间
        int n = 400;
        BigInteger t = DP_Change_Sum(n);  // 动态规划法求解
        Date end_time =  new Date(); // 结束时间
        Long cost_time = end_time.getTime()-start_time.getTime();  // 计算时间，返回毫秒数
        System.out.println(String.format("The fib(%d) is %s.\nCost time is %.3fs.", n, t, cost_time*1.0/1000));
    }

    public static BigInteger DP_Change_Sum(int n){
        if(n <= 2)
            return BigInteger.ONE;
        if(n == 3)
            return  new BigInteger("2");
        else {
            BigInteger first = BigInteger.ONE;
            BigInteger second = BigInteger.ONE;
            BigInteger third  = BigInteger.ONE;
            BigInteger fourth  = new BigInteger("2");
            BigInteger answer;

            for(int i=1; i<n-2; i++){ // 重复循环n-3次
                answer =  first.add(second.add(fourth));
                first = second;
                second = third;
                third = fourth;
                fourth = answer;
            }

            return fourth;
        }
    }
}
