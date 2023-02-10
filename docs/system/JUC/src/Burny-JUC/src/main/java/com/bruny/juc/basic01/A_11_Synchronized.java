package com.bruny.juc.basic01;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * @author cyx
 * @note 线程的互斥同步：
 * Java 提供了两种锁机制来控制多个线程对共享资源的互斥访问，第一个是 JVM 实现的 synchronized，而另一个是 JDK 实现的 ReentrantLock。
 * 同步代码块
 * synchronized 它只作用于同一个对象，如果调用两个对象上的同步代码块，就不会进行同步。
 * @date 2023/2/7 9:39
 */

public class A_11_Synchronized {

    public static void main(String[] args) {
        A_11_Synchronized syn = new A_11_Synchronized();
        ExecutorService executorService = Executors.newCachedThreadPool();


        //1 同步代码块
        //1.1 不使用 synchronized 的情况下
        //输出结果:
        //0	1	2	3	4	5	6	7	8	9	10	11	12	13	0	1	2	3	4	5	6	7	14	8	15	9	16	10	17	11	18	12	19	13	20	21	14	22	23	24	25	26	15	27	28	29	30	31	32	33	34	35	36	37	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	37	60	38	61	39	62	40	63	64	41	65	42	66	43	67	44	45	46	47	48	49	50	68	51	69	52	70	53	71	54	72	55	73	56	74	57	75	58	76	59	77	60	78	61	79	62	80	63	81	64	82	65	83	66	84	67	85	86	68	87	69	88	70	89	71	90	72	91	73	92	74	93	75	94	76	95	77	96	78	97	79	98	80	99	81	82
        //
        //83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99
        executorService.submit(() -> {
            syn.fun1("one");
        });
        executorService.submit(() -> {
            syn.fun1("one");
        });
        //1.2.对于以下代码，synchronized 作用于同一个对象，因此两个子线程是同步的。
        //输出结果:
        //four0	four1	four2	four3	four4	four5	four6	four7	four8	four9	four10	four11	four12	four13	four14	four15	four16	four17	four18	four19	four20	four21	four22	four23	four24	four25	four26	four27	four28	four29	four30	four31	four32	four33	four34	four35	four36	four37	four38	four39	four40	four41	four42	four43	four44	four45	four46	four47	four48	four49	four50	four51	four52	four53	four54	four55	four56	four57	four58	four59	four60	four61	four62	four63	four64	four65	four66	four67	four68	four69	four70	four71	four72	four73	four74	four75	four76	four77	four78	four79	four80	four81	four82	four83	four84	four85	four86	four87	four88	four89	four90	four91	four92	four93	four94	four95	four96	four97	four98	four99
        //
        //four0	four1	four2	four3	four4	four5	four6	four7	four8	four9	four10	four11	four12	four13	four14	four15	four16	four17	four18	four19	four20	four21	four22	four23	four24	four25	four26	four27	four28	four29	four30	four31	four32	four33	four34	four35	four36	four37	four38	four39	four40	four41	four42	four43	four44	four45	four46	four47	four48	four49	four50	four51	four52	four53	four54	four55	four56	four57	four58	four59	four60	four61	four62	four63	four64	four65	four66	four67	four68	four69	four70	four71	four72	four73	four74	four75	four76	four77	four78	four79	four80	four81	four82	four83	four84	four85	four86	four87	four88	four89	four90	four91	four92	four93	four94	four95	four96	four97	four98	four99
        executorService.submit(() -> {
            syn.fun2("two");
        });
        executorService.submit(() -> {
            syn.fun2("two");
        });


        //1.3. 使用了synchronized 但是使用不了不同对象 的情况下
        //对于以下代码，synchronized 作用于不同对象，因此两个子线程是不同步的。
        //输出结果:
        //0	1	2	3	4	5	6	7	8	9	10	11	12	13	0	1	2	3	4	5	6	7	14	8	15	9	16	10	17	11	18	12	19	13	20	21	14	22	23	24	25	26	15	27	28	29	30	31	32	33	34	35	36	37	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	37	60	38	61	39	62	40	63	64	41	65	42	66	43	67	44	45	46	47	48	49	50	68	51	69	52	70	53	71	54	72	55	73	56	74	57	75	58	76	59	77	60	78	61	79	62	80	63	81	64	82	65	83	66	84	67	85	86	68	87	69	88	70	89	71	90	72	91	73	92	74	93	75	94	76	95	77	96	78	97	79	98	80	99	81	82
        //
        //83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99
        A_11_Synchronized syn2 = new A_11_Synchronized();
        executorService.submit(() -> {
            syn.fun2("two");
        });
        executorService.submit(() -> {
            syn2.fun2("two");
        });

        //2. 同步一个方法

        executorService.submit(() -> syn.fun3("three"));


        //3. 同步一个类 ,作用于整个类，也就是说两个线程调用同一个类的不同对象上的这种同步语句，也会进行同步
        //输出结果:
        //four0	four1	four2	four3	four4	four5	four6	four7	four8	four9	four10	four11	four12	four13	four14	four15	four16	four17	four18	four19	four20	four21	four22	four23	four24	four25	four26	four27	four28	four29	four30	four31	four32	four33	four34	four35	four36	four37	four38	four39	four40	four41	four42	four43	four44	four45	four46	four47	four48	four49	four50	four51	four52	four53	four54	four55	four56	four57	four58	four59	four60	four61	four62	four63	four64	four65	four66	four67	four68	four69	four70	four71	four72	four73	four74	four75	four76	four77	four78	four79	four80	four81	four82	four83	four84	four85	four86	four87	four88	four89	four90	four91	four92	four93	four94	four95	four96	four97	four98	four99
        //
        //four0	four1	four2	four3	four4	four5	four6	four7	four8	four9	four10	four11	four12	four13	four14	four15	four16	four17	four18	four19	four20	four21	four22	four23	four24	four25	four26	four27	four28	four29	four30	four31	four32	four33	four34	four35	four36	four37	four38	four39	four40	four41	four42	four43	four44	four45	four46	four47	four48	four49	four50	four51	four52	four53	four54	four55	four56	four57	four58	four59	four60	four61	four62	four63	four64	four65	four66	four67	four68	four69	four70	four71	four72	four73	four74	four75	four76	four77	four78	four79	four80	four81	four82	four83	four84	four85	four86	four87	four88	four89	four90	four91	four92	four93	four94	four95	four96	four97	four98	four99
        executorService.submit(() -> syn.fun4("four"));
        executorService.submit(() -> syn2.fun4("four"));

        executorService.shutdown();


    }

