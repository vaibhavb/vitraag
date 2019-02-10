---
author: vitraag
comments: true
date: 2009-10-19 10:21:00+00:00
layout: post
link: https://vitraagblog.wordpress.com/2009/10/19/healthvault-apps-on-windows-azure/
slug: healthvault-apps-on-windows-azure
title: Running HealthVault Apps On Windows Azure
wordpress_id: 184
categories:
- ASP.NET
- HealthVault
---

[HealthVault SDK 1.0](http://blogs.msdn.com/healthvault/archive/2009/08/27/healthvault-0908-release-notes.aspx) introduces an interesting capability by which an HealthVault application can read their application certificate from a file. Eric has some details about this on his [blog](http://blogs.msdn.com/ericgu/archive/2009/10/16/healthvault-0908-sdk-highlights.aspx).

 

I’m going to describe how this capability of reading an application’s certificates from the file store could be used to run HealthVault application on Windows Azure. Here are the steps to get a simple HealthVault application (which I call HelloHV) running on Windows Azure:

 

  
  1. Install the [Azure SDK](http://www.microsoft.com/windowsazure/windowsazure/) and [HealthVault SDK](http://msdn.microsoft.com/HealthVault). Create your HealthVault application as a Web Role. 
   
  2. Configure and create an HealthVault application using the application manager utility in HealthVault SDK. **Make sure** you set the **Action-Url** to http://<yourapp>.cloudapp.net/Redirect.aspx using the Application Configuration Center. 
   
  3. Copy the Redirect.aspx & Redirect.cs from HealthVault samples (HelloWorld in HealthVault SDK) in to your application and add reference to HealthVault assemblies (you can find them in C:Program FilesMicrosoft HealthVaultSDKDotNetAssemblies) 
   
  4. Add the HealthVault related config settings to your WebRole’s Web.Config, the easiest way to do this would be copy the relevant key(s) from a sample in HealthVault SDK. Here is an illustration :      
    
    <font size="2"><span style="color:blue;"><</span><span style="color:#a31515;">appSettings</span></font><font size="2"><span style="color:blue;">>
      <</span><span style="color:#a31515;">add </span><span style="color:red;">key</span><span style="color:blue;">=</span>"<span style="color:blue;">ApplicationId</span>" <span style="color:red;">value</span><span style="color:blue;">=</span>"<span style="color:blue;">01e21bd1-cb13-40d6-8f01-596286827d6d</span>"</font><font size="2"><span style="color:blue;">/>
      <</span><span style="color:#a31515;">add </span><span style="color:red;">key</span><span style="color:blue;">=</span>"<span style="color:blue;">ShellUrl</span>" <span style="color:red;">value</span><span style="color:blue;">=</span>"<span style="color:blue;">https://account.healthvault-ppe.com/</span>"</font><font size="2"><span style="color:blue;">/>
      <</span><span style="color:#a31515;">add </span><span style="color:red;">key</span><span style="color:blue;">=</span>"<span style="color:blue;">HealthServiceUrl</span>" <span style="color:red;">value</span><span style="color:blue;">=</span>"<span style="color:blue;">https://platform.healthvault-ppe.com/platform/</span>"</font><span style="color:blue;"><font size="2">/>
      <!-- </font></span><span style="color:green;"><font size="2">when we call the SignOut() method on HealthServicePage, 
           it redirects us to the page below </font></span><font size="2"><span style="color:blue;">-->
      <!--</span><span style="color:green;"><add key="NonProductionActionUrlRedirectOverride" value="Redirect.aspx" /></span></font><span style="color:blue;"><font size="2">-->
      <!-- </font></span><span style="color:green;"><font size="2">The redirect page (specified above) uses these keys below to redirect to different
           pages based on the response from the shell </font></span><font size="2"><span style="color:blue;">-->
      <</span><span style="color:#a31515;">add </span><span style="color:red;">key</span><span style="color:blue;">=</span>"<span style="color:blue;">WCPage_ActionHome</span>" <span style="color:red;">value</span><span style="color:blue;">=</span>"<span style="color:blue;">default.aspx</span>"</font><font size="2"><span style="color:blue;">/>
      <</span><span style="color:#a31515;">add </span><span style="color:red;">key</span><span style="color:blue;">=</span>"<span style="color:blue;">WCPage_ActionAppAuthSuccess</span>" <span style="color:red;">value</span><span style="color:blue;">=</span>"<span style="color:blue;">HelloHV.aspx</span>"</font><font size="2"><span style="color:blue;">/>
      <</span><span style="color:#a31515;">add </span><span style="color:red;">key</span><span style="color:blue;">=</span>"<span style="color:blue;">ApplicationCertificateFileName</span>" 
           <span style="color:red;">value</span><span style="color:blue;">=</span>"<span style="color:blue;">~certWildcatApp-01e21bd1-cb13-40d6-8f01-596286827d6d.pfx</span>"</font><font size="2"><span style="color:blue;">/>
    </</span><span style="color:#a31515;">appSettings</span><span style="color:blue;">></span></font>



    

[](http://11011.net/software/vspaste)


  


  
  5. While testing on your local machine uncomment the following line in the Web.Config, this will allow HealthVault to communicate with your local machine. However make sure that this is commented when you publish the application. Alternatively the following key can also be stored in UserApplicationConfigs.xml, if you maintain one for your development. 
    
    
    <font size="2"><span style="color:blue;"><!--</span><span style="color:green;"><add key="NonProductionActionUrlRedirectOverride" value="Redirect.aspx" /></span></font><span style="color:blue;"><font size="1"><font size="2">—-></font></font></span>



    

**Gotacha1:** Windows Azure changes the port numbers for your application so its hard to make it work without using the action-url configured for your application in Application Configuration Center.


  


  
  6. In your Default HealthVault Page Make sure you read the certificate for your application from a local file (you can also use Azure Storage). 
    

**Gotacha2: **HealthVault SDK expects the **ApplicationCertificateFileName** to be absolute filename, this is impossible to determine for a cloud system like Azure. However we can get the absolute path by changing the value of the key at run-time.



    
    
    <p><font size="2"><span style="color:blue;">public partial class </span><span style="color:#2b91af;">HelloHV </span>: </font><font size="2"><span style="color:#2b91af;">HealthServicePage
    </span>{
        <span style="color:blue;">protected void </span>Page_PreInit(<span style="color:blue;">object </span>sender, <span style="color:#2b91af;">EventArgs </span>e)
        {
            <span style="color:#2b91af;">ConfigurationSettings</span>.AppSettings[<span style="color:#a31515;">"ApplicationCertificateFileName"</span>] =
                MapPath(<span style="color:#a31515;">@"~certWildcatApp-01e21bd1-cb13-40d6-8f01-596286827d6d.pfx"</span>);
        }
    
        <span style="color:blue;">protected void </span>Page_Load(<span style="color:blue;">object </span>sender, <span style="color:#2b91af;">EventArgs </span>e)
        {</font></p><p><font size="2">..</font></p>


  


  
  7. Hit Run and see your Hello HealthVault application in action!! 





**_Now the show time:_**





Check out a simple (HelloHV application) running on Windows Azure [here](http://hvsamples.cloudapp.net/HelloHV.aspx).





[![image](http://healthblog.vitraag.com/wp-content/uploads/2009/10/image_thumb1.png)](http://healthblog.vitraag.com/wp-content/uploads/2009/10/image4.png)





The associated code for this application is shared [here](http://code.msdn.microsoft.com/healthvaultazure).





Remember to switch to SSL and secure your application certificate (using password or Azure Storage) before you consider taking an application running on Windows Azure live as a production HealthVault application.
