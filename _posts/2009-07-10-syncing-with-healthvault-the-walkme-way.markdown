---
author: vitraag
comments: true
date: 2009-07-10 22:48:00+00:00
layout: post
link: https://vitraagblog.wordpress.com/2009/07/10/syncing-with-healthvault-the-walkme-way/
slug: syncing-with-healthvault-the-walkme-way
title: Syncing with HealthVault – the WalkMe way
wordpress_id: 397
categories:
- HealthVault
- WalkMe
---

A few months back [I promised](http://healthblog.vitraag.com/2009/02/walkme-walk-with-your-friends/) that I will do subsequent posts detailing implementation of [WalkMe](http://apps.healthvault.com/walkme). In this post I’ll attempt to described the way WalkMe synchronizes with HealthVault. As you might have noticed WalkMe keeps track of your most recent steps when you login to the application and without you having to log-in to the application via the [pedometer widget](http://healthblog.vitraag.com/2009/07/sharing-your-walkme-pedometer-using-e-mail-signature/), how does this magic happen?

 

**_The Syncing Philosophy         
_**Microsoft provides a [sync framework](http://en.wikipedia.org/wiki/Microsoft_Sync_Framework) which solves the problem of syncing between various data sources elegantly. However the framework is largely designed for data which is sourced using multiple masters, in WalkMe’s case we simplify this and consider HealthVault to be the master data source. Given that **HealthVault is our master data source** we radically simplify the complexity of syncing and don’t need to employ the services of sync framework.

 

To make HealthVault as the master data source any data input from WalkMe is always entered in HealthVault first and then the WalkMe database syncs with HealthVault

 

**_The Data Model         
_**In WalkMe’s case it maintains a local database of all its users and their data with regards to [aerobic exercise session](http://developer.healthvault.com/types/type.aspx?id=90dbf000-fc55-4b92-b4a1-da45c36ad8bb) and [exercise](http://developer.healthvault.com/types/type.aspx?id=85a21ddb-db20-4c65-8d30-33c899ccf612). I’ll keep the discussion about where to look for which data in HealthVault data types context for some other day. So why does WalkMe need a local database? We need a local database to maintain running totals of a users total steps, weekly steps and yearly steps. Also various analytical, notificational and graphical tools are only able to run in context of local data.

 

For each HealthVault user WalkMe keeps the following in the database:

 

  
  * HealthVault Person Id – This is unique to each person.
   
  * HealthVault Record Id – This is unique to each record Id, since WalkMe is a single record application (doesn’t work on multiple records associated with a person at a time), the record id has one to one mapping with the WalkMe user id
   
  * Last Sync Time with HealthVault – The time at which this user last synched with HealthVault. We will discuss the tuning aspects of sync time later in the mechanics section.
   
  * Last Sync Entity – Who performed the last sync. We will discuss various sync mechanism WalkMe we employs in the mechanics section.
   
  * Last Sync Status – Details about the sync status. This is helpful to reform the sync or flag whether the sync is in progress.
 

For each activity (aerobic exercise session and exercise) entry for each user, WalkMe keeps the following in the database:

 

  
  * HealthVault Item Id – This is the GUID of the item (any HealthVault thing). The contents of this HealthVault item are stored in this particular activity row. The content in our case are – steps, aerobic steps, calories, distance.
   
  * Updated_at – This is the time at which this item was last updated.
 

For each sync job / activity we maintain a database table having:

 

  
  * sync server name
   
  * sync status
   
  * sync timestamp
   
  * sync frequency (in hours)
   
  * sync job id
   
  * sync msg
 

[![WalkMe-DataModel]({{site.images}}/2009/07/walkmedatamodel-thumb.jpg)]({{site.images}}/2009/07/walkmedatamodel.jpg)

 

**Fig1. Relevant Parts Of WalkMe Data Model**

 

**_The Mechanics         
_**The key aspects to understand in any sync problem is when is it that your user will need the most up to date information and how are they going to access it. Other than the time when a user is directly logged in the application, WalkMe’s needs the most up to date information when showing the WalkMe pedometers (which exist outside the context of WalkMe and HealthVault and they are accessed via a public webpage). Other key piece is for the WalkMe groups to show the most up to date information with regards to the leaders in the group they need each users data to be synched at least in last 24 hours.

 

So I can summarize that we have the following three scenarios needing the most up to date HealthVault data:

 

  
  1. When the user in logged in the application – data needed to show his analytics, and standings in age-group, BMI, Zip etx.
   
  2. When the user pedometer is accessed from a public page – data needed to show the most recent steps.
   
  3. When the user accesses their group page – the current standings of participants should be up to date at least as of last 24 hours.
 

_**When and How to Sync         
**_Clearly for scenarios 1 and 2 above we need to sync for a single user while for scenario #3 (and a part of #2) we need to sync the entire list of application users. Also note that for scenario 1 the user is present and for scenario 2 the user is not online. Lets name them #1 is **UserOnlineSync** #2 is **UserOfflineSync** and #3 is **ApplicationSync. **

 

**UserOnlineSync** : We should sync it every 20 minutes (based on a cookie) and sync the account when the user signs in.

 

**UserOfflineSync:** This sync should be done as requested but in the context of this sync user is not online (This is done using HealthVault offline calls). However the frequency is deteremined by output caching enabled on the widgets (I would put that to 20 minutes as well).

 

**ApplicationSync: **This is done for all the user and typically by a background process the last table in the data model is primarily meant for this process. However we don't want to ping HealthVault for all the records so we use the method [GetUpdateRecordsForApplication](https://platform.healthvault-ppe.com/platform/XSD/method-getupdatedrecordsforapplication.xsd). The background process can run once or twice a day the frequency of the same can be made configurable.

 

Please note application sync is not fully functional in WalkMe yet owing to resource constraints on background processes in our hosting environment.

 

**_What to do when things go wrong?         
_**As you will note in the above three sync mechanisms are primarily tailored to be partial syncs i.e they dont fetch all the user activities all the time. So what happens if a user deletes an entry in HealthVault or lets say the sync never completed? Well the user will see discrepancy is his/ her record and in that case we provide a mechanism for them to do a full sync with HealthVault. The idea of full sync being that all the current items are deleted and all the items form the users HealthVault record are imported again, and of course all the totals are re-calculated. In addition to taking care of uncompleted syncs this process also account for deleted items (there is not other way for delete items to be communicated). This is a powerful “reset” button and is exposed to the user with caution.

 

**_The Implementation_**

 

**_ **_![caution]({{site.images}}/2009/07/caution-thumb.jpg)_**          
_**Here is some code showing the implementation of above three sync mechanisms with full and partial syncs. Please take it with grain of salt its here for illustrative purposes only and is no way meant to be used as is.

 

 

  
  *     

**UserOnlineSync**

  
 

  

    
    
    <span style="color:#606060;" id="lnum1">   1:</span> <span style="color:#0000ff;">public</span> <span style="color:#0000ff;">static</span> <span style="color:#0000ff;">void</span> OnlineSyncUser(ProfileModel profile, PersonInfo info, <span style="color:#0000ff;">bool</span> partialSync)




    
    
    <span style="color:#606060;" id="lnum2">   2:</span>  {




    
    
    <span style="color:#606060;" id="lnum3">   3:</span>      <span style="color:#0000ff;">string</span> syncType = <span style="color:#006080;">"partial"</span>;




    
    
    <span style="color:#606060;" id="lnum4">   4:</span>      DateTime? lastSyncTime = profile.UserCtx.hv_last_sync_time;




    
    
    <span style="color:#606060;" id="lnum5">   5:</span>      DateTime timeStamp = DateTime.Now;




    
    
    <span style="color:#606060;" id="lnum6">   6:</span>  




    
    
    <span style="color:#606060;" id="lnum7">   7:</span>      <span style="color:#008000;">// reset lastsynctime if this is a full sync</span>




    
    
    <span style="color:#606060;" id="lnum8">   8:</span>      <span style="color:#0000ff;">if</span> (!lastSyncTime.HasValue || !partialSync)




    
    
    <span style="color:#606060;" id="lnum9">   9:</span>      {




    
    
    <span style="color:#606060;" id="lnum10">  10:</span>          WlkMiTracer.Instance.Log(<span style="color:#006080;">"HVSync.cs:OnlineSyncUser"</span>, WlkMiEvent.UserSync,




    
    
    <span style="color:#606060;" id="lnum11">  11:</span>                WlkMiCat.Info, <span style="color:#0000ff;">string</span>.Format(<span style="color:#006080;">"Full syncing for User: {0}"</span>,




    
    
    <span style="color:#606060;" id="lnum12">  12:</span>                  profile.UserCtx.user_id));




    
    
    <span style="color:#606060;" id="lnum13">  13:</span>          lastSyncTime = <span style="color:#0000ff;">null</span>;




    
    
    <span style="color:#606060;" id="lnum14">  14:</span>      }




    
    
    <span style="color:#606060;" id="lnum15">  15:</span>  




    
    
    <span style="color:#606060;" id="lnum16">  16:</span>      <span style="color:#008000;">// Retrieve the latest info from HealthVault</span>




    
    
    <span style="color:#606060;" id="lnum17">  17:</span>      HealthRecordItemCollection items = 




    
    
    <span style="color:#606060;" id="lnum18">  18:</span>          GetHVItemsOnline(info, lastSyncTime);




    
    
    <span style="color:#606060;" id="lnum19">  19:</span>      <span style="color:#0000ff;">if</span> (items != <span style="color:#0000ff;">null</span> && items.Count > 0)




    
    
    <span style="color:#606060;" id="lnum20">  20:</span>      {




    
    
    <span style="color:#606060;" id="lnum21">  21:</span>          <span style="color:#0000ff;">foreach</span> (HealthRecordItem item <span style="color:#0000ff;">in</span> items)




    
    
    <span style="color:#606060;" id="lnum22">  22:</span>          {




    
    
    <span style="color:#606060;" id="lnum23">  23:</span>              <span style="color:#008000;">// Do the distinct per item work</span>




    
    
    <span style="color:#606060;" id="lnum24">  24:</span>              ProcessStepsHealthItem(item, profile);




    
    
    <span style="color:#606060;" id="lnum25">  25:</span>          }




    
    
    <span style="color:#606060;" id="lnum26">  26:</span>      }




    
    
    <span style="color:#606060;" id="lnum27">  27:</span>  




    
    
    <span style="color:#606060;" id="lnum28">  28:</span>      <span style="color:#008000;">//only update the last sync time if we are able to download items</span>




    
    
    <span style="color:#606060;" id="lnum29">  29:</span>      <span style="color:#0000ff;">if</span> (items != <span style="color:#0000ff;">null</span>)




    
    
    <span style="color:#606060;" id="lnum30">  30:</span>      {




    
    
    <span style="color:#606060;" id="lnum31">  31:</span>          <span style="color:#008000;">//set last sync time</span>




    
    
    <span style="color:#606060;" id="lnum32">  32:</span>          profile.UserCtx.hv_last_sync_time = timeStamp;




    
    
    <span style="color:#606060;" id="lnum33">  33:</span>          profile.Save();




    
    
    <span style="color:#606060;" id="lnum34">  34:</span>      }




    
    
    <span style="color:#606060;" id="lnum35">  35:</span>  




    
    
    <span style="color:#606060;" id="lnum36">  36:</span>      <span style="color:#008000;">// Clear the WlkMi data cache if the last sync is null or this is a full sync</span>




    
    
    <span style="color:#606060;" id="lnum37">  37:</span>      <span style="color:#0000ff;">if</span> (!lastSyncTime.HasValue || !partialSync)




    
    
    <span style="color:#606060;" id="lnum38">  38:</span>      {




    
    
    <span style="color:#606060;" id="lnum39">  39:</span>          WlkMiTracer.Instance.Log(<span style="color:#006080;">"HVSync.cs:OnlineSyncUser"</span>, WlkMiEvent.UserSync,




    
    
    <span style="color:#606060;" id="lnum40">  40:</span>                WlkMiCat.Info, <span style="color:#0000ff;">string</span>.Format(<span style="color:#006080;">"Full sync deleting information for User: {0}"</span>,




    
    
    <span style="color:#606060;" id="lnum41">  41:</span>                  profile.UserCtx.user_id));




    
    
    <span style="color:#606060;" id="lnum42">  42:</span>          lastSyncTime = <span style="color:#0000ff;">null</span>;




    
    
    <span style="color:#606060;" id="lnum43">  43:</span>          WalkLogModel.ClearUserCache(profile);




    
    
    <span style="color:#606060;" id="lnum44">  44:</span>          syncType = <span style="color:#006080;">"full"</span>;




    
    
    <span style="color:#606060;" id="lnum45">  45:</span>      }




    
    
    <span style="color:#606060;" id="lnum46">  46:</span>  




    
    
    <span style="color:#606060;" id="lnum47">  47:</span>      <span style="color:#008000;">//Processtotals for this user</span>




    
    
    <span style="color:#606060;" id="lnum48">  48:</span>      WalkLogModel.ProcessTotals(profile.UserCtx.user_id);




    
    
    <span style="color:#606060;" id="lnum49">  49:</span>      




    
    
    <span style="color:#606060;" id="lnum50">  50:</span>      WlkMiTracer.Instance.Log(<span style="color:#006080;">"HVSync:OnlineSyncUser"</span>, WlkMiEvent.UserSync,




    
    
    <span style="color:#606060;" id="lnum51">  51:</span>          WlkMiCat.Info, <span style="color:#0000ff;">string</span>.Format(<span style="color:#006080;">"Completed Online {1} Sync of User: {0}"</span>,




    
    
    <span style="color:#606060;" id="lnum52">  52:</span>          profile.UserCtx.user_id.ToString(), syncType));  




    
    
    <span style="color:#606060;" id="lnum53">  53:</span>  }




    
    
    <span style="color:#606060;" id="lnum54">  54:</span>  




    
    
    <span style="color:#606060;" id="lnum55">  55:</span> <span style="color:#0000ff;">public</span> <span style="color:#0000ff;">static</span> HealthRecordItemCollection GetHVItemsOnline(PersonInfo info, DateTime? lastSync)




    
    
    <span style="color:#606060;" id="lnum56">  56:</span> {




    
    
    <span style="color:#606060;" id="lnum57">  57:</span>     HealthRecordSearcher searcher = info.SelectedRecord.CreateSearcher();




    
    
    <span style="color:#606060;" id="lnum58">  58:</span>  




    
    
    <span style="color:#606060;" id="lnum59">  59:</span>     HealthRecordFilter filter = <span style="color:#0000ff;">new</span> HealthRecordFilter(Exercise.TypeId,




    
    
    <span style="color:#606060;" id="lnum60">  60:</span>         AerobicSession.TypeId);




    
    
    <span style="color:#606060;" id="lnum61">  61:</span>  




    
    
    <span style="color:#606060;" id="lnum62">  62:</span>     <span style="color:#0000ff;">if</span>(lastSync.HasValue)




    
    
    <span style="color:#606060;" id="lnum63">  63:</span>         filter.UpdatedDateMin = (DateTime) lastSync;




    
    
    <span style="color:#606060;" id="lnum64">  64:</span>  




    
    
    <span style="color:#606060;" id="lnum65">  65:</span>  




    
    
    <span style="color:#606060;" id="lnum66">  66:</span>     <span style="color:#008000;">// TODO: Add filter so that we get only items with steps</span>




    
    
    <span style="color:#606060;" id="lnum67">  67:</span>     searcher.Filters.Add(filter);




    
    
    <span style="color:#606060;" id="lnum68">  68:</span>     HealthRecordItemCollection items = searcher.GetMatchingItems()[0];




    
    
    <span style="color:#606060;" id="lnum69">  69:</span>  




    
    
    <span style="color:#606060;" id="lnum70">  70:</span>     <span style="color:#0000ff;">return</span> items;




    
    
    <span style="color:#606060;" id="lnum71">  71:</span> }












  
  * _**UserOfflineSync**_






  


    
    
    <span style="color:#606060;" id="lnum1">   1:</span> <span style="color:#0000ff;">public</span> <span style="color:#0000ff;">static</span> <span style="color:#0000ff;">void</span> OfflineSyncUser(ProfileModel profile)




    
    
    <span style="color:#606060;" id="lnum2">   2:</span> {




    
    
    <span style="color:#606060;" id="lnum3">   3:</span>     DateTime timeStamp = DateTime.Now;




    
    
    <span style="color:#606060;" id="lnum4">   4:</span>  




    
    
    <span style="color:#606060;" id="lnum5">   5:</span>     <span style="color:#008000;">// Retrieve the latest info from HealthVault</span>




    
    
    <span style="color:#606060;" id="lnum6">   6:</span>     <span style="color:#0000ff;">if</span> (profile.UserCtx.hv_personid != <span style="color:#0000ff;">null</span>)




    
    
    <span style="color:#606060;" id="lnum7">   7:</span>     {




    
    
    <span style="color:#606060;" id="lnum8">   8:</span>         HealthRecordItemCollection items = GetHVItemsOffline(profile.UserCtx.hv_personid, 




    
    
    <span style="color:#606060;" id="lnum9">   9:</span>             profile.UserCtx.hv_recordid,profile.UserCtx.hv_last_sync_time);




    
    
    <span style="color:#606060;" id="lnum10">  10:</span>         <span style="color:#0000ff;">if</span> (items != <span style="color:#0000ff;">null</span> && items.Count > 0)




    
    
    <span style="color:#606060;" id="lnum11">  11:</span>         {




    
    
    <span style="color:#606060;" id="lnum12">  12:</span>             <span style="color:#0000ff;">foreach</span> (HealthRecordItem item <span style="color:#0000ff;">in</span> items)




    
    
    <span style="color:#606060;" id="lnum13">  13:</span>             {




    
    
    <span style="color:#606060;" id="lnum14">  14:</span>                 <span style="color:#008000;">// Do the distinct per item work</span>




    
    
    <span style="color:#606060;" id="lnum15">  15:</span>                 ProcessStepsHealthItem(item, profile);




    
    
    <span style="color:#606060;" id="lnum16">  16:</span>             }




    
    
    <span style="color:#606060;" id="lnum17">  17:</span>             WlkMiTracer.Instance.Log(<span style="color:#006080;">"HVSync.cs:OfflineSyncUser"</span>, WlkMiEvent.AppSync,




    
    
    <span style="color:#606060;" id="lnum18">  18:</span>                 WlkMiCat.Info, <span style="color:#0000ff;">string</span>.Format(<span style="color:#006080;">"Number of items retrieved from HV: {0}"</span>,




    
    
    <span style="color:#606060;" id="lnum19">  19:</span>                 items.Count));




    
    
    <span style="color:#606060;" id="lnum20">  20:</span>         }




    
    
    <span style="color:#606060;" id="lnum21">  21:</span>         <span style="color:#008000;">//only update the last sync time if we are able to download items</span>




    
    
    <span style="color:#606060;" id="lnum22">  22:</span>         <span style="color:#0000ff;">if</span> (items != <span style="color:#0000ff;">null</span>)




    
    
    <span style="color:#606060;" id="lnum23">  23:</span>         {




    
    
    <span style="color:#606060;" id="lnum24">  24:</span>             <span style="color:#008000;">//set last sync time</span>




    
    
    <span style="color:#606060;" id="lnum25">  25:</span>             profile.UserCtx.hv_last_sync_time = timeStamp;




    
    
    <span style="color:#606060;" id="lnum26">  26:</span>             profile.Save();




    
    
    <span style="color:#606060;" id="lnum27">  27:</span>         }




    
    
    <span style="color:#606060;" id="lnum28">  28:</span>     }




    
    
    <span style="color:#606060;" id="lnum29">  29:</span>  




    
    
    <span style="color:#606060;" id="lnum30">  30:</span>     <span style="color:#008000;">// Clear the WlkMi data cache if the last sync is null</span>




    
    
    <span style="color:#606060;" id="lnum31">  31:</span>     <span style="color:#008000;">// In other words, you can also set the time stamp for user's last sync to null</span>




    
    
    <span style="color:#606060;" id="lnum32">  32:</span>     <span style="color:#008000;">// to trigger a full offline sync.</span>




    
    
    <span style="color:#606060;" id="lnum33">  33:</span>     <span style="color:#008000;">// TODO: Consider not doing this for production</span>




    
    
    <span style="color:#606060;" id="lnum34">  34:</span>     <span style="color:#0000ff;">if</span> (!profile.UserCtx.hv_last_sync_time.HasValue)




    
    
    <span style="color:#606060;" id="lnum35">  35:</span>     {




    
    
    <span style="color:#606060;" id="lnum36">  36:</span>         WlkMiTracer.Instance.Log(<span style="color:#006080;">"HVSync.cs:OfflineSyncUser"</span>, WlkMiEvent.AppSync,




    
    
    <span style="color:#606060;" id="lnum37">  37:</span>             WlkMiCat.Info, <span style="color:#0000ff;">string</span>.Format(<span style="color:#006080;">"Deleting information for user {0}"</span>,




    
    
    <span style="color:#606060;" id="lnum38">  38:</span>             profile.UserCtx.user_id));




    
    
    <span style="color:#606060;" id="lnum39">  39:</span>  




    
    
    <span style="color:#606060;" id="lnum40">  40:</span>         WalkLogModel.ClearUserCache(profile);




    
    
    <span style="color:#606060;" id="lnum41">  41:</span>     }




    
    
    <span style="color:#606060;" id="lnum42">  42:</span>  




    
    
    <span style="color:#606060;" id="lnum43">  43:</span>     <span style="color:#008000;">// Processtotals for this user</span>




    
    
    <span style="color:#606060;" id="lnum44">  44:</span>     WalkLogModel.ProcessTotals(profile.UserCtx.user_id);




    
    
    <span style="color:#606060;" id="lnum45">  45:</span>  




    
    
    <span style="color:#606060;" id="lnum46">  46:</span>     WlkMiTracer.Instance.Log(<span style="color:#006080;">"HVSync.cs:OfflineSyncUser"</span>, WlkMiEvent.AppSync,




    
    
    <span style="color:#606060;" id="lnum47">  47:</span>         WlkMiCat.Info, <span style="color:#0000ff;">string</span>.Format(<span style="color:#006080;">"Completed Offline Sync of User: {0}"</span>,




    
    
    <span style="color:#606060;" id="lnum48">  48:</span>         profile.UserCtx.user_id.ToString()));




    
    
    <span style="color:#606060;" id="lnum49">  49:</span> }




    
    
    <span style="color:#606060;" id="lnum50">  50:</span>  




    
    
    <span style="color:#606060;" id="lnum51">  51:</span> <span style="color:#0000ff;">public</span> <span style="color:#0000ff;">static</span> HealthRecordItemCollection GetHVItemsOffline(Guid personId, 




    
    
    <span style="color:#606060;" id="lnum52">  52:</span>     Guid recordGuid, DateTime? lastSync)




    
    
    <span style="color:#606060;" id="lnum53">  53:</span> {




    
    
    <span style="color:#606060;" id="lnum54">  54:</span>     <span style="color:#008000;">// Do the offline connection</span>




    
    
    <span style="color:#606060;" id="lnum55">  55:</span>     OfflineWebApplicationConnection offlineConn =




    
    
    <span style="color:#606060;" id="lnum56">  56:</span>         <span style="color:#0000ff;">new</span> OfflineWebApplicationConnection(personId);




    
    
    <span style="color:#606060;" id="lnum57">  57:</span>     offlineConn.RequestTimeoutSeconds = 180;  <span style="color:#008000;">//extending time to prevent time outs for accounts with large number of items</span>




    
    
    <span style="color:#606060;" id="lnum58">  58:</span>     offlineConn.Authenticate();




    
    
    <span style="color:#606060;" id="lnum59">  59:</span>     HealthRecordAccessor accessor =




    
    
    <span style="color:#606060;" id="lnum60">  60:</span>         <span style="color:#0000ff;">new</span> HealthRecordAccessor(offlineConn, recordGuid);




    
    
    <span style="color:#606060;" id="lnum61">  61:</span>     HealthRecordSearcher searcher = accessor.CreateSearcher();




    
    
    <span style="color:#606060;" id="lnum62">  62:</span>  




    
    
    <span style="color:#606060;" id="lnum63">  63:</span>     HealthRecordFilter filter = <span style="color:#0000ff;">new</span> HealthRecordFilter(Exercise.TypeId,




    
    
    <span style="color:#606060;" id="lnum64">  64:</span>         AerobicSession.TypeId);




    
    
    <span style="color:#606060;" id="lnum65">  65:</span>  




    
    
    <span style="color:#606060;" id="lnum66">  66:</span>     <span style="color:#0000ff;">if</span> (lastSync.HasValue)




    
    
    <span style="color:#606060;" id="lnum67">  67:</span>         filter.UpdatedDateMin = (DateTime)lastSync;




    
    
    <span style="color:#606060;" id="lnum68">  68:</span>  




    
    
    <span style="color:#606060;" id="lnum69">  69:</span>     searcher.Filters.Add(filter);




    
    
    <span style="color:#606060;" id="lnum70">  70:</span>  




    
    
    <span style="color:#606060;" id="lnum71">  71:</span>     HealthRecordItemCollection items = <span style="color:#0000ff;">null</span>;




    
    
    <span style="color:#606060;" id="lnum72">  72:</span>     <span style="color:#0000ff;">try</span>




    
    
    <span style="color:#606060;" id="lnum73">  73:</span>     {




    
    
    <span style="color:#606060;" id="lnum74">  74:</span>         items = searcher.GetMatchingItems()[0];




    
    
    <span style="color:#606060;" id="lnum75">  75:</span>     }




    
    
    <span style="color:#606060;" id="lnum76">  76:</span>     <span style="color:#0000ff;">catch</span> (Exception err)




    
    
    <span style="color:#606060;" id="lnum77">  77:</span>     {




    
    
    <span style="color:#606060;" id="lnum78">  78:</span>         WlkMiTracer.Instance.Log(<span style="color:#006080;">"HVSync.cs:GetHVItemsOffline"</span>, WlkMiEvent.AppSync, WlkMiCat.Error,




    
    
    <span style="color:#606060;" id="lnum79">  79:</span>                 <span style="color:#0000ff;">string</span>.Format(<span style="color:#006080;">"Error for user {0} : {1} "</span>, 




    
    
    <span style="color:#606060;" id="lnum80">  80:</span>                 recordGuid.ToString(),err.ToString()));




    
    
    <span style="color:#606060;" id="lnum81">  81:</span>     }




    
    
    <span style="color:#606060;" id="lnum82">  82:</span>     <span style="color:#0000ff;">return</span> items;




    
    
    <span style="color:#606060;" id="lnum83">  83:</span> }












  
  * _**ApplicationSync**_






  


    
    
    <span style="color:#606060;" id="lnum1">   1:</span> <span style="color:#0000ff;">public</span> <span style="color:#0000ff;">static</span> <span style="color:#0000ff;">void</span> SyncWlkMiWithHealthVault(




    
    
    <span style="color:#606060;" id="lnum2">   2:</span>     DateTime? lastUpdatedDate)




    
    
    <span style="color:#606060;" id="lnum3">   3:</span> {




    
    
    <span style="color:#606060;" id="lnum4">   4:</span>     WlkMiTracer.Instance.Log(<span style="color:#006080;">"HVSync.cs"</span>, WlkMiEvent.AppSync, WlkMiCat.Info, 




    
    
    <span style="color:#606060;" id="lnum5">   5:</span>         <span style="color:#006080;">"Getting updated records from HealthVault"</span>);




    
    
    <span style="color:#606060;" id="lnum6">   6:</span>     <span style="color:#008000;">// Do the offline connection</span>




    
    
    <span style="color:#606060;" id="lnum7">   7:</span>     OfflineWebApplicationConnection offlineConn =




    
    
    <span style="color:#606060;" id="lnum8">   8:</span>         <span style="color:#0000ff;">new</span> OfflineWebApplicationConnection();




    
    
    <span style="color:#606060;" id="lnum9">   9:</span>     offlineConn.Authenticate();




    
    
    <span style="color:#606060;" id="lnum10">  10:</span>     IList<Guid> updatedUserIds = 




    
    
    <span style="color:#606060;" id="lnum11">  11:</span>         offlineConn.GetUpdatedRecordsForApplication(lastUpdatedDate);




    
    
    <span style="color:#606060;" id="lnum12">  12:</span>     WlkMiTracer.Instance.Log(<span style="color:#006080;">"HVSync.cs"</span>, WlkMiEvent.AppSync, WlkMiCat.Info,




    
    
    <span style="color:#606060;" id="lnum13">  13:</span>         <span style="color:#0000ff;">string</span>.Format(<span style="color:#006080;">"Got {0} updated records from HealthVault"</span>, updatedUserIds.Count));




    
    
    <span style="color:#606060;" id="lnum14">  14:</span>  




    
    
    <span style="color:#606060;" id="lnum15">  15:</span>     <span style="color:#0000ff;">foreach</span>(Guid recordid <span style="color:#0000ff;">in</span> updatedUserIds)




    
    
    <span style="color:#606060;" id="lnum16">  16:</span>     {




    
    
    <span style="color:#606060;" id="lnum17">  17:</span>         ProfileModel syncUser = ProfileModel.Fetch(recordid);




    
    
    <span style="color:#606060;" id="lnum18">  18:</span>         <span style="color:#0000ff;">if</span> (syncUser == <span style="color:#0000ff;">null</span>)




    
    
    <span style="color:#606060;" id="lnum19">  19:</span>         {




    
    
    <span style="color:#606060;" id="lnum20">  20:</span>             WlkMiTracer.Instance.Log(<span style="color:#006080;">"HVSync.cs"</span>, WlkMiEvent.AppSync, WlkMiCat.Error,




    
    
    <span style="color:#606060;" id="lnum21">  21:</span>                 <span style="color:#0000ff;">string</span>.Format(<span style="color:#006080;">"No WlkMi user found for recordif {0} "</span>, recordid));




    
    
    <span style="color:#606060;" id="lnum22">  22:</span>             <span style="color:#0000ff;">continue</span>;




    
    
    <span style="color:#606060;" id="lnum23">  23:</span>         }




    
    
    <span style="color:#606060;" id="lnum24">  24:</span>         <span style="color:#008000;">// Decide to update this guy?</span>




    
    
    <span style="color:#606060;" id="lnum25">  25:</span>         <span style="color:#0000ff;">if</span> (syncUser.UserCtx.hv_last_sync_time > DateTime.Now.AddSeconds(




    
    
    <span style="color:#606060;" id="lnum26">  26:</span>             -Constants.UserSyncIntervalInSeconds))




    
    
    <span style="color:#606060;" id="lnum27">  27:</span>         {




    
    
    <span style="color:#606060;" id="lnum28">  28:</span>             WlkMiTracer.Instance.Log(<span style="color:#006080;">"HVSync.cs"</span>, WlkMiEvent.AppSync, WlkMiCat.Info,




    
    
    <span style="color:#606060;" id="lnum29">  29:</span>                 <span style="color:#0000ff;">string</span>.Format(<span style="color:#006080;">"Skipping sync for user {0} "</span>, syncUser.UserCtx.user_id));




    
    
    <span style="color:#606060;" id="lnum30">  30:</span>         }




    
    
    <span style="color:#606060;" id="lnum31">  31:</span>         <span style="color:#0000ff;">else</span>




    
    
    <span style="color:#606060;" id="lnum32">  32:</span>         {




    
    
    <span style="color:#606060;" id="lnum33">  33:</span>             HVSync.OfflineSyncUser(syncUser);




    
    
    <span style="color:#606060;" id="lnum34">  34:</span>         }




    
    
    <span style="color:#606060;" id="lnum35">  35:</span>     }




    
    
    <span style="color:#606060;" id="lnum36">  36:</span> }











**_Suggestions?
        
_**There are various ways in which the HealthVault platform can assist application in syncing with the data native to HealthVault. One thing comes to my mind is support for [feedsync](http://en.wikipedia.org/wiki/FeedSync). You may have a lot of suggestions, please feel free to chime in the comments!!