    public void fun1(String name) {
        for (int i = 0; i < 100; i++) {
            System.out.print(name + i + "\t");
        }
        System.out.println("\n");
    }

    public void fun2(String name) {
        synchronized (this) {
            for (int i = 0; i < 100; i++) {
                System.out.print(name + i + "\t");
            }
            System.out.println("\n");

        }
    }

    //
    public synchronized void fun3(String name) {
        for (int i = 0; i < 100; i++) {
            System.out.print(name + i + "\t");
        }
        System.out.println("\n");
    }

    public synchronized void fun4(String name) {
        synchronized (A_11_Synchronized.class) {
            for (int i = 0; i < 100; i++) {
                System.out.print(name + i + "\t");
            }
            System.out.println("\n");
        }
    }
}

/**
 * fun1() 结果：
 * 0	1	2	3	4	5	6	7	0	8	1	9	2	10	3	11	4	5	6	7	8	9	10	11	12	12	13	13	14	14	15	15	16	16	17	17	18	18	19	19	20	20	21	21	22	22	23	24	23	25	24	26	25	27	26	28	27	29	28	30	29	31	30	32	31	33	32	34	33	35	34	36	35	37	36	38	37	39	38	40	39	41	40	41	42	42	43	43	44	44	45	46	45	47	46	48	47	49	48	50	49	51	50	52	51	53	52	54	53	55	54	56	55	57	56	58	57	59	58	59	60	60	61	61	62	63	64	65	66	67	68	62	69	70	71	63	72	64	73	74	65	75	66	76	67	77	78	79	80	81	82	83	68	69	70	71	72	73	74	84	75	85	76	86	77	87	78	79	80	81	82	83	84	85	88	86	89	87	90	88	91	89	90	91	92	92	93	93	94	95	96	97	98	99
 * <p>
 * 94	95	96	97	98	99
 * fun2() 结果：
 * 0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	60	61	62	63	64	65	66	67	68	69	70	71	72	73	74	75	76	77	78	79	80	81	82	83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99
 * 0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	60	61	62	63	64	65	66	67	68	69	70	71	72	73	74	75	76	77	78	79	80	81	82	83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99
 */
