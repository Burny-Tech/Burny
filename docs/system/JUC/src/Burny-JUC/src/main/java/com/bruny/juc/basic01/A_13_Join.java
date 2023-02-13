package com.bruny.juc.basic01;

/**
 * @author cyx
 * @note 线程之间的协作 -Join
 * 
 */

/**
 * join 会将当前线程挂起,而不是忙等待
 */

public class A_13_Join {

    public class A extends Thread {

        @Override
        public void run() {
            System.out.println("A");
        }
    }

    public class B extends Thread {

        private A a;

        B(A a) {
            this.a = a;
        }


        @Override
        public void run() {

            try {
                a.join();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.println("B");
        }
    }


    public void test() {
        A a = new A();
        B b = new B(a);
        b.start();
        a.start();
    }

    public static void main(String[] args) {
        A_13_Join join = new A_13_Join();
        join.test();
    }


}
