---
author: vitraag
comments: true
date: 2008-07-07 15:17:43+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/07/07/creating-a-healthvault-child-application/
slug: creating-a-healthvault-child-application
title: Creating a HealthVault Child Application
wordpress_id: 37
categories:
- HealthVault
---

If your application is a master application, you can programmatically create child application in the HealthVault environment. This implies that you have the ability to provision the child application. This is particularly desirable in the patientconnect scenario.

So here are the steps to do this, highlighting the gotchas:



	
  1. Create an OfflineWebApplicationConnection, you don't need a PersonId for this it can be Guid.Empty

	
  2. Make a template ApplicationInfo object

	
  3. Read the public key you want to associate with this application and use the GetRawCertData method to add it to the ApplicationInfo object

	
  4. Read the image you want to associate with this child application and add it to ApplicationInfo

	
  5. Since a child application is an offline application it doesn't really need a action url, so instead of this you are suppose to provide the contents for PrivacyStatement and TermsOfUse of this application (with content type text) by setting the appropriate ApplicationInfo properties

	
  6. Add the rules for datatypes this child application will use. The best way to do this is individually add a rule for each type accessed.

	
  7. Viola, fire it up to the HealthVault environment - using the AddApplication method!



**Update:** Below is a prototype sample, you will need to add paths to appropriate files.


    
    
    /// <summary>
    /// Summary description for CreateChildApplication
    /// </summary>
    public class CreateChildApplication
    {
        public static void CreateApplication()
        {
            // Create an offline connection, we use an empty Guid as personId
            // There is a bug to create a constructor without requiring a guid
            // Use this only if you master application wants to do this in Offline mode
            OfflineWebApplicationConnection offlineConnection =
                new OfflineWebApplicationConnection(Guid.Empty);
            offlineConnection.Authenticate();
    
            // Setting up the application we want to create
            ApplicationInfo appInfo =
                new ApplicationInfo();
            appInfo.Name = "Cool child application";
            appInfo.AuthorizationReason =
                "Cool child application needs authorization to improve your health";
            appInfo.Description =
                "Cool child application can help you change our lifestyle";
            // get a base64 encoded logo
            appInfo.LargeLogo = new ApplicationBinaryConfiguration(
                pathTojpgOrGifOrPng, "image/gif");
            // base64 encoded public key for this application
            appInfo.PublicKeys.Add(
                GetPublicKeyFromPfxOrP12(fullPathToPfxOrP12OrCerFile));
    
            // You need to have PrivacyStatement + TermsOfUse or ActionUrl
            appInfo.PrivacyStatement = new ApplicationBinaryConfiguration(
            pathToPrivacyStatementTextFile, "text/plain");
            appInfo.TermsOfUse = new ApplicationBinaryConfiguration
                (pathToTermsOfUseTextFile, "text/plain");
            //actionUrl
            //appInfo.ActionUrl = new Uri("http://localhost/redirect.aspx");
    
            // Create and add the rules individually
            List rules = new List();
            rules.Add((AuthorizationSetDefinition)(new TypeIdSetDefinition(Height.TypeId)));
            AuthorizationRule rule1 = new AuthorizationRule(
                HealthRecordItemPermissions.Read,
                rules,
                null);
            // Here we are setting up the child as an offline application
            appInfo.OfflineBaseAuthorizations.Add(rule1);
            
            // Add more rules, if needed
    
            // Lets make the child app!
            Provisioner.AddApplication(offlineConnection, appInfo);
        }
    
        private static byte[] GetPublicKeyFromPfxOrP12(string fullPathToCerFile)
        {
            X509Certificate cert = new X509Certificate(fullPathToCerFile);
            return cert.GetRawCertData();
        }
    }
    
