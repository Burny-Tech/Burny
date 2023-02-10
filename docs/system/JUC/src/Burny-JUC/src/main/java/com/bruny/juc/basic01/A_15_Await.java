package com.bruny.juc.basic01;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * @author cyx
 * @note
 * @date 2023/2/9 15:19
 */

public class A_15_Await {


    private Lock lock = new ReentrantLock();

    private Condition condition = lock.newCondition();


    public void before() {
        lock.lock();

        try {
            System.out.println("before");
            condition.signal();
        } finally {
            lock.unlock();
        }
    }

    public void after() {
        lock.lock();
        try {
            condition.await();
            System.out.println("after");
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        } finally {
            lock.unlock();
        }
    }

    public static void main(String[] args) {
        A_15_Await await = new A_15_Await();

        ExecutorService pool = Executors.newCachedThreadPool();

        pool.execute(() -> await.after());
        pool.execute(() -> await.before());
    }


}
