package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note
 * @date 2023/2/13 11:26
 */

public class A_23_ClassLock implements  Runnable{

    static  A_23_ClassLock instance1  = new A_23_ClassLock();
    static  A_23_ClassLock instance2 = new A_23_ClassLock();

    @Override
    public void run() {
        //锁住的是class ,所以执行是串行的。
        synchronized (A_23_ClassLock.class){
            System.out.println(Thread.currentThread().getName() + "  block1-线程开始---");
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + "  block1-线程结束");  
        }
    }
    public static void main(String[] args) {
        //锁住的是class ,所以执行是串行的。
        Thread t1 = new Thread(instance1);
        Thread t2 = new Thread(instance2);
        t1.start();
        t2.start();
    }
}

