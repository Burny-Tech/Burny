package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note
 * @date 2023/2/6 17:28
 */

/**
 * 中断线程 是暂时暂停线程执行，而不是终止线程执行
 * 中断线程：
 * thread1.interrupt();
 * 线程处于阻塞时，调用该方法，则会抛出中断异常
 * <p>
 * <p>
 * 线程的run方法无限循环，
 */
public class A_08_Interrupt {

    public static void main(String[] args) {
        Thread th = new Thread(new InterruptException());
        th.start();
        if (!th.isInterrupted()) {
            th.interrupt();
        } else {
            System.out.println("线程已经中断");
        }
        System.out.println("main-end");

    }


}

class InterruptException implements Runnable {

    @Override
    public void run() {
        try {
            System.out.println("before--");
            Thread.sleep(3000);
            System.out.println("after--");
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
/**
 * 结果：
 * main-end
 * before--
 * Exception in thread "Thread-0" java.lang.RuntimeException: java.lang.InterruptedException: sleep interrupted
 * at com.burny.burnyjuc.thread.basic01.InterruptException.run(Interrupt_08.java:42)
 * at java.lang.Thread.run(Thread.java:748)
 * Caused by: java.lang.InterruptedException: sleep interrupted
 * at java.lang.Thread.sleep(Native Method)
 * at com.burny.burnyjuc.thread.basic01.InterruptException.run(Interrupt_08.java:39)
 * ... 1 more
 */



