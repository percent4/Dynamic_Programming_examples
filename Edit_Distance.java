package DP_example;


// 计算两个字符串的编辑距离(Edit Distance)
public class Edit_Distance {

    // 主函数
    public static void main(String[] args) {
        String str1 = "cat";//"Sunday";
        String str2 = "hat";//"Saturday";
        int edit_dist = edit_distance(str1, str2);
        System.out.println(String.format("The edit distance of '%s' and '%s' is %d.",
                str1, str2, edit_dist));
    }

    /*
    函数edit_distanc: 计算两个字符串的编辑距离(Edit Distance)
    传入参数:  两个字符串str1和str2
    返回: 编辑距离
     */
    public static int edit_distance(String str1, String str2){

        // 字符串的长度
        int m = str1.length();
        int n = str2.length();

        // 初始化表格，用于维护子问题的解
        int[][] dp = new int[m+1][n+1];
        for(int i=0; i <= m; i++)
            for(int j=0; j <= n; j++)
                dp[i][j] = 0;

        // using DP in bottom-up manner
        for(int i=0; i <= m; i++){
            for(int j=0; j <= n; j++) {
                /* If first string is empty, only option is to
                 * isnert all characters of second string, thus the
                 * min opration is j
                 */
                if(i == 0) { dp[i][j] = j;}

                /* If second string is empty, only option is to
                 * remove all characters of second string, thus the
                 * min opration is i
                 */
                else if(j == 0){dp[i][j] = i;}

                /* If last characters are same, ignore last character
                 * and recursive for remaining string
                 */
                else if(str1.charAt(i-1) == str2.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1];
                }

                /*If last character are different, consider all
                 *possibilities and find minimum of inserting, removing, replacing
                 */
                else{
                    /*
                     * dp[i][j-1]: Insert
                     * dp[i-1][j]: Remove
                     * dp[i-1][j-1]: Replace
                     */
                    dp[i][j] = 1 + min(min(dp[i][j-1], dp[i-1][j]), dp[i-1][j-1]);
                }
            }
        }

        return dp[m][n];
    }

    public static int min(int i, int j){
        return (i <= j) ? i : j;
    }

}
