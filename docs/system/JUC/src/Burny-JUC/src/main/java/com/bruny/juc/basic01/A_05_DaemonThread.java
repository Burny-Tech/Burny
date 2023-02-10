package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note守护线程： 当所有非守护线程结束时，程序也就终止，同时会杀死所有守护线程。
 * @date 2023/2/6 16:19
 */

public class A_05_DaemonThread {
    public static void main(String[] args) {
        Thread th = new Thread(new DaemonThread());
        th.setDaemon(true);
        th.start();
        System.out.println("main-end");
    }


}

class DaemonThread implements Runnable {

    @Override
    public void run() {
        System.out.println("befor++");
        for (int i = 0; i < 5; i++) {
            System.out.println("sub-ing");
        }
        System.out.println("after++");

    }
}

/**
 * 结果：
 * 有时候是
 * main-end
 * <p>
 * 有时候是
 * befor++
 * main-end
 */
