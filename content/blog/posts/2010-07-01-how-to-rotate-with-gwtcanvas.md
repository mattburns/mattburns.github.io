---
title: 'Solved: How to rotate with GWTCanvas'
author: matt
type: post
date: 2010-07-01T14:31:39+00:00
url: /blog/2010/07/01/how-to-rotate-with-gwtcanvas/
categories:
  - Uncategorized

---
Having trouble rotating something you’ve drawn with [GWTCanvas][1]?

It took me a little while to work out, but GWTCanvas works slightly differently to Graphic2D in Java. It’s important to realise that with GWTCanvas, when you invoke “rotate(r)” you’re actually transforming the coordinate space that will be used for subsequent drawing.

    canvas.moveTo(50, 50);
    canvas.lineTo(50, 10);
    canvas.stroke();

Produces:  
![](/wp-content/uploads/2010/07/arrow_01.png)

In order to rotate it, you must invoke rotate **_before_** you start any drawing.  

    canvas.translate(50, 50);
    canvas.rotate(Math.toRadians(45));
    canvas.translate(-50, -50);
    canvas.moveTo(50, 50);
    canvas.lineTo(50, 10);
    canvas.stroke();


Tadaa!  
![](/wp-content/uploads/2010/07/arrow_451.png)

The same is also true for other transformation methods such as “scale” and “translate”.

 [1]: http://code.google.com/p/google-web-toolkit-incubator/wiki/GWTCanvas