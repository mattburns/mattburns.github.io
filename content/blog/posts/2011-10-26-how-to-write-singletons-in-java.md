---
title: How to write Singletons in java
author: matt
type: post
date: 2011-10-26T11:30:37+00:00
url: /blog/2011/10/26/how-to-write-singletons-in-java/
categories:
  - Uncategorized

---
Singletons get a pretty bad press. Often described as an “anti-pattern”. I think it’s a little unfair since I find them pretty useful in several situations. However, the reason they can be bad is important to understand:

> _Making a class a singleton can make it difficult to test its clients, as it’s impossible to substitute a mock implementation for a singleton unless it implements an interface that serves as its type._

That quote, and most of what I am about to write are completely stolen from Josh Bloch’s excellent book, Effective Java (highly recommended in [paperback][1] or [kindle][2] editions). Those are affiliate links, but I still recommend you buy it no matter where you get it from.

Anyway, it raises an important point about testability, but one that I think doesn’t matter. The way I see it, if you’re writing a singleton that represents something you want to swap with a mock, such as a database connection or network resource etc then your design will change as your tests evolve. You practice [TDD][3] right? You’ll soon realise that a singleton doesn’t make sense or you need an interface of some kind. This post is about how to write a good singleton.

In the bad old days before java 1.5 there were 2 common ways to implement a singleton. A public final field:

```
public static final Elvis INSTANCE = new Elvis();
```

or a static factory:

```
private static final Elvis INSTANCE = new Elvis();
public static Elvis getInstance() {
    return INSTANCE;
}
```

The static factory version is slightly better in that the you have a bit more flexibility to change your implementation details at a later date. In my two examples there is no performance benefit of either technique in modern JVMs. This is all well and good. There is only one Elvis in the world. There is the possibility a privileged client can invoke the private constructor reflectively but I’m not going to dwell on that.

Bloch raises another problem:

> _To make a singleton class that is implemented using either of the previous approaches serializable, it is not sufficient merely to add implements Serializable to its declaration. To maintain the singleton guarantee, you have to declare all instance fields transient and provide a readResolve method. Otherwise, each time a serialized instance is deserialized, a new instance will be created, leading, in the case of our example, to spurious Elvis sightings._

Oo-er, this sounds messy. You implied in java 1.5 there’s a better way, please, what is it, I’m desperate!

```
// Enum singleton - the preferred approach
public enum Elvis {
    INSTANCE;
    public void leaveTheBuilding() { ... }
}
```

TADA!

> _This approach is functionally equivalent to the public field approach, except that it is more concise, provides the serialization machinery for free, and provides an ironclad guarantee against multiple instantiation, even in the face of sophisticated serialization or reflection attacks. While this approach has yet to be widely adopted, a single-element enum type is the best way to implement a singleton._

Have a little think about it, let it sink in, then run off and replace any singletons in any projects you can get your hands on.

 [1]: http://amzn.to/sxX8l4
 [2]: http://amzn.to/vVgXVU
 [3]: http://en.wikipedia.org/wiki/Test-driven_development