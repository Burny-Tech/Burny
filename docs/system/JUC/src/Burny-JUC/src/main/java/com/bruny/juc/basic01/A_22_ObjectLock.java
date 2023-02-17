package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note
 * 
 */

public class A_22_ObjectLock implements  Runnable {
    static  A_22_ObjectLock instance1 = new A_22_ObjectLock();
    static  A_22_ObjectLock instance2 = new A_22_ObjectLock();

    @Override
    public void run() {
        method();
    }

    // synchronized用在静态方法上，默认的锁就是当前所在的Class类，所以无论是哪个线程访问它，需要的锁都只有一把
    private static synchronized  void method() {
        System.out.println(Thread.currentThread().getName() + "  block1-线程开始---");
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(Thread.currentThread().getName() + "  block1-线程结束");

    }

    public static void main(String[] args) {
        // 虽然是不同的实例，调用的方法是static  方法 所以不会并行执行，是串行执行
        Thread t1 = new Thread(instance1);
        Thread t2 = new Thread(instance2);
        t1.start();
        t2.start();
    }
}
