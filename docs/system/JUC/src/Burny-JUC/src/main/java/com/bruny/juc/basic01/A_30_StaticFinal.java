package com.bruny.juc.basic01;

import java.util.Random;

/**
 * @author cyx
 * @note
 * @date 2023/2/14 10:10
 */

public class A_30_StaticFinal {

    static Random r = new Random();
    final   int k = r.nextInt(9000);
    static  final  int  t = r.nextInt(10);



    public static void main(String[] args) {
        A_30_StaticFinal bean  = new A_30_StaticFinal();
        System.out.println(bean.k);
        System.out.println(A_30_StaticFinal.t);
        A_30_StaticFinal bean2  = new A_30_StaticFinal();
        System.out.println(bean2.k);
        System.out.println(A_30_StaticFinal.t);




    }
}
