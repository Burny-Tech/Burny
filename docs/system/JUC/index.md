---
lang: zh-CN
title: JUC
description: JUC
---


[[toc]]


## 线程

### 线程的状态


![线程状态图](/images/system/JUC/001-线程图.png)

###  线程实现方式

#### 实现 Runnable
@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_01_MyRunnable.java)
#### 实现 Callable 并且有返回值
@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_02_Callable.java)
#### 继承 Thread
@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_03_MyThread.java)

### 线程池 Excutor

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01//A_04_Executor.java)
### 守护线程 Daemon
@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_05_DaemonThread.java)

### 单线程操作
#### 线程睡眠 Sleep-超时等待态
@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_06_Sleep.java)

#### 给予其他线程优先调度 Thread.yield()-就绪态

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_07_Yield.java)

#### 中断线程 Thread.interrupt()-中断状态，仅仅是加了个状态位而已


@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_08_Interrupt.java)
@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_09_Interrupt.java)

#### 线程池的中断 Executor.shutdownNow()

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_10_Interrupt_Executor.java)

### 多线程协作
#### 线程的互斥同步 Synchronized-阻塞状态

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_11_Synchronized.java)

#### 线程的互斥同步 ReentrantLock-等待或超时等待

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_12_ReentrantLock.java)
#### 等待线程操作 Thread.join()-等待或超时等待
@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_13_Join.java)

#### 唤醒线程操作 wait notify notifyAll --超时或超时等待-会释放锁

* ``after``方法 先执行，但能保证 ``after``方法 打印晚于``before``方法


* ``wait() 、notify()、 notifyAll()`` 属于``Object``，不属于``Thread`` 
* 只能在同步方法或同步代码块使用，否则会抛出错误
* 使用``wati``挂起期间，线程会释放锁。这是因为，如果没有释放锁，那么其他线程就无法进入对象的同步方法或同步代码块中，那么就无法执行``notify()``或者``notiffyAll()``来唤醒 挂起的线程，造成死锁。

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_14_Wait.java)

结果：

```java
before
after
```

* ``wait()`` 和``sleep()``的区别
  * ``wait()`` 是``Object``的方法，而``sleep()`` 是``Thread``的静态方法
  *  ``wait()``会释放锁，而``sleep()``不会

#### await() signal() signalAll() 

与上一小点 wait() notify() notifyAll() 类似；

  但有以下区别
* 上一小点：属于对象的方法
* 这一小点：属于  ``java.util.concurrent``，并且配合``Condition``可以指定等待的条件，更加灵活

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_15_Await.java)


### Java中所有的锁-理论

![Java主流的锁](/images/system/JUC/002-Java主流锁.png)


#### 悲观锁-乐观锁

**悲观锁：**
* 每次都锁住资源
* 适合 写操作 多于 读操作  的情况
*  ``synchronized`` 和 ``Lock`` 的实现类都是悲观锁  

**乐观锁：** 
* 不锁住资源
* 适合 读操作  多于 写操作  的情况
* JPA中的``@Version`` ,添加一个字段作为版本，需要先读取数据，更新的时候再判断下 version 和现有的version 是否一致 .简称 CAS
@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_16_OptimismPessimismLocks.java)

#### 自旋锁-适应性自旋锁

