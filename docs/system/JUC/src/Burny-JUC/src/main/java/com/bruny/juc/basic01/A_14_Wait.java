package com.bruny.juc.basic01;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * @author cyx
 * @note
 * 
 */

public class A_14_Wait {

    public synchronized void before() {
        System.out.println("before");
        this.notify();
    }

    public synchronized void after() {
        try {
            this.wait();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        System.out.println("after");
    }

    public static void main(String[] args) {
        ExecutorService executorService = Executors.newCachedThreadPool();
        A_14_Wait wait = new A_14_Wait();
        executorService.execute(() -> wait.after());
        executorService.execute(() -> wait.before());
    }

}
