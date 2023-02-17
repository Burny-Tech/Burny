---
lang: zh-CN
title: JUC
description: JUC
---

[[toc]]

## 理论

### 需要多线程的原因

CPU , 内存,  I/O 设备的读写速读是有极大差异的,为了合理利用CPU的高性能,

1、 CPU 增加了缓存 ,即 Cache ,以均衡与内存的速读差异;
2、 操作系统增加了进程,线程,以分时复用CPU ,进而均衡CPU与I/O设备的
3、 编译程序优化指令执行次序,使得缓存能够得到更加合理地利用

分别导致的问题

1、可见性: 一个线程修改了共享变量，另一个线程不能立刻看到，CPU缓存引起
2、原子性: 对于一个操作或者多个操作,要么全部执行,要么全部不执行.
3、有序性: 为了效率,代码进行编译的时候,JVM可能对代码进行重排序.

#### 可见性

```java
int i = 0;
//线程1执行的代码
i = 10;
 
//线程2执行的代码
j = i;

```
多核CPU中,线程1 执行将i 设置为10 ,线程1 将 i 缓存到了Cache ,此时,另一核的CPU 从 **主存** 中 读取到I  还是 0 ,是因为线程1 中没有及时地将10 写入到主存中.



#### 原子性

```java

i++; 

```
最主要还是 `` i++`` ,这个操作不是原子性操作.需要经过以下几步

1. 将变量 i 从内存读取到 CPU寄存器；
2. 在CPU寄存器中执行 i + 1 操作；
3. 将最后的结果i写入内存（缓存机制导致可能写入的是 CPU 缓存而不是内存）。
.....
由于CPU分时复用（线程切换）的存在，线程1执行了第一条指令后，就切换到线程2执行，假如线程2执行了这三条指令后，再切换会线程1执行后续两条指令，将造成最后写到内存中的i值是2而不是3
#### 有序性

有序性：即程序执行的顺序按照代码的先后顺序执行。举个简单的例子，看下面这段代码：

```java
int i = 0;
boolean flag = false;
i = 1;                //语句1  
flag = true;          //语句2
```

上面代码定义了一个int型变量，定义了一个boolean类型变量，然后分别对两个变量进行赋值操作。从代码顺序上看，语句1是在语句2前面的，那么JVM在真正执行这段代码的时候会保证语句1一定会在语句2前面执行吗? 不一定，为什么呢? 这里可能会发生指令重排序（Instruction Reorder）。

在执行程序时为了提高性能，编译器和处理器常常会对指令做重排序。重排序分三种类型：

- 编译器优化的重排序。编译器在不改变单线程程序语义的前提下，可以重新安排语句的执行顺序。
- 指令级并行的重排序。现代处理器采用了指令级并行技术（Instruction-Level Parallelism， ILP）来将多条指令重叠执行。如果不存在数据依赖性，处理器可以改变语句对应机器指令的执行顺序。
- 内存系统的重排序。由于处理器使用缓存和读 / 写缓冲区，这使得加载和存储操作看上去可能是在乱序执行。

从 java 源代码到最终实际执行的指令序列，会分别经历下面三种重排序：

![img](https://pdai.tech/images/jvm/java-jmm-3.png)

上述的 1 属于编译器重排序，2 和 3 属于处理器重排序。这些重排序都可能会导致多线程程序出现内存可见性问题。对于编译器，JMM 的编译器重排序规则会禁止特定类型的编译器重排序（不是所有的编译器重排序都要禁止）。对于处理器重排序，JMM 的处理器重排序规则会要求 java 编译器在生成指令序列时，插入特定类型的内存屏障（memory barriers，intel 称之为 memory fence）指令，通过内存屏障指令来禁止特定类型的处理器重排序（不是所有的处理器重排序都要禁止）




### 多线程导致问题实例

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic00/A_01_MultiThread.java)

输出结果:总是小于 1000 

```java
995
```

### 线程安全的实现方法

##### 互斥和同步-阻塞同步-悲观策略

synchronized 和 ReentrantLock
##### 非阻塞同步-乐观策略

1. CAS - 比较并交换- 直接操作内存原子性操作  

1.1  什么是CAS?  