**-XX:+UseSpinning** JDK6 后默认开启自旋锁

  <iframe src ="https://viewer.diagrams.net/?tags=%7B%7D&target=blank&highlight=0000ff&layers=1&nav=1&title=002-%E8%87%AA%E6%97%8B%E9%94%81%20%E9%80%82%E5%BA%94%E6%80%A7%E8%87%AA%E6%97%8B%E9%94%81.drawio#R5Vpbc6s2EP41ekwGcZUewZd25pxO08l02vPUIbFs04MtF8uxfX59tUIyYOSEpL42eXBgdUHs7qf9dgXyerPNT0W6mP7CRyxHrjPaIK%2BPXJcQR%2F6CYFsK%2FMAtBZMiG5UiXAkesx9MC%2FW4ySobsWWjo%2BA8F9miKXzm8zl7Fg1ZWhR83ew25nnzqYt0wlqCx%2Bc0b0v%2FyEZiqqUedaqGn1k2mepHU%2FPCs9R01oLlNB3xdU3kDZDXKzgX5dVs02M56M7opRw3PNC6W1jB5qLLgPHot%2BJh9mX4JXPEr%2FN48vDX%2BPudnuUlzVf6hfVixdZooOCr%2BYjBJA7yEl6IKZ%2FweZp%2F5XwhhVgK%2F2ZCbLXt0pXgUjQVs1y3jvlc6EZM5H35BDZqKb56Ey1a8lXxzF5Zvl6tSIsJE6%2F0i3b6ln7K%2BIyJYivHFSxPRfbSXEeqPWay61cpVV5ovb5Dx25bx4MQ0SGSPjSIUBKjZAgXMUEkQYMAJQ6ifTQgKJZ9ArggA5RE0ESkJIQLOZb0YJ64j2LVJ5GtPkjkhOXMNFYSiqiPCIZRsY8SrDr7atQQJT01T3u4fLqLYrUeIh9RTujDIg87CFh7Pc0Ee1ykym5ruSd0cYYXVgi2ed0d2ubTA3ZY3Bpw6vt1Bdhdn2kNq75zIot7LR2Btz%2Fq2zmfy3%2FJNeMq6oircru4FLB8C7AkViSSYoWwSOHJuL%2FNJF%2FTJxmuGlpN82wyl9fPUmmskALwzUwGhFg3zLLRKFcGZMvsR%2Fqk5gMTLng2F%2BodgwQF%2Ffc4u45eerIqZtRtd9jTDiLjzrn3PCdqoEPvRp0tpCd%2FgJerdeHj8VK6xr4Jd2v4uFWDm4pAXZFCLwmU0AIUCjGGDj4dYoJXEePcY%2BrhBmDurh4x0fv2wTCX%2BkmeioZxw39WQESVAe6WygKx7IDJYqPMYNrl1UQoFB5pog95YjHls6fV8iJ0I%2FCadMN1ghbdwNhCN3bCo%2BO7zclOwTekfortnzD%2BPjC33%2FR06qa%2Fadxt9d0Jd1%2FacffFB0x6nu2XtvDZe%2FhdEWvl8dLdgWG7wLCJTAZCJXEUZd8RdEnc%2BypPCOCCemo4hYGWFMKHURQryt4D7n5tlH2HGYMhC2XHrgVD4akghNtK%2BiQYwqas8iaIDpDN84DILHMvjZYYiCOVrWKFE4mKQEFIYiBRuXIIaAGcKAhJPFw7GDzfElDOC4Z2FejGEljsdXXqA3zwTE7tWZy6VXB5X7mnHQ7KIEL0zImnoEAg1sA8Q6g3VcPbALKVqOKBXo%2BcFp7uQx%2BiKlNJpFZo0KafToHMERXgAJGydVAbdZDnXRiaOGpC0%2FdJG5rEAk16Mmj6nzZOBR0hXauuXwLSgT1OYcXwVAm2JG1Q03UUtnsAg2tz%2Ff2oFEQXj0rhmV2%2F4fgVDs7v%2BkbNb7t%2BeFHXtxUidiEigL2fDq02vPmqEj6g%2BKqsFIZNPJnq9UfLSqbEuzfidFUm%2FHqVgeVPfD2oBFdNDzsD6r%2BWbdXQuCjSba2DdtCDNsV%2Bs8LkE2fPoOWMxzVvu0phOTH8f4KXvAle6h0VvKdHq3n5%2FcxC1Zo6nTFfY%2B3V3au9EqddN7LRcXIqTuK29XNjmbLrduUWF82UzTIb%2Flymsf1aRhmoZNNT9VV1ipCUnhzB%2FgWkWyWhVVmVQqGVmkSYRLVDCNUEeWsESTdcBPAImR1XX1S0UtprY%2FE%2B3UtgbYcVNsQYtn98Q9pKHp1I4i2BqnOuelHC7tq%2BoOgU840tKrXfDPXrbBr3EtwvipoRLqDkntb%2BgrrR3xzt%2B%2B59sOcmJ%2BCOrq3mcfNkIzDwMKbwLMU%2FE5caB71GeHzA2r7kONLngdcWugLzsobr4UufEbq2%2BkYXBtE6ggJTRWAtDQ584EC4JDjmM9E46lRJhCZFcMqVlMRHGzsEQgRHAWpaGrWsLu0lmqZdioJ%2FZz2e86IKvuMsz%2FdE3XM%2Bmy81Q8YJ3Ckie%2FVMp41mz7Cjujt573cneVt9111ustXH8d7gXw%3D%3D"  width= "780" height="580"  ></iframe>

