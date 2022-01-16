---
title: Passing your credentials in order to deploy to Google App Engine with Ant
author: matt
type: post
date: 2012-07-11T12:53:26+00:00
url: /blog/2012/07/11/passing-your-credentials-in-order-to-deploy-to-google-app-engine-with-ant/
categories:
  - Uncategorized

---
If you use the [example ant script][1] provided by Google you’ll face the following error:

```
Your authentication credentials can't be found and may have expired.
Please run appcfg directly from the command line to re-establish your credentials.
```

Sure, you can run appcfg.sh from the console, and login and all will be fine next time. Well, for 24 hours before your credentials are booted from the cache.

Here’s my ant target that does the same thing but takes the credentials interactively using the [input task][2].

```
&lt;target name="deploy-app" description="Uploads and deploys the application to App Engine."&gt;
    &lt;input message="Enter email" addproperty="gae-email"/&gt;
    &lt;input message="Enter password :- " addproperty="gae-password"&gt;
        &lt;handler type="secure"/&gt;
    &lt;/input&gt;

    &lt;!-- Call dependencies here rather than with 'depends' attribute to get input first --&gt;
    &lt;antcall target="test" /&gt;

    &lt;java classname="com.google.appengine.tools.admin.AppCfg" inputstring="${gae-password}"
            classpath="${sdk.dir}/lib/appengine-tools-api.jar" fork="true" failonerror="true"&gt;
        &lt;arg value="--email=${gae-email}" /&gt;
        &lt;arg value="--passin" /&gt;
        &lt;arg value="update" /&gt;
        &lt;arg value="war" /&gt;
    &lt;/java&gt;
&lt;/target&gt;
```

Obviously, if you want to run this target from your [CI][3] server then you’ll need to populate the email and password properties in some other way.

&nbsp;

 [1]: https://developers.google.com/appengine/docs/java/tools/ant#The_Complete_Build_File
 [2]: http://ant.apache.org/manual/Tasks/input.html
 [3]: http://en.wikipedia.org/wiki/Continuous_integration