CAS(compare and swap)的缩写，中文翻译成比较并交换,实现并发算法时常用到的一种技术。它包含三个操作数——内存位置、预期原值及更新值。执行CAS操作的时候，将内存位置的值与预期原值比较:如果相匹配，那么处理器会自动将该位置值更新为新值，如果不匹配，处理器不做任何操作，多个线程同时执行CAS操作只有一个会成功。

1.2 CAS原理  

CAS有3个操作数，位置内存值V，旧的预期值A，要修改的更新值B。当且仅当旧的预期值A和内存值V相同时，将内存值V修改为B，否则什么都不做或重试。它重试的这种行为称为自旋! 原理有点类似乐观锁，修改带版本号。

  <iframe src ="https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&layers=1&nav=1&title=006-CAS-01#RzVfbjpswEP2aeawEhnB55Jau2q5aNdJW6ps3eIEKcOSYkOzXdwATQiBpVuoq%2B5KMDzNj%2B8zMIQEjKPafBd2kjzxmORAt3oMRAiG26%2BBnAxw6wHAWHZCILO4gfQBW2StToKbQKovZduQoOc9lthmDa16WbC1HGBWC12O3F56Pd93QhE2A1ZrmU%2FRXFsu0Q03dGPAHliWp2pm4KqCgva%2B6yDalMa9PICMCIxCcy84q9gHLG%2Bp6Wrq45YWnx3MJVspbAuyv5pfw5YH9pvT7z%2BWP15DXj59sdTZ56O%2FLYry%2BWpa8xC9f8KqMWZNGwxUXMuUJL2n%2BjfMNgjqCf5iUB1U8WkmOUCqLXD3tNmkyXzy7gra8Emt25cB9C1CRMHnFjxwZxsZkvGBSHDBOsJzKbDc%2BB1Utkhz9BhrRUEy%2BgVWVd0fzSu0UeCuIHPCW4NsQWeDr4BCIFuAsW8MCdwE%2BFtDK8Vb%2Bs0ArkS1158gTZm4jLcBRQsMLAYcMDTdoUjRGCM5MLq%2BNxK1s8PAUNrgeOCZELnikNawmhbtss2vgB9MUfp%2FCUlspv7MmGjqmKX%2BdZpKtNrQtbI0qMdcdOyYk21%2Fvj2k9lagQpSn1MKG6qeYuPZlOV3unii8mFW%2F59cF3GgNL5LhXWLr%2FXJEb58q451xZMyybDcVOeAPdH1zZbq2Aec8KkJkKnAvPkyqKF55oTK8UjXa0Oth4a%2BBZrYHyE1xSpyuR%2F56wlBfP1fZ9NUgFEM2%2BTYSO4H%2BvjjGvQiZ4jj8mEmkzjzr%2BNPPymPJ%2FN41XAWZP20fRfPOaGp1zfHf6iG6P6dO0KX9khj%2Fr7fzhcvhd2z47%2BW9gRH8B"  width= "780" height="580"  ></iframe>


CAS是JDK提供的非阻塞原子性操作，它通过硬件保证了比较-更新的原子性。它是非阻塞的且自身具有原子性，也就是说这玩意效率更高且通过硬件保证，说明它更可靠。 

