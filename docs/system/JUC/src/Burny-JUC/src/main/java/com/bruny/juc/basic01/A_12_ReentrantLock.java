package com.bruny.juc.basic01;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * @author cyx
 * @note
 * 
 */

public class A_12_ReentrantLock {


    private Lock lock = new ReentrantLock();

    //submit.cancel 和 shutdown 组合结果不同
    //1. 只有 submit.cancel 则会打印第一个,第二个不会打印, 并且需要过一会儿才自动结束程序.原因:第二次未执行之前,主线程就已经cancel了线程,所以不会打印
    //2. shutdown : 第一个和第二个都打印,并且执行结束后立即 自动结束程序. 应该是会等待所有线程执行完之后关闭线程池
    //3. 有submit 和shutdonw : 只打印第一个,并且执行结束后立即 自动结束程序

    //总结:有shutdown :等待子线程执行完后再关闭线程池,并且关闭后马上退出程序
    //     submit.cancel: 在子线程还没执行之前可能就会已被取消执行,不能马上退出程序


    public static void main(String[] args) {
        A_12_ReentrantLock re = new A_12_ReentrantLock();
        ExecutorService executorService = Executors.newCachedThreadPool();
        Future<?> submit = executorService.submit(() -> re.fun());
        Future<?> submit1 = executorService.submit(() -> re.fun());


        submit.cancel(true);
        submit1.cancel(true);
        executorService.shutdown();


    }


    public void fun() {
        lock.lock();
        try {
            for (int i = 0; i < 10; i++) {
                System.out.print(i + "\t");
            }
            System.out.println("\n");
        } finally {
            //确保释放锁,从而避免发生死锁.
            lock.unlock();

        }

    }

    // synchronized 和 ReentrantLock 比较:
    /**
     *  1.锁的实现
     *  synchronized 是基于JVM 实现的,ReentrantLock 是JDK 实现的.
     *
     *  2.性能
     *  synchronized 性能比 ReentrantLock 好
     *
     *  3.等待可终端
     *  当持有锁的线程长期不释放锁的时候,正在等待的线程可以选择放弃等待,改为处理其他事情.
     *  ReentrantLock 可以中断, Synchronized 不行
     *  4. 公平锁
     *  公平锁是指多个线程在等待同一锁时,必须按照申请锁的时间顺序来一次获得的
     *  synchronized 中的所示非公平的, ReentrantLock 默认情况也是非公平的,但是可以是公平的
     *
     *  5. 锁绑定多个条件
     *  一个ReentrantLock 可以同时绑定多个Condition对象
     *
     *  总结:
     *      除非需要使用 ReentrantLock 的高级功能，否则优先使用 synchronized。这是因为 synchronized 是 JVM 实现的一种锁机制，JVM 原生地支持它，而 ReentrantLock 不是所有的 JDK 版本都支持。并且使用 synchronized 不用担心没有释放锁而导致死锁问题，因为 JVM 会确保锁的释放。
     *
     *
     *
     *
     */


}
