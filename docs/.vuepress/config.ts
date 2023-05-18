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
        link: "/debris/git/index.md",
      },
      {
        text: "系统笔记",
        link: "/system/OpenCV/index.md",
      },
    ],

    sidebar: {
      "/debris/": [
        {
          text: "Git",
          children: ["/debris/git/index.md"],
        },
        {
          text: "sh",
          children: [
            "/debris/sh/docker/index.md",
            "/debris/sh/gogs2gitlab/index.md",
            "/debris/sh/ssl/index.md",
            "/debris/sh/yum/index.md",
            "/debris/sh/dashbord/index.md",
            "/debris/sh/sh/crontabs.md",
            "/debris/sh/sh/httpd-tools.md",
            "/debris/sh/sh/jps.md",
            "/debris/sh/sh/selfStart.md",
            "/debris/sh/sh/xianzhi.md",
            "/debris/sh/index.md",
          ],
        },
        {
          text: "Java",
          children: ["/debris/java/Java/index.md"],
        },
        {
          text: "SpringBoot",
          children: ["/debris/java/SpringBoot/index.md"],
        },
        {
          text: "SpringJPA",
          children: ["/debris/java/JPA/index.md"],
        },
        {
          text: "MongoDB",
          children: ["/debris/mongodb/index.md"],
        },
        {
          text: "MySQL",
          children: ["/debris/mysql/index.md"],
        },
        {
          text: "Oracle",
          children: ["/debris/oracle/index.md"],
        },
        {
          text: "软考",
          children: ["/debris/ruankao/index.md"],
        },
        {
          text: "Node",
          children: ["/debris/web/index.md"],
        },
      ],

      "/system/": [
        {
          text: "Arthas",
          children: ["/system/Arthas/index.md"],
        },
        {
          text: "AI",
          children: ["/system/DeepLean/index.md", "/system/OpenCV/index.md"],
        },
        {
          text: "Docker",
          children: ["/system/docker/index.md"],
        },

        {
          text: "Gradle",
          children: ["/system/gradle/index.md"],
        },
        {
          text: "K8S",
          children: ["/system/kubernetes/index.md"],
        },
        {
          text: "Rabbitmq",
          children: ["/system/rabbitmq/index.md"],
        },
        {
          text: "Redis",
          children: ["/system/redis/index.md"],
        },
        {
          text: "SpringSecurity",
          children: ["/system/SpringSecurity/index.md"],
        },
        {
          text: "JUC",
          children: ["/system/JUC/index.md"],
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
