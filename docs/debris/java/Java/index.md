---
lang: zh-CN
title: Java
description: 碎片笔记-Java
---



## JDK8特性



::: details  Optional 

```java
 public void checkOutId(StockCus stockCus) {
        Optional.ofNullable(stockCus.getCusId()).ifPresent((b) -> {
            Optional<StockCus> byId = stockCusRepository.findById(b);
            Optional.ofNullable(byId).orElseThrow(() -> new BaseException("记录不存在"));
        });
        Optional.ofNullable(stockCus.getCusId()).ifPresent((b)->{
            Customer customer = customerService.get(b);
            Optional.ofNullable(customer).orElseThrow(()->new BaseException("记录不存在"));
        });

    }
```

:::


::: details   `List &lt;  List  &lt;   Object&gt;&gt;` 转`List  &lt; Object &gt;`

```java
            List<List<StockCus>> collect2 = stocks.stream().map(b -> b.getStockCusList()).collect(Collectors.toList());
            List<StockCus> collect3 = collect2.stream().flatMap(Collection::stream).collect(Collectors.toList());
```

:::

:::   details  归类

```java
        Map<Long, List<Stock>> collect1 = all1.stream().collect(Collectors.groupingBy(b -> b.getBrandId()));
//相同报错
Map<Long, User> maps = userList.stream().collect(Collectors.toMap(User::getId,Function.identity()));
//相同不报错
        Map<Long, User> maps = userList.stream().collect(Collectors.toMap(User::getId, Function.identity(), (key1, key2) -> key2));

   
Map<Long, String> maps = userList.stream().collect(Collectors.toMap(User::getId, User::getAge, (key1, key2) -> key2));


```

:::

:::  details  统计

```java
            Integer down = collect3.stream().filter(b -> b.getDownNum() != null).map(StockCus::getDownNum).reduce(Integer::sum).orElse(null);

```

:::



Linux环境变量



```java
 fdsafdsa 
```



## The last packet sent successfully to the server was 0 milliseconds ago. The

```yml
     更改如下：
     url: jdbc:mysql://192.168.1.62/data_standard?useSSL=false&autoReconnect=true&characterEncoding=UTF-8&nullCatalogMeansCurrent=true&autoReconnect=true&failOverReadOnly=false&maxReconnects=100

```

