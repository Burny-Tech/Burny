package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note
 * @date 2023/2/6 15:53
 */

public class A_03_MyThread extends Thread {

    /**
     * 一定要以run命名
     */
    public void run() {
        System.out.println("eee");
    }

    public static void main(String[] args) {
        A_03_MyThread th = new A_03_MyThread();
        th.start();
    }


}

/**
 * 结果：
 * eee
 */
