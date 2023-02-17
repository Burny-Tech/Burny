package com.bruny.juc.basic01;

import org.springframework.boot.autoconfigure.ldap.embedded.EmbeddedLdapProperties;

/**
 * @author cyx
 * @note 单例模式实现方法之一
 * @date 2023/2/13 16:04
 */

public class A_25_VolatileSingleton {

    public static  volatile   A_25_VolatileSingleton instance;

    //禁止外部实例化
    private A_25_VolatileSingleton(){};

    public  static A_25_VolatileSingleton getInstance(){
        if (instance == null){
            synchronized (A_25_VolatileSingleton.class){
                if (instance == null){
                    instance = new A_25_VolatileSingleton();
                }
            }

        }
        return  instance;
    }
}
