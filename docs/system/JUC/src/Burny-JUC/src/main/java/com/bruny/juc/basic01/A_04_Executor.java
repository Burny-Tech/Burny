package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note
 * 
 */


import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Excutor 管理多个异步恩物的执行。这里的异步是指多个任务的执行互不干扰，无需进行同步操作
 * <p>
 * 主要有三种Excutor
 * CachedThreadPool 一个任务创建一个线程
 * FixedThreadPool 所有任务只能使用固定大小的线程
 * SingleThreadExcutor 相当于大小为1 的FixedThreadPool
 */


public class A_04_Executor {

    public static void main(String[] args) {
        ExecutorService executorService =
                Executors.newCachedThreadPool();
        for (int i = 0; i < 10; i++) {
            executorService.execute(new A_01_MyRunnable());
        }
        executorService.shutdown();
        System.out.println("shutdown");
        //此时主线程已经关闭，executor里还有其他线程没执行完
    }
}
/**
 * 结果：
 * shutdown
 * print
 * print
 * print
 * print
 * print
 * print
 * print
 * print
 * print
 * print
 */
