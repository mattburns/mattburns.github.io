---
title: Using Java 7 on OSX
author: matt
type: post
date: 2014-05-16T10:43:59+00:00
url: /blog/2014/05/16/using-java-7-on-osx/
categories:
  - Uncategorized

---
Does your current version point to JDK6 even though you’ve installed JDK7?

```
matt$ ls -l /System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK
8 lrwxr-xr-x  1 root  wheel  59 21 Nov 14:43 /System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK -> /System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents
```

The do this:

```
sudo rm /System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK
sudo ln -s /Library/Java/JavaVirtualMachines/jdk1.7.0_51.jdk/Contents/ /System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK
```

If it’s not already, set JAVA\_HOME accordingly in your ~/.bash\_profile:

```
export JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK/Home
```

Test it worked:

```
matt$ java -version
java version "1.7.0_51"
Java(TM) SE Runtime Environment (build 1.7.0_51-b13)
Java HotSpot(TM) 64-Bit Server VM (build 24.51-b03, mixed mode)
```