阻塞或唤醒一个Java线程需要操作系统切换CPU状态来完成，这种状态转换需要耗费处理器时间。如果同步代码块中的内容过于简单，状态转换消耗的时间有可能比用户代码执行的时间还要长。在许多场景中，同步资源的锁定时间很短，为了这一小段时间去切换线程，线程挂起和恢复现场的花费可能会让系统得不偿失。如果物理机器有多个处理器（应该是理解为有空余时间的多核处理器），能够让两个或以上的线程同时并行执行，我们就可以让后面那个请求锁的线程不放弃CPU的执行时间，看看持有锁的线程是否很快就会释放锁。而为了让当前线程“稍等一下”，我们需让当前线程进行自旋，如果在自旋完成后前面锁定同步资源的线程已经释放了锁，那么当前线程就可以不必阻塞而是直接获取同步资源，从而避免切换线程的开销。这就是自旋锁

自旋锁本身是有缺点的，它不能代替阻塞。自旋等待虽然避免了线程切换的开销，但它要占用处理器时间。如果锁被占用的时间很短，自旋等待的效果就会非常好。反之，如果锁被占用的时间很长，那么自旋的线程只会白浪费处理器资源。所以，自旋等待的时间必须要有一定的限度，如果自旋超过了限定次数（默认是10次，可以使用-XX:PreBlockSpin来更改）没有成功获得锁，就应当挂起线程。自旋锁的实现原理同样也是CAS，AtomicInteger中调用unsafe进行自增操作的源码中的do-while循环就是一个自旋操作，如果修改数值失败则通过循环来执行自旋，直至修改成功。


#### 无锁-偏向锁-轻量级锁-重量级锁

* 是属于 synchronized 的范围
  

锁的程度比较
无锁 > 偏向锁 > 轻量级锁  > 重量级锁

#### 公平锁-非公平锁

公平锁
> 指多个线程按照申请所的顺序来获取锁，线程直接进入队列中排队，队列中的第一个线程才能获得锁。
* **优点：** 等待锁的线程不会饿死
* **缺点：** 
  * 整体吞吐效率相对非公平锁要低
  * 等待队列中除第一个线程以外的所有线程都会阻塞，**CPU唤醒阻塞线程的开销比非公平锁大**。

非公平锁
> 多个线程加锁时直接尝试获取锁，获取不到才会到等待队列的队尾等待。但如果此时锁刚好可用，那么这个线程可以无需阻塞直接获取锁，所以非公平锁有可能出现后申请锁的线程先获取锁的场景。
* **优点：** 减少唤起线程的开销，整体吞吐效率高；因为线程有几率不阻塞直接获取锁，CPU不必唤醒所有线程。
* **缺点：** 等待队列中的线程可能会饿死，或者等很久才能获得锁

#### 可重入锁(递归锁)- 非可重入锁

> 可重入： 若一个程序或子程序可以在 任意时刻被中断 ，然后操作系统调度执行另外一段代码

> 可重入锁 又名递归锁，是指同一个线程再外层方法获取锁的时候，再进入该线程的内层方法会自动获取锁（前提锁对象得是同一个对象或class）,不会因为之前已经获取过还没释放而阻塞。  
> ReentrantLock 和 synchronized 都是可重入锁

* **优点：**  可以定程度避免死锁

  

以下代码分析：

