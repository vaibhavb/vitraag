---
author: vitraag
comments: true
date: 2008-06-27 04:05:29+00:00
layout: post
link: https://vitraagblog.wordpress.com/2008/06/26/scheming-for-method-schemas/
slug: scheming-for-method-schemas
title: Scheming for Method Schemas
wordpress_id: 36
categories:
- HealthVault
---

Eric did a great [post ](http://blogs.msdn.com/ericgu/archive/2008/03/11/scheming-for-schema.aspx)about how to retrieve the thing-type schemas programmatically. This code shows how to retrieve the methods reponse an request programmatically.

The gist is in the method call GetServiceDefinition, this call returns the list of method and only can work on the methods to retrieve the urls for the schema's for that version's request and response.


    
    
        protected void Page_Load(object sender, EventArgs e)
        {
            ApplicationConnection connection = base.DictionaryConnection;
            ServiceInfo serviceInfo = connection.GetServiceDefinition();
            List methodVersions =
                new List(
                    serviceInfo.Methods.Count);
            foreach (HealthServiceMethodInfo method in serviceInfo.Methods)
            {
                SaveMethodXSD(method);
            }
        }
    
        void SaveMethodXSD(HealthServiceMethodInfo methods)
        {
            string directoryName = MapPath("platform");
            Directory.CreateDirectory(directoryName).CreateSubdirectory("web").CreateSubdirectory("methods");
    
            foreach (HealthServiceMethodVersionInfo method in methods.Versions)
            {
                if (!String.IsNullOrEmpty(method.RequestFileName))
                {
                    SaveFile(method.RequestSchemaUrl.ToString(), method.RequestFileName);
                }
                if (!String.IsNullOrEmpty(method.ResponseFileName))
                {
                    SaveFile(method.ResponseSchemaUrl.ToString(), method.ResponseFileName);
                }
            }
        }
    
        void SaveFile(string schemaUri, string name)
        {
            string filename = MapPath(@"platformwebmethods" + name + ".xsd");
            using (StreamWriter writer = System.IO.File.CreateText(filename))
            {
                HttpWebRequest httpRequest = (HttpWebRequest)WebRequest.Create(schemaUri);
                using (HttpWebResponse httpResponse = (HttpWebResponse)httpRequest.GetResponse())
                {
                    using (StreamReader httpResponseStream = new StreamReader(httpResponse.GetResponseStream()))
                    {
                        writer.Write(httpResponseStream.ReadToEnd());
                    }
                }
            }
        }
    



Note: the above snipped tries to save the schemas to a directory named platformwebmethods.
PLEASE NOTE: By blogging software is capitalizing the code in a weird way. I dont know what's up with dpSyntaxHighligher.
