package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note
 * @date 2023/2/13 15:04
 */

public class A_24_ReentrantLock  implements  Runnable {

    public static void main(String[] args) {
        A_24_ReentrantLock lock = new A_24_ReentrantLock();
        Thread t =new Thread(lock);
        t.start();


    }
    public synchronized void A() {
        System.out.println(Thread.currentThread().getId() + ": A()");
        B();
    }

    //线程A 锁 的对象是 当前 实例，此时还没有释放掉当前实例，可以处理 方法B ，方法B 锁的对象也是当前实例。
    public synchronized void B() {
        System.out.println(Thread.currentThread().getId()+ ": B()");
        C();
    }

    public synchronized void C() {
        System.out.println(Thread.currentThread().getId()+ ": C()");
    }


    @Override
    public void run() {
        A();
    }
}