CAS是一条CPU的原子指令(`cmpxchg`指令），不会造成所谓的数据不一致问题，`Unsafe`提供的`CAS`方法（如`compareAndSwapXXX`）底层实现即为CPU指令cmpxchg.  

执行`cmpxchg`指令的时候，会判断当前系统是否为多核系统，如果是就给总线加锁，只有一个线程会对总线加锁成功，加锁成功之后会执行`cas`操作，也就是说`CAS`的原子性实际上是CPU实现独占的，比起用`synchronized`重量级锁，这里的排他时间要短很多，所以在多线程情况下性能会比较好。

```java

 //  Unsafe.class
    public final native boolean compareAndSwapObject(Object var1, long var2, Object var4, Object var5);

    public final native boolean compareAndSwapInt(Object var1, long var2, int var4, int var5);

    public final native boolean compareAndSwapLong(Object var1, long var2, long var4, long var6);

    /*
    * var1 表示要操作的对象
    * var2 表示要操作对象中属性地址的偏移量
    * var4 表示需要修改数据的期望值
    * var5/var8 表示需要修改为新的值
    */
```

原子类靠的是`CAS`思想，`CAS`思想实现靠的是`Unsafe`类。工作中尽量不要使用`UnSafe`类，使用不当容易出现大问题。


```java

public class AtomicInteger extends Number implements java.io.Serializable {
    private static final long serialVersionUID = 6214790243416807050L;

    // setup to use Unsafe.compareAndSwapInt for updates
    private static final Unsafe unsafe = Unsafe.getUnsafe();
    private static final long valueOffset;

    static {
        try {
            valueOffset = unsafe.objectFieldOffset
                (AtomicInteger.class.getDeclaredField("value"));
        } catch (Exception ex) { throw new Error(ex); }
    }

    private volatile int value;
```

以原子类`AtomicIntefer`为例

`Unsafe`类是`CAS`的核心类，由于`Java`方法无法直接访问底层系统，需要通过本地(`native`)方法来访问，`Unsafe`相当于一个后门，基于该类可以直接操作特定内存的数据。`Unsafe`类存在于`sun.misc`包中，其内部方法操作可以像C的指针一样直接操作内存，因为`Java`中`CAS`操作的执行依赖于`Unsafe`类的方法。
注意`Unsafe`类中的所有方法都是`native`修饰的，也就是说`Unsafe`类中的方法都直接调用操作系统底层资源执行相应任务。

变量`valueOffset`，表示该变量值在内存中的偏移地址，因为`Unsafe`就是根据内存偏移地址获取数据的。

变量`value`用`volatile`修饰，保证了多线程之间的内存可见性。 

我们知道i++线程不安全的， `` atomicInteger.getAndIncrement() ``  是线程安全的

CAS的全称为 `Compare-And-Swap`，它是一条CPU并发原语。 
它的功能是判断内存某个位置的值是否为预期值，如果是则更改为新的值，这个过程是原子的。
`Atoniclnteger`类主要利用`CAS(compare and swap) + volatile`和 `native`方法来保证原子操作，从而避免 `synchronized`的高开销，执行效率大为提升。

```java
AtomicInteger的getAndIncrement()

    public final int getAndIncrement() {
        return unsafe.getAndAddInt(this, valueOffset, 1);
    }
Unsafe的getAndAddInt()

    public final int getAndAddInt(Object var1, long var2, int var4) {
        int var5;
        do {
            var5 = this.getIntVolatile(var1, var2);
        } while(!this.compareAndSwapInt(var1, var2, var5, var5 + var4));

        return var5;
    }
```
此处复习一下do while循环，因为工作中不太常用
do {
循环体语句；
} while（条件判断语句）；

执行流程：
执行循环体语句
执行条件判断语句，看其结果是true还是false
如果是false，循环结束
如果是true，回到循环体语句继续循环。

`do while` 循环第一次会不经过判断直接执行一次循环体，这与for循环和while循环都不相同。

`CAS`并发原语体现在`JAVA`语言中就是`sun.misc.Unsafe`类中的各个方法。调用UnSafe类中的CAS方法，JVM会帮我们实现出`CAS`汇编指令。这是一种完全依赖于硬件的功能，通过它实现了原子操作。再次强调，由于CAS是一种系统原语，原语属于操作系统用语范畴，是由若干条指令组成的，用于完成某个功能的一个过程，并且原语的执行必须是连续的，在执行过程中不允许被中断，也就是说CAS是一条CPU的原子指令，不会造成所谓的数据不一致问题。

假设线程A和线程B两个线程同时执行`getAndAddInt`操作（分别跑在不同CPU上):

`AtomicInteger`里面的`value`原始值为`3`，即主内存中`AtomicInteger i`的`value`为3，根据`JMM`模型，线程A和线程B各自持有一份值为3的`value`的副本分别到各自的工作内存。

线程A通过`getIntVolatile`(`var1`, `var2`)拿到value值3，这时线程A被挂起。

线程B也通过`getIntVolatile`(`var1`, `var2`)方法获取到value值3，此时刚好线程B没有被挂起并执行`compareAndSwaplnt`方法比较内存值也为3，成功修改内存值为4，线程B打完收工，一切`OK`。