两个方法都被内置的锁`synchronized` 修饰的，`before` 方法中调用 `after` 方法。因为内置锁是可重入的，所以同一个线程再调用 after 方法的时候可以直接获得当前的锁，进入 `after` 方法进行操作

如果不是可重入锁，**那么当前线程再调用 B 之前 需要执行 before 获取当前对象的锁释放锁，实际上该对象已被当前线程持有，且无法释放。**所以此时会出现死锁。 

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_17_ReentrantLock.java)

#### 排他锁-共享锁

排他锁

> 该锁一次只能被一个线程持有。如果线程 T 对数据 A 加上排他锁后，则 其他线程不能再对A 加任何类型的锁。获得排他锁的线程即能读又能修改数据 

* synchronized
* JUC的Lock 实现类

以上两个都是排他锁

共享锁

> 锁可被多个线程所持有。如果线程 T 对数据 A 加上共享锁后，则其他线程只能对 A 再加共享锁，不能加排他锁。获得共享锁的线程只能读数据，不能修改数据



### synchronized 详解

#### 注意

* 一把锁只能同时被一个线程获取，没有获得锁的线程只能等待
* 每个实例都对应又自己的一把锁 （`this`） ,不同实例之间互不影响；例外：锁对象是 `*.class`  以及 `synchronized` 修饰的是`static`方法的时候，所有对象公用一把锁
* synchronized 修饰的方法，无论方法正常执行完毕还是抛出异常，都会释放锁


#### 概览锁

* 对象锁
  * 方法锁-this
  * 同步代码块锁
    * this 对象
    * 自定义锁对象
* 类锁
  *  修饰静态的方法
  * 指定多对象为Class对象

#### 对象锁-this

包括方法锁（默认锁对象为this ,当前实例对象） 和 同步代码块锁 （手动指定锁对象）



##### 方法锁形式：synchronized 修饰普通方法，锁对象默认为this.

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_18_MethodLock.java)
结果：

```java
Thread-0  线程开始---
Thread-0  线程结束
Thread-1  线程开始---
Thread-1  线程结束
```
如果 `method()` 方法没有加上 `synchronized` 关键词，则输出的结果如下

```java
Thread-0  线程开始---
Thread-1  线程开始---
Thread-1  线程结束
Thread-0  线程结束
```

或者

```jade
Thread-0  线程开始---
Thread-1  线程开始---
Thread-0  线程结束
Thread-1  线程结束
```



##### 代码块形式：手动指定锁定对象，该对象可以是 this,也可以是自定义锁对象

###### this 对象

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_19_CodeBlock.java)

###### 自定义锁对象

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_20_CusLock.java)

结果：

```java
Thread-0  block1-线程开始--- 
Thread-0  block1-线程结束
Thread-0  block2-线程开始---  
Thread-1  block1-线程开始---
Thread-1  block1-线程结束
Thread-0  block2-线程结束
Thread-1  block2-线程开始---
Thread-1  block2-线程结束

//结果分析

//       线程t1 执行object1 锁 必定要比 t2 执行 Object1 锁早
//    同理
//       线程t1 执行Ojbect2 锁 必定要比 t2 执行 Ojbect2 锁早
//但不保证
//       线程t1 执行object2 锁 要比 t2 执行 object1 锁 早
```



#### 类锁

* 修饰静态的方法
* 指定锁对象为Class对象



##### synchronized 修饰静态的方法

* 不是静态方法的情况：

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_21_ObjectLock.java)

结果：

```java
Thread-0  block1-线程开始---
Thread-1  block1-线程开始---
Thread-1  block1-线程结束
Thread-0  block1-线程结束
```



* 是静态方法的情况：

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_22_ObjectLock.java)

结果：

```java

Thread-0  block1-线程开始---
Thread-0  block1-线程结束
Thread-1  block1-线程开始---
Thread-1  block1-线程结束
```



##### 指定锁对象为Class对象

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_23_ClassLock.java)

结果：

```java
Thread-0  block1-线程开始---
Thread-0  block1-线程结束
Thread-1  block1-线程开始---
Thread-1  block1-线程结束
```



