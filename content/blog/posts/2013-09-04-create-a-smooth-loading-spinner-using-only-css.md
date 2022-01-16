---
title: Create a smooth loading spinner using only CSS
author: matt
type: post
date: 2013-09-04T17:25:56+00:00
url: /blog/2013/09/04/create-a-smooth-loading-spinner-using-only-css/
categories:
  - Uncategorized

---
We’ve all seen loading spinners and they generally look like this:

![](/wp-content/uploads/2013/09/ajax-loader.gif)

Urgh.

This is just an animated gif and has the following drawbacks:

  * Limited to 256 colours
  * Need to [regenerate the image][2] if you want a different colour.
  * Framerate and resolution set when you create the image. (and increasing either will hurt load times).
  * Playback is jerky until all frames are downloaded

Wouldn’t it be better to use some [vector magic][3] and hardware-accelerated loveliness to get a spinner like this:

<div class="spinner">
</div>

Mmmmm, hot-diggity, how delicious is that?!

## Let’s do it!

For all the examples, there is no javascript and the only html markup is this:

```
<div class="spinner">
  
</div>
```

### Rounding a square

To create the loader I had to be a bit creative. Firstly, the circle is simply the border of a div with corners so round it become a circle:

<div class="spinner1">
</div>

<div class="spinner1 rounded">
</div>

```
.spinner {
  width: 50px;
  height: 50px;
  border: solid 3px #DB73D7;

  -webkit-border-radius: 50%;
     -moz-border-radius: 50%;
          border-radius: 50%;
}
```

### Arc

But we don’t want a circle, we want an arc, so one way is to set the border-width to 0px except for one edge:

<div class="spinner2">
</div>

<div class="spinner2 rounded">
</div>

```
.spinner {
  width: 50px;
  height: 50px;
  border: solid #DB73D7;
  border-width: 3px 0px 0px 0px;

  -webkit-border-radius: 50%;
     -moz-border-radius: 50%;
          border-radius: 50%;
}
```

### Animate

Now all that’s left is to animate it:

<div class="spinner2 rounded spinning">
</div>

```
.spinner {
  width: 50px;
  height: 50px;
  border: solid #DB73D7;
  border-width: 3px 0px 0px 0px;

  -webkit-border-radius: 50%;
     -moz-border-radius: 50%;
          border-radius: 50%;

  -webkit-animation: spin 0.5s infinite linear;
     -moz-animation: spin 0.5s infinite linear;
       -o-animation: spin 0.5s infinite linear;
          animation: spin 0.5s infinite linear;
}

@-webkit-keyframes spin {
  from {-webkit-transform: rotate(0deg);}
  to   {-webkit-transform: rotate(359deg);}
}

@-moz-keyframes spin {
  from {-moz-transform: rotate(0deg);}
  to   {-moz-transform: rotate(359deg);}
}

@-o-keyframes spin {
  from {-o-transform: rotate(0deg);}
  to   {-o-transform: rotate(359deg);}
}

@keyframes spin{
  from {transform: rotate(0deg);}
  to   {transform: rotate(359deg);}
}
```

### Square capped

Alternatively, you can set the border-color to transparent except for one edge. This gives the arc a more traditional square capped edge:

<div class="spinner3 rounded spinning">
</div>

```
.spinner {
  ...
  border: solid 3px rgba(0,0,0,0);
  border-top-color: #DB73D7;
  ...
}
```

You can play with the code in this [JS Bin][4]. You can easily change the speed, size, colour. Why not try replacing the simple “linear” animation with something a bit more interesting like: 

```
cubic-bezier(0.1, 0.2, 0.4, 0.1)
```

If you make something interesting, please post links to your creations in the comments below 🙂

 [1]: http://www.mattburns.co.uk/blog/wp-content/uploads/2013/09/ajax-loader.gif
 [2]: http://www.ajaxload.info/
 [3]: http://www.mattburns.co.uk/blog/2013/02/24/4-reasons-to-design-your-logo-in-css-and-a-few-why-you-shouldnt/ "4 reasons to design your logo in CSS (and a few why you shouldn’t)"
 [4]: http://jsbin.com/usIjEgI/1/