这时线程A恢复，执行`compareAndSwapInt`方法比较，发现自己手里的值数字3和主内存的值数字4不一致，说明该值已经被其它线程抢先一步修改过了，那A线程本次修改失败，只能重新读取重新来一遍了。

线程A重新获取`value`值，因为变量`value`被`volatile`修饰，所以其它线程对它的修改，线程A总是能够看到，线程A继续执行`compareAndSwapInt`进行比较替换，直到成功。


1.3 原子更新引用类  

原子更新基本类型的AtomicInteger,只能更新一个变量，如果要原子更新多个变量，就要使用这个原子更新引用类型提供的类。

```java
public class AtomicReferenceTest {
    public static void main(String[] args) {
        Cat cat1 = new Cat("狸花",1);
        Cat cat2 = new Cat("奶牛",2);
        Cat cat3 = new Cat("大橘",3);
        AtomicReference<Cat> reference = new AtomicReference<>(cat1);
        new Thread(()->{
            System.out.println(reference.compareAndSet(cat1,cat2)+":"+reference.get());
        }).start();
        new Thread(()->{
            System.out.println(reference.compareAndSet(cat1,cat3)+":"+reference.get());
        }).start();
    }
}
class Cat{
    private String color;
    private  int age;

    public Cat(String color, int age) {
        this.color = color;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Cat{" +
                "color='" + color + '\'' +
                ", age=" + age +
                '}';
    }
}
```

1.4 CAS与自旋锁  

自旋锁(spinlock)，借鉴CAS思想，CAS是实现自旋锁的基础，CAS利用CPU指令保证了操作的原子性，以达到锁的效果，至于自旋呢，看字面意思也很明白，自己旋转。是指尝试获取锁的线程不会立即阻塞，而是采用循环的方式去尝试获取锁，当线程发现锁被占用时，会不断循环判断锁的状态，直到获取。这样的好处是减少线程上下文切换的消耗，缺点是循环会消耗CPU

CAS是实现自旋锁的基础，自旋俗称循环或者递归，一般是用一个无限循环实现。这样一来，一个无限循环中，执行一个CAS操作，当操作成功返回 true 时，循环结束;当返回 false 时，接着执行循环，继续尝试CAS操作，直到返回true。

自旋锁代码
```java
public class SpinLockTest {
    AtomicReference<Thread> reference = new AtomicReference<>();

    public static void main(String[] args) {
        SpinLockTest spinLockTest = new SpinLockTest();
        new Thread(() -> {
            spinLockTest.lock();
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            spinLockTest.unLock();
        }, "A").start();
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        new Thread(() -> {
            System.out.println("B进入时间" + System.currentTimeMillis());
            spinLockTest.lock();
            System.out.println("B拿到锁时间" + System.currentTimeMillis());
            spinLockTest.unLock();
        }, "B").start();
    }

    private void lock() {
        Thread thread = Thread.currentThread();
        while (!(reference.compareAndSet(null, thread))) {
        };
        System.out.println("当前持有锁的线程：" + thread.getName());
    }

    private void unLock() {
        Thread thread = Thread.currentThread();
        while (!(reference.compareAndSet(thread, null))) {
        };
        System.out.println("当前释放锁的线程：" + thread.getName());
    }
}
```

1.5 ABA问题  

CAS缺点
* 循环时间长开销很大。
* 引出来ABA问题

如果CAS失败，会一直进行尝试。如果CAS长时间一直不成功，可能会给CPU带来很大的开销。


CAS算法实现一个重要前提是取出内存中某时刻的数据并在当下时刻比较并替换，那么在这个时间差类会导致数据的变化。

比如说一个线程1从内存位置V中取出A，这时候另一个线程2也从内存中取出A，并且线程2进行了一些操作将值变成了B，然后线程2又将V位置的数据变成A，这时候线程1进行CAS操作发现内存中仍然是A，预期OK，然后线程1操作成功。

尽管线程1的CAS操作成功，但是不代表这个过程就是没有问题的。

一句话解决 ABA:比较+版本号

版本号时间戳原子引用AtomicStampedReference

ABA问题解决代码
```java
public class AtomicStampedReferenceTest {
    public static void main(String[] args) {
        Cat cat1 = new Cat("狸花",1);
        Cat cat2 = new Cat("奶牛",2);
        Cat cat3 = new Cat("大橘",3);
        AtomicStampedReference<Cat> reference = new AtomicStampedReference<>(cat1,1);
        new Thread(()->{
            try {
                Thread.sleep(200);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("线程A修改结果"+reference.compareAndSet(cat1, cat2, reference.getStamp(), reference.getStamp()+1)+",stamp:"+reference.getStamp());
            reference.compareAndSet(cat2,cat1,reference.getStamp(),reference.getStamp()+1);
        },"A").start();

        new Thread(()->{
            int stamp = reference.getStamp();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("线程B修改结果"+reference.compareAndSet(cat1, cat3, stamp, stamp + 1)+",stamp:"+reference.getStamp());
        },"B").start();
    }
}
```
每次操作后版本号每次必须改变，要么递增，要么递减，需要保持一致，不能有的线程增有的线程减。



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
锁可以升级但是不可降级
**目的：**为了提供获取锁和释放锁的效率

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

> 可重入： 若一个程序或子程序可以在 任意时刻被中断 ，然后操作系统调度执行另外一段代码,这端代码又调用了该子程序灰灰出错，则称其为 可重入 ；即当该子程序正在运行时，执行线程可以再次我、进入并执行它，仍然获得符合设计时预期的结果。与多线程并发执行的线程安全不同，可重入强调对单个线程执行时重新进入同一个子程序仍然时安全的。

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_24_ReentrantLock.java)

> 可重入锁 又名递归锁，是指同一个线程再外层方法获取锁的时候，再进入该线程的内层方法会自动获取锁（前提锁对象得是同一个对象或class）,不会因为之前已经获取过还没释放而阻塞。  
> ReentrantLock 和 synchronized 都是可重入锁

* **优点：**  可以定程度避免死锁

  

以下代码分析：

两个方法都被内置的锁`synchronized` 修饰的，`before` 方法中调用 `after` 方法。因为内置锁是可重入的，所以同一个线程再调用 after 方法的时候可以直接获得当前实例锁，进入 `after` 方法进行操作

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



### Synchronized 详解

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



#### synchronized 和Lock

##### synchronized的缺点

- `效率低`：锁的释放情况少，只有代码执行完毕或者异常结束才会释放锁；试图获取锁的时候不能设定超时，不能中断一个正在使用锁的线程，相对而言，Lock可以中断和设置超时
- `不够灵活`：加锁和释放的时机单一，每个锁仅有一个单一的条件(某个对象)，相对而言，读写锁更加灵活
- `无法知道是否成功获得锁`，相对而言，Lock可以拿到状态，可以做到 ：如果成功获取锁，做某操作，如果获取失败，做某操作。

#####  Lock解决相应问题

主要看里面的4个方法:

- `lock()`: 加锁
- `unlock()`: 解锁
- `tryLock()`: 尝试获取锁，返回一个boolean值
- `tryLock(long,TimeUtil)`: 尝试获取锁，可以设置超时

Synchronized加锁只与一个条件(是否获取锁)相关联，不灵活，后来`Condition与Lock的结合`解决了这个问题。

多线程竞争一个锁时，其余未得到锁的线程只能不停的尝试获得锁，而不能中断。高并发的情况下会导致性能下降。ReentrantLock的lockInterruptibly()方法可以优先考虑响应中断。 一个线程等待时间过长，它可以中断自己，然后ReentrantLock响应这个中断，不再让这个线程继续等待。有了这个机制，使用ReentrantLock时就不会像synchronized那样产生死锁了



### Volatile详解

* 解决可见性 
* 解决指令重排序

#### 解决指令重排序


@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_25_VolatileSingleton.java)

* 对于此单例模式来说，解决同步性是依靠 synchronized
**题外话-双检索**

第一个`if`语句，用来确认调用`getInstance`()时`instance`是否为空，如果不为空即已经创建，则直接返回，如果为空，那么就需要创建实例，于是进入`synchronized`同步块。`synchronized`加类锁，确保同时只有一个线程能进入，进入以后进行第二次判断，是因为，对于首个拿锁者，它的时段`instance`肯定为`null`，那么进入`new Singleton()`对象创建，而在**首个拿锁者的创建对象期间**，可能有其他线程同步调用`getInstance()`，那么它们也会通过`if`进入到同步块试图拿锁然后阻塞。这样的话，当首个拿锁者完成了对象创建，之后的线程都不会通过第一个`if`了，而这期间阻塞的线程开始唤醒，它们则需要靠第二个if语句来避免再次创建对象。以上就是**双检索的实现思路**，`synchronized`与第二个`if`即是用来保证线程安全与不产生第二个实例，也是`Double_Checked_Lock（DCL）`由来。  

* 解决指令重排序  

指令重排序主要体现在instance = new Singleton()这条语句上了。

这条语句显然是个复合操作，可以简单分下，（已完成类加载 ，假设在堆上分配内存）

实例化一个对象可以分为三个步骤：   

1.在堆中分配对象内存  

2.填充对象必要信息+具体数据初始化+末位填充  

3.将引用指向这个对象的堆内地址  

那么，在完成1后，对象的大小和地址已经确定，但是由于系统可以 **对指令进行重排序** ，因此，2和3存在指令重排序的可能。  

并且可以看到，3的操作明显比2要少，那么如果让2与3一起执行，并且反应到具体的顺序上变成了1-3-2.  

先完成3，引用变量instance先指向了在堆中给对象分配的空间，然后2仍在慢慢吞吞继续。  

这时候，被synchronized挡在外面的阻塞线程其实是不会有什么影响的，因为一定会等到对象创建完，首个拿锁者才会释放锁。  

那么关键是在，此刻如果在3完成而2未完成这个临界点，有一个新线程调用getInstance()，那么第一个if，会怎么样？  

答案是因为第一个if没在同步块里，而此时instance已经非空，指向具体内存地址了，所以直接返回此时未完成初始化的instance实例  

那么如果在Singleton里有个变量 int number ,有个方法int getNumber()返回number，这时候调用  

Singleton.getInstance().getNumber();  

可能会报错，或者会得到错误结果，  

volatile修饰变量避免指令重排序，保证1-2-3按顺序来，这样即使在首个拿锁者未释放锁前，有线程切入，当它在第一个if处得到instance非空时，此时instance的初始化也一定已经完成。  

因此这就是volatile在DCL的作用了。  

#### 解决可见性

可见性的问题主要是指 一个线程修改了共享变量值，而在另一个线程看不到。

原因：
每个线程都拥有自己的一个高速缓冲区`Cache`（计算机组成原理），第一个线程更改了数据后，会写入 高速缓冲区，再而写入磁盘。如果该数据是在告诉缓冲区还没有写入磁盘之前，第二个线程进行读取的时候，读取到的依然是旧数据。为了解决这个问题，加入Volatile关键词后，第一个线程执行更改了数据之后，会马上写入磁盘，并刷新高速缓冲区。



@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_26_VolatileVisible.java)

结果

```java
sleep 3000 
// 一直在运行while(true)里面的空内容,因为线程 A 由于可见性原因看不到 main 已经修改 stop 为 true
// 没有停止
```



加上volatile 后的结果:

```java
sleep 3000 
//结束了
```



**这里需要待研究一下:**

**这里有例外是:**

while 的空内容换成 各换成如下三行内容,运行结果各有所不同

@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_27_VolatileVisible.java)

单独加入1 或者单独加入2 的运行结果是

打印完  `sleep 3000` 后打印一小段日志出来或不打印就结束了

单独加入2 的运行结果是:

打印完 `sleep 3000` 就一直运行  `ArrayList<Integer> b = new ArrayList<>();` 并且不会结束.

### Final详解

### 基础使用-修饰类

当某个类的整体定义为 final 时，就表明了该类是最终类，不能被继承。

注意：final 类的每个方法都隐式为 final  ，所以给每个方法添加是final 是 无意义的。

### 基础使用-修饰方法

类中所有的private 方法都隐式地指定为final 

final 方法是可以重载，但不可以重写

### 基础使用-修饰参数

Java 允许在参数列表中以声明地方式将参数指明为 final ,这意味无法更改参数引用所指向地对象。

主要是用来向匿名内部类传递数据。

### 修饰变量

被 static 和 final 同时修饰的时候，必须进行定义并赋值。（并不一定要赋明确的值）
@[code](./src/Burny-JUC/src/main/java/com/bruny/juc/basic01/A_30_StaticFinal.java)





