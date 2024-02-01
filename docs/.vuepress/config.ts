import { defaultTheme } from "@vuepress/theme-default";

export default {
  lang: "zh-CN",
  title: "Burny.tech",
  description: "Burny笔记",
  debug: true,
  open: false,
  port: 80,
  // head: [["script ", { type: "text/javascript", src: "/js/client.js" }]],

  theme: defaultTheme({
    colorModeSwitch: true,
    home: "/",

    lastUpdated: false,
    contributors: false,

    navbar: [
      {
        text: "首页",
        link: "/",
      },
      {
        text: "碎片笔记",
        link: "/debris/git/",
      },
      {
        text: "系统笔记",
        link: "/system/OpenCV/",
      },
    ],

    sidebar: {
      "/debris/": [
        {
          text: "Git",
          children: ["/debris/git/"],
        },
        {
          text: "sh",
          children: [
            "/debris/sh/docker/",
            "/debris/sh/gogs2gitlab/",
            "/debris/sh/ssl/",
            "/debris/sh/yum/",
            "/debris/sh/dashbord/",
            "/debris/sh/sh/crontabs.md",
            "/debris/sh/sh/httpd-tools.md",
            "/debris/sh/sh/jps.md",
            "/debris/sh/sh/selfStart.md",
            "/debris/sh/sh/xianzhi.md",
            "/debris/sh/",
          ],
        },
        {
          text: "Java",
          children: ["/debris/java/Java/"],
        },
        {
          text: "SpringBoot",
          children: ["/debris/java/SpringBoot/"],
        },
        {
          text: "SpringJPA",
          children: ["/debris/java/JPA/"],
        },
        {
          text: "MongoDB",
          children: ["/debris/mongodb/"],
        },
        {
          text: "MySQL",
          children: ["/debris/mysql/"],
        },
        {
          text: "Oracle",
          children: ["/debris/oracle/"],
        },
        {
          text: "软考",
          children: ["/debris/ruankao/"],
        },
        {
          text: "Node",
          children: ["/debris/web/"],
        },
      ],

      "/system/": [
        {
          text: "Arthas",
          children: ["/system/Arthas/"],
        },
        {
          text: "AI",
          children: ["/system/DeepLean/", "/system/OpenCV/"],
        },
        {
          text: "Docker",
          children: ["/system/docker/"],
        },

        {
          text: "Gradle",
          children: ["/system/gradle/"],
        },
        {
          text: "K8S",
          children: ["/system/kubernetes/"],
        },
        {
          text: "Rabbitmq",
          children: ["/system/rabbitmq/"],
        },
        {
          text: "Redis",
          children: ["/system/redis/"],
        },
        {
          text: "SpringSecurity",
          children: ["/system/SpringSecurity/"],
        },
        {
          text: "JUC",
          children: ["/system/JUC/"],
        },
      ],
    },
  }),

  markdown: {
    level: [1, 2, 3, 4, 5, 6, 7, 8],
    toc: {
      level: [1, 2, 3, 4, 5, 6, 7, 8],
    },
  },
};
