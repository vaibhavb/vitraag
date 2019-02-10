---
author: vitraag
comments: true
date: 2017-07-21 23:49:30+00:00
layout: post
link: https://vitraagblog.wordpress.com/2017/07/21/our-secure-future-can-be-built-on-blockchains-introducing-pensieve/
slug: our-secure-future-can-be-built-on-blockchains-introducing-pensieve
title: Our Secure Future Can Be Built on Blockchains — Introducing Pensieve!
wordpress_id: 1556
categories:
- ramblings
tags:
- Blockchain
- Cybersecurity
- Ethereum
- Team Pensieve
---





![](https://cdn-images-1.medium.com/max/800/0*ZkhfrIIVqzYYJszd.)

Securing Data with BlockChain (Source: [http://www.ethosvo.org](http://www.ethosvo.org/blockchain-for-dummies/))

**Editor’s Note:** This article describes the project “**Pensieve: Decentralized Ethereum Application for Privacy & Data Security” **being developed by Nick Handy, Brandon Rawlin, and Eric Tinoco for [Lib13 Inc](http://www.lib13.com), as part of the Cyber Defenders 2017 Program.




### Background




For the past couple of weeks of summer, we’ve been exploring blockchain systems as a group of college interns in the Cyber Defenders program. Our project is a tool called Pensieve, a decentralized Ethereum application that can secure confidential data.




### The Problem — Big Corporations Store User Data




Users have to depend on big corporations like Google & Facebook to store their personal data like passwords and interests associated with their identity. Overtime this huge data store becomes onerous and a prime target for security breaches. Pensieve will protect user data by using the blockchain to identify users and store sensitive data.




### Enter Ethereum




We are starting with a relative new but well proven system — Ethereum. The Ethereum blockchain network can provide a way of decentralizing data on a peer to peer network. We will use Ethereum to interact with a google chrome extension that can store user submitted data so that they are the only ones that can access the data.




### Why BlockChain for Security?




Blockchain — This may be a familiar term to some, and you may have heard it referred to as Bitcoin, Ethereum, or the countless other cryptocurrency systems popping up over the past couple years. But what is the blockchain and how can we use it for security?




The blockchain, in its simplest form, is just a transaction ledger that everyone on the system has a copy of. Every time a transaction is made it gets added to a block that is th stored on the block chain. The history of every transaction ever made is stored in this chain and is available for every person on the network to see. A block once added to the blockchain cannot be changed which makes it impossible to undo any transaction.




### Smart Contracts!




Ethereum is the blockchain system we have chosen to work with because it provides more functionality over a traditional cryptocurrency like Bitcoin. Ethereum uses the idea of smart contracts to allow the building of decentralized applications within the network.




A smart contract allows a computer program to be stored on the blockchain and be accessed through a transaction. Smart contracts are computer programs that can be submitted as a transaction to the blockchain. Every peer on the network has the contract and is able to see how it functions. Like with other blockchains, these contracts cannot be changed once submitted to the network. Smart contracts run automatically based on the conditions set up initially by the developer. Each interaction within Ethereum involves communication of the contracts.




![](https://cdn-images-1.medium.com/max/800/0*uDxO9YWh4pMksXVS.)

Smart Contracts on a BlockChain

By having smart contracts, Ethereum allows decentralized apps in their system. A decentralized application is not run by any particular person and gives the users more control over how they interact with an application. A centralized application, such as a social network, holds all of the user’s data. They hold the power to do with it what they like. On the other hand, a decentralized application can only use user information in predefined ways that are public to the network.




### Our Solution to Decentralize Private Data




Normally user data is stored in a central location such as datacenter. The user has access of the data, but so does the company holding that data. This creates a problem where the company, as the keeper of the data, could use that data however they see fit. This causes vulnerabilities to the data if the company becomes hacked. We will use Ethereum to interact with a google chrome extension that can store user submitted data so that they are the only ones that can access the data.




Our project will use these ideas to develop a browser extension that interacts with the Ethereum blockchain to secure sensitive data. An extension is a built in tool for browsers for google chrome, firefox etc. that can provide special interactions with web applications. This extension will be our connection from user to blockchain.




By having the data stored with the blockchain we are decentralizing the information. No single company or person will have access to the data stored on the network. Instead, data on the blockchain can only be accessed from the user’s address that originally stored the data.




To access this data through the browser we must communicate between the blockchain and the extension. Ethereum has its own native programming language called Solidity. Solidity is a contract-oriented language that is designed to allow developers to create decentralized applications (DApps). With the use of the chrome extension and Solidity, we will be able to program a way to save the consumer’s sensitive data, such as, passwords, .txt files, and much more.




### Give us ideas ?




In the future, we aim to allow users to store more than just username and password information. We are still brainstorming ideas for other data to store on the blockchain and would love your suggestions — dear reader. Some preliminary ideas include storing someone’s will and testament, medical information, or other sensitive data on the blockchain.




Moving forward we also aim to provide a service that would do more than simply secure user information. We also want to devise a system to inform users of potential security breaches. For example, if some major retailer was hacked and millions’ of customers information was leaked, we would notify our user of the breach and provide steps to ensure that their personal information remains secure.




With the help of the Ethereum blockchain and the creation of a decentralized app that will communicate with the blockchain to store sensitive data, we will be able to create a new form of protection and messaging for sensitive data.




### Peer Review Our Approach..




What do you think of our approach? Any pointers to simplify your implementation of a Chrome plugin (javascript based) to store sensitive information from browser to an Ethereum DApp (solidity based). We plan to have an active github repository at [https://github.com/cyberdefenders/Pensieve](https://github.com/cyberdefenders/Pensieve).



