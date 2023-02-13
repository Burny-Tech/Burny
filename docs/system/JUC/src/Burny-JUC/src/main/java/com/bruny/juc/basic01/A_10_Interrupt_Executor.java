package com.bruny.juc.basic01;

import java.time.LocalDateTime;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

/**
 * @author cyx
 * @note 线程池的中断操作
 * 
 */

public class A_10_Interrupt_Executor {
    public static void main(String[] args) {
        ExecutorService executorService = Executors.newCachedThreadPool();
        //创建匿名内部线程

        executorService.execute(() -> {
            //try {
            // Thread.sleep(20000);
            System.out.println("Thread run ..." + LocalDateTime.now());
            //} catch (InterruptedException e) {
            //    throw new RuntimeException(e);
            //}

        });

        interrutTarget();
        executorService.shutdownNow();
        System.out.println("main-end");


    }


    // 如果只想中断Excutor 中的一个线程，可以通过使用submit() 方法来提交一个线程，它会返回一个Future<?>对象，通过该对象的cancel(true)就可以中断线程

    public static void interrutTarget() {

        ExecutorService executorService = Executors.newCachedThreadPool();
        System.out.println("target_inter1");

        Future<Integer> submit = executorService.submit(() -> {
            System.out.println("target_inter");
            return 5;
        });
        System.out.println("target_inter2");

        submit.cancel(true);


    }

}
/**
 * 结果：
 * 当加上Thread.sleep后
 * <p>
 * main-end
 * Exception in thread "pool-1-thread-1" java.lang.RuntimeException: java.lang.InterruptedException: sleep interrupted
 * at com.burny.burnyjuc.thread.basic01.Interrupt_Executor.lambda$main$0(Interrupt_Executor.java:22)
 * at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
 * at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
 * at java.lang.Thread.run(Thread.java:748)
 * Caused by: java.lang.InterruptedException: sleep interrupted
 * at java.lang.Thread.sleep(Native Method)
 * at com.burny.burnyjuc.thread.basic01.Interrupt_Executor.lambda$main$0(Interrupt_Executor.java:19)
 * ... 3 more
 * <p>
 * 不加
 * main-end
 * Thread run ...2023-02-07T09:12:55.563
 * <p>
 * 加上interrutTarget（） 方法后的结果：
 * <p>
 * <p>
 * target_inter1
 * target_inter2
 * main-end
 * Thread run ...2023-02-07T09:25:55.001
 * <p>
 * 进程已结束,退出代码0
 */


/**
 * 加上interrutTarget（） 方法后的结果：
 *
 *
 * target_inter1
 * target_inter2
 * main-end
 * Thread run ...2023-02-07T09:25:55.001
 *
 * 进程已结束,退出代码0
 *
 */



