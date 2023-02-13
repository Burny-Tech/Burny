package com.bruny.juc.basic01;

import java.time.LocalDateTime;

/**
 * @author cyx
 * @note
 * 
 */

/**
 * 中断线程的意思是暂停线程执行，而不是终止线程执行
 */

public class A_09_Interrupt {
    public static void main(String[] args) {

        System.out.println("main-start");
        Thread th = new Thread(new InterruptException2());
        th.start();
        while (true) {
            if (th.isInterrupted()) {
                System.out.println("子线程已中断");
            } else {
                th.interrupt();
            }
        }
    }
}


class InterruptException2 implements Runnable {

    @Override
    public void run() {
        System.out.println("sub-start");

        while (true) {
            //Thread.interrupted();
            System.out.println(LocalDateTime.now());
        }

    }
}
/**
 * 结果：
 * 主线程关闭，但是子线程会一直执行，一直打印
 * <p>
 * 子线程已中断
 * 子线程已中断
 * 2023-02-06T18:03:20.819
 * 子线程已中断
 * 子线程已中断
 * 2023-02-06T18:03:20.820
 */
