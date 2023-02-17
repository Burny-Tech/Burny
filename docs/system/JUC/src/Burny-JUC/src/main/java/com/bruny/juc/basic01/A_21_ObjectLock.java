package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note
 * 
 */

public class A_21_ObjectLock implements  Runnable {
    static  A_21_ObjectLock instance1 = new A_21_ObjectLock();
    static  A_21_ObjectLock instance2 = new A_21_ObjectLock();

    @Override
    public void run() {
        method();
    }

    // synchronized用在普通方法上，默认的锁就是this，当前实例
    private synchronized  void method() {
        System.out.println(Thread.currentThread().getName() + "  block1-线程开始---");
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(Thread.currentThread().getName() + "  block1-线程结束");

    }

    public static void main(String[] args) {
        // 因为是不同的实例，所以会并行执行
        Thread t1 = new Thread(instance1);
        Thread t2 = new Thread(instance2);
        t1.start();
        t2.start();
    }
}
