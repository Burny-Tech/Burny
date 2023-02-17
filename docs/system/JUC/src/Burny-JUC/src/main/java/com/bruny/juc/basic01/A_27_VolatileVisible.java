package com.bruny.juc.basic01;

import lombok.extern.slf4j.Slf4j;

import java.util.ArrayList;

/**
 * @author cyx
 * @note
 * @date 2023/2/13 17:31
 */

@Slf4j
public class A_27_VolatileVisible {
    //注意这里没有加上  volatile
    private static boolean stop = false;

    public static void main(String[] args) {

        Runnable r = new Runnable() {

            @Override
            public void run() {

                while (!stop) {
                    log.info("xxxxx");                             //1
                    System.out.println("working");                 //2
                    ArrayList<Integer> b = new ArrayList<>();      //3
                }
                System.out.println(Thread.currentThread().getName() + "  stopped");
            }
        };
        new Thread(r).start();
        try {
            Thread.sleep(3000);
            System.out.println("sleep 3000 ");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        stop = true;

    }
}
