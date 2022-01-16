---
title: How to dynamically choose the color of your Google maps marker pin using javascript
author: matt
type: post
date: 2011-10-07T12:30:41+00:00
url: /blog/2011/10/07/how-to-dynamically-choose-the-color-of-you-google-maps-marker-pin-using-javascript/
categories:
  - Uncategorized

---
You can dynamically request icon images from the [Google charts api][1] with the urls:

> http://chart.apis.google.com/chart?chst=d\_map\_pin_letter&chld=%E2%80%A2|FE7569

Which looks like this:![default][2] the image is 21×43 pixels and the pin tip is at position (10, 34)

And you’ll also want a separate shadow image (so that it doesn’t overlap nearby icons):

> http://chart.apis.google.com/chart?chst=d\_map\_pin_shadow

Which looks like this:![shadow][3] the image is 40×37 pixels and the pin tip is at position (12, 35)

When you construct your MarkerImages you need to set the size and achor points accordingly:

> var pinColor = “FE7569”;  
> var pinImage = new google.maps.MarkerImage(“http://chart.apis.google.com/chart?chst=d\_map\_pin_letter&chld=%E2%80%A2|” + pinColor,  
> new google.maps.Size(21, 34),  
> new google.maps.Point(0,0),  
> new google.maps.Point(10, 34));  
>  
> var pinShadow = new google.maps.MarkerImage(“http://chart.apis.google.com/chart?chst=d\_map\_pin_shadow”,  
> new google.maps.Size(40, 37),  
> new google.maps.Point(0, 0),  
> new google.maps.Point(12, 35));

You can then add the marker to your map with:

> var marker = new google.maps.Marker({  
> position: new google.maps.LatLng(0,0),  
> map: map,  
> icon: pinImage,  
> shadow: pinShadow  
> });

Simply replace “FE7569” with the color code you’re after. Eg:![yellow][4]

 [1]: http://code.google.com/apis/chart/infographics/docs/dynamic_icons.html#pins
 [2]: http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|FE7569
 [3]: http://chart.apis.google.com/chart?chst=d_map_pin_shadow
 [4]: http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|FFFF57