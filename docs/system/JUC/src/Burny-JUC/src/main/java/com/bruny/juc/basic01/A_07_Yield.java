package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note
 * @date 2023/2/6 16:41
 */

public class A_07_Yield {
    public static void main(String[] args) {


    }

}

class MyRunnal1 implements Runnable {
    @Override
    public void run() {

        //before:处理重要的事情
        Thread.yield();
        //after:声明了当前线程已经完成了重要的执行操作，接下来  建议CPU给其他线程先行操作
        //注意是：建议，具体看CPU调度


    }
}

