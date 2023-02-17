package com.bruny.juc.basic01;

import sun.security.jca.GetInstance;

/**
 * @author cyx
 * @note
 * 
 */

public class A_19_CodeBlock  implements  Runnable{

    static  A_19_CodeBlock instance = new A_19_CodeBlock();

    public static    A_19_CodeBlock getInstance(){
        return instance;
    }
    @Override
    public void run() {
        // 同步代码块形式——锁为this,两个线程使用的锁是一样的,线程1必须要等到线程0释放了该锁后，才能执行
        synchronized (this){
            System.out.println(Thread.currentThread().getName()+"  线程开始---");
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName()+"  线程结束");
        }

    }

    public static void main(String[] args) {
        Thread t1 =new Thread(getInstance());
        Thread t2 = new Thread(getInstance());
        t1.start();
        t2.start();
    }
}
