package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note
 * 
 */

public class A_17_ReentrantLock {

    public  synchronized  void before(){
        System.out.println("before");
        this.after();
    }
    public synchronized void after(){
        System.out.println("after");
    }
}
