package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note 推荐实现接口方式而不是继承
 * 理由如下：Java不支持多重继承，
 * 类可能只要求可执行就行，继承整个Thread类开销过大
 * 
 */

public class A_01_MyRunnable implements Runnable {

    @Override
    public void run() {
        System.out.println("print");
    }


    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            A_01_MyRunnable my = new A_01_MyRunnable();
            Thread thread = new Thread(my);
            thread.start();
        }
        System.out.println("main-end");

    }

    /**结果：
     *main-end
     * print
     * print
     * print
     * print
     * print
     */

}
