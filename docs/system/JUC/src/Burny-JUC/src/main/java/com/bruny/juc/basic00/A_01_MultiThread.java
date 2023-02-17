package com.bruny.juc.basic00;

import lombok.SneakyThrows;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

/**
 * @author cyx
 * @note
 * @date 2023/2/16 15:47
 */

public class A_01_MultiThread {
    private int i = 0;
    public void addI (){
        i++;
    }
    public int getI(){
        return i;
    }

    @SneakyThrows
    public static void main(String[] args) {
        int size =1000;
        A_01_MultiThread bean = new A_01_MultiThread();
        final CountDownLatch  countDownLatch = new CountDownLatch(size);
        ExecutorService executorService = Executors.newCachedThreadPool();
        for (int i = 0; i < size; i++) {
            executorService.execute(()->{
                bean.addI();
                countDownLatch.countDown();
            });
        }
        countDownLatch.await();
        executorService.shutdown();
        System.out.println(bean.getI());

    }
}
