package com.bruny.juc.basic01;

import lombok.Synchronized;

/**
 * @author cyx
 * @note
 * 
 */

public class A_18_MethodLock implements  Runnable {

    static A_18_MethodLock instance  = new A_18_MethodLock();

    public  synchronized   void method (){
        System.out.println(Thread.currentThread().getName()+"  线程开始---");
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(Thread.currentThread().getName()+"  线程结束");
    }


    @Override
    public void run() {
        method();
    }

    public static void main(String[] args) {
        Thread t1 = new Thread(instance);
        Thread t2 = new Thread(instance);
        t1.start();
        t2.start();
    }
}
