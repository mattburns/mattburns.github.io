---
title: Bug with JQuery validation error messages showing tooltip text
author: matt
type: post
date: 2011-10-28T13:50:45+00:00
url: /blog/2011/10/28/bug-with-jquery-validation-error-messages-showing-tooltip-text/
categories:
  - Uncategorized

---
I had the following html in my form:

```
<label for="email-input">Email</label>
&lt;input id="email-input"
       type="text"
       title="Don't worry, your email will not be displayed on the website or given to anyone else. We hate spam too." />
```

Nothing complicated there I hope.  
I had the help text set in the title attribute of the input which I styled with the lovely [qTip][1] to make it look nice. I validated my entry using the jQuery [validation plugin][2] which also works well. The problem is that if an attempt is made to submit the form before any attempt at editing the value or showing the tooltip, the error message would show the value of the tooltip (“Don’t worry…“) instead of the validation error message (“This field is required“).

It’s taken me a while to find the cause, but the fix is easy. When invoking the validator, throw in the option to [ignore title attributes][3].

```
$("#your-form").validate({
ignoreTitle: true
})
```

 [1]: http://craigsworks.com/projects/qtip/
 [2]: http://bassistance.de/jquery-plugins/jquery-plugin-validation/
 [3]: http://rocketsquared.com/wiki/Plugins/Validation/validate#options