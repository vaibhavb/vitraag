---
author: vitraag
comments: true
date: 2011-06-24 22:50:43+00:00
layout: post
link: https://vitraagblog.wordpress.com/2011/06/24/associating-mood-tracker-with-healthvault-3/
slug: associating-mood-tracker-with-healthvault-3
title: 'Associating Mood Tracker With HealthVault #3'
wordpress_id: 332
categories:
- Mobile
- MoodTracker
---

Sorry for the delay in installment #3 in the series of how to write a WP7 app for HealthVault! The code for this application is now hosted on [github](https://github.com/vaibhavb/moodtracker).

 

In order for the Mood Tracker application to work with HealthVault we will get appropriate application creation credentials from the HealthVault Service and authorize them through the user with HealthVault Shell. 

 

1. To get the credential from HealthVault Service the application contacts the HealthVault service to get application creation Url.

 

The code for that is outlined in [MyMood.xaml.cs](https://github.com/vaibhavb/moodtracker/blob/master/MoodTracker/MyMood.xaml.cs)

 

  
    
     <span class="kwrd">void</span> MainPage_Loaded(<span class="kwrd">object</span> sender, RoutedEventArgs e)
            {
                App.HealthVaultService.LoadSettings(SettingsFilename);
                App.HealthVaultService.BeginAuthenticationCheck(AuthenticationCompleted, 
                    DoShellAuthentication);
                SetProgressBarVisibility(<span class="kwrd">true</span>);
            }
    
    <span class="kwrd">void</span> DoShellAuthentication(<span class="kwrd">object</span> sender, HealthVaultResponseEventArgs e)
            {
                SetProgressBarVisibility(<span class="kwrd">false</span>);
    
                App.HealthVaultService.SaveSettings(SettingsFilename);
    
                <span class="kwrd">string</span> url;
    
                <span class="kwrd">if</span> (_addingRecord)
                {
                    url = App.HealthVaultService.GetUserAuthorizationUrl();
                }
    ...








2. The application creation needs to be validated on behalf of the user.
    


    
The best mechanism to achieve this is by having a page with a hosted browser which redirect appropriately to HealthVault and closes the browsers and navigated back to page on a successful authorization.





Following is the code in [HostedBrowserPage.xaml](https://github.com/vaibhavb/moodtracker/blob/master/MoodTracker/HostedBrowser.xaml.cs) :




    
          <span class="kwrd">void</span> c_webBrowser_Navigated(<span class="kwrd">object</span> sender, System.Windows.Navigation.NavigationEventArgs e)
            {
                <span class="kwrd">if</span> (e.Uri.OriginalString.Contains(<span class="str">"target=AppAuthSuccess"</span>))
                {
                    Uri pageUri = <span class="kwrd">new</span> Uri(<span class="str">"/MyMood.xaml"</span>, UriKind.RelativeOrAbsolute);
    
                    Deployment.Current.Dispatcher.BeginInvoke(() =>
                    {
                        NavigationService.Navigate(pageUri);
                    });
                }
            }
    
            <span class="kwrd">void</span> HealthVaultWebPage_Loaded(<span class="kwrd">object</span> sender, RoutedEventArgs e)
            {
                <span class="kwrd">string</span> url = App.HealthVaultShellUrl;
    
                c_webBrowser.Navigate(<span class="kwrd">new</span> Uri(url));
            }





Note that on success the Application is being redirected to MyMood.xaml which is our landing page!





Here is flow of how the above authentication works!





[![image]({{site.images}}/2011/06/image_thumb.png)]({{site.images}}/2011/06/image.png)[![image]({{site.images}}/2011/06/image_thumb1.png)]({{site.images}}/2011/06/image1.png)[![image]({{site.images}}/2011/06/image_thumb2.png)]({{site.images}}/2011/06/image2.png)

    
Step1. Home page Step2.Sign-in & Auth Step3. Mood track in action!





**Next time:** Adding the emotional state data type to Mood Tracker

    
**Previous Post:** [Getting Started](http://healthblog.vitraag.com/2011/05/getting-started-with-mood-tracker-2/)






.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }
