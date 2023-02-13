package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note
 * @date 2023/2/13 9:53
 */

public class A_20_CusLock implements  Runnable {

    static  A_20_CusLock instance = new A_20_CusLock();

       Object block1 = new Object();
       Object block2 = new Object();


    @Override
    public void run() {
        synchronized (block1){
            System.out.println(Thread.currentThread().getName()+"  block1-线程开始---");
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName()+"  block1-线程结束");
        }
        synchronized (block2){
            System.out.println(Thread.currentThread().getName()+"  block2-线程开始---");
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName()+"  block2-线程结束");
        }
    }
    public static void main(String[] args) {
        Thread t1 = new Thread(instance);
        Thread t2 = new Thread(instance);
        t1.start();
        t2.start();
    }
}
