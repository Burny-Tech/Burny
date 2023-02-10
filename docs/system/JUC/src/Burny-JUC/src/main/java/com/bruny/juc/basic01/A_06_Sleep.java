package com.bruny.juc.basic01;

import java.time.LocalDateTime;

/**
 * @author cyx
 * @note
 * @date 2023/2/6 16:32
 */

public class A_06_Sleep {
    public static void main(String[] args) {
        Thread th = new Thread(new MyRunnal());
        th.start();
        System.out.println("main-end");


    }


}

class MyRunnal implements Runnable {
    @Override
    public void run() {
        try {
            System.out.println("sub-start" + LocalDateTime.now());
            Thread.sleep(30000);
            System.out.println("sub-end" + LocalDateTime.now());

        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

    }
}

/**
 * 结果：
 * main-end
 * sub-start2023-02-06T17:25:21.686
 * sub-end2023-02-06T17:25:51.715
 */



