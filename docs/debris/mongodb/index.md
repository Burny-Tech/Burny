---
lang: zh-CN
title: MongoDB
description: 碎片笔记-MongoDB
---

# MongoDB
```sh



/mongodb/apps/mongodb/bin
./mongo

//不存在则创建
use gdin-standard

show users   //查看所有用户
//创建用户
db.createUser({
    user:"gdin-standard",  
    pwd:"gdin-standard@2020",  
    roles:[
        {role:"readWrite",db:"gdin-standard"}
    ],
    "mechanisms" : [   //认证机制
		"SCRAM-SHA-1"
	]
})
 
 
db.dropUser('lisi')   //删除用户

数据库用户角色：read、readWrite；
数据库管理角色：dbAdmin、dbOwner、userAdmin;
集群管理角色：clusterAdmin、clusterManager、4. clusterMonitor、hostManage；
备份恢复角色：backup、restore；
所有数据库角色：readAnyDatabase、readWriteAnyDatabase、userAdminAnyDatabase、dbAdminAnyDatabase
超级用户角色：root
内部角色：__system

```



```sh
# 文档
https://www.mongodb.com/docs/v6.0/reference/connection-string/
        Query query = new Query();
        Query query2 = new Query(Criteria.where("字段").gt(8000));

        Query query1=new BasicQuery("原生的条件");

        Update update =new Update();
        update.set("字段名","value");

        MongoTemplate mongoTemplate=new MongoTemplate();
        mongoTemplate.updateFirst(new Query(),update, Host.class)


```

