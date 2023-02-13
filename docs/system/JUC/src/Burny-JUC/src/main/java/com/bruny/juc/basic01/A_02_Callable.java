package com.bruny.juc.basic01;

import lombok.SneakyThrows;

import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;

/**
 * @author cyx
 * @note
 * 
 */


public class A_02_Callable implements Callable<Integer> {

    @Override
    public Integer call() throws Exception {
        return null;
    }

    @SneakyThrows
    public static void main(String[] args) {
        A_02_Callable call = new A_02_Callable();
        FutureTask<Integer> ft = new FutureTask<>(call);
        Thread th = new Thread(ft);
        th.start();
        System.out.println(ft.get());
    }

    /**结果：
     *null
     */
}
