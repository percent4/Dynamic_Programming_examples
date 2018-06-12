package scala.com.dynamic_programming.fibnacci

object Fibnacci_DP_demo {

  /*
  * This test is utilized to calculate the fibanacci sequence result by two different methods:
  * i.e. normal dynamic programming, and dynamic programming & recursive.
  * And the speed and efficiency will be obtained by comparing two test results.
  */

  def main(args: Array[String]): Unit = {

    val x = 39
    val ts_start = System.currentTimeMillis()
	
    //fibnacci数列求解结果--dynamic programming动态规划法
    val fib_n = dp_fib(x)
    val ts_end = System.currentTimeMillis()
	
    // 递归法
    val fib_N = rec_fid(x)
    val ts_final = System.currentTimeMillis()

    println(s">>>>>> use dynamic programming, fibnacci sequence, i.e. f(${x}), result is: " + fib_n)
    println(">>>>>> And its consumed time (in miliseconds) is: " + (ts_end-ts_start))
    println(s">>>>>> use recursive, fibnacci sequence, i.e. f(${x}), result is : " + fib_N)
    println(">>>>>> And its consumed time (in miliseconds) is: " + (ts_final-ts_end))


  }

  // calculate fibanacci sequence result by using dynamic programming
  def dp_fib(n:Int): BigInt ={
    // 该方法在普通的动态规划法的基础上进行了改进，通过不断更新最新两个fibnacci数列的值来替代将所有数列的
    // 值存储在list中，可以有效防止内存OOM错误
    // 需要使用scala 的Bigint，其对应java的biginteger，如果使用Long，则容易溢出
    var previousFib:BigInt = 0
    var currentFib:BigInt = 1
    var newFib:BigInt = 0L

    if(n<2){
      BigInt.int2bigInt(n)
    }

    else {
      for(i <- 1 until  n){ // 重复循环n-1次
        // 不断把fibanacci数列中最新的两个值赋值给previousFib和currentFib，减少对对内存的占用，提高效率
        newFib = previousFib + currentFib
        previousFib = currentFib
        currentFib = newFib
      }
      // scala中默认以最后一个变量作为返回值
      currentFib
    }

  }

  // 递归法去求fibnacci数
  def rec_fid(n:Int): BigInt = {
    if(n<2){
      BigInt.int2bigInt(n)
    }
    else {
      // 所有的中间fibnacci数列的值都会存储在内存中，一旦过大则会导致内存OOM错误
      rec_fid(n-1) + rec_fid(n-2)
    }
  }

}

