package com.bruny.juc.basic01;

import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.ReentrantLock;

/**
 * @author cyx
 * @note
 * @date 2023/2/9 17:28
 */

public class A_16_OptimismPessimismLocks {
    //悲观锁
    public synchronized void A() {

    }

    //需要保证多个线程使用的是同一把锁
    private ReentrantLock lock = new ReentrantLock();

    public void updateData() {
        lock.lock();
        try {
            //同步操作
        } finally {
            lock.unlock();
        }
    }

    //乐观锁
    private AtomicInteger atomicInteger = new AtomicInteger();

    public void updateData2() {
        atomicInteger.incrementAndGet();
    }
}
