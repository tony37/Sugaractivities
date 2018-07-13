#SugarActivities
This repository provides an alternate to SugarLab's  [ASLO](http://activities.sugarlabs.org). ASLO is an abbreviation which refers to the url of the website: http://activities.sugarlabs.org.

#Introduction

A major feature of Sugar is its rich collection of Sugar Activities. Currently there are over 500 different activities in the ASLO collection.

#Transition
The original model is that activities are created and contributed by individual volunteers who also submit new version fixing problems or adding additional capabilities.

However, the environment has changed. Many of the original contributors are no longer active in the community. Meanwhile, over time there have been many changes in the supporting software. For example, several activities used the Python module 'hulahop'. This has been replaced by a module 'WebKit'. However, this has now been replaced by a newer module 'WebKit2'. Fixing these kinds of problems is often easier for a single volunteer providing new versions of several activities. 

So a decsion was made to base activity development on github to take advantage of its support for collaboration by a team of contributors. 

#Beware of Detours

The situation is analoguous to road construction. The first thing the crew does is render the current road unusable. It puts up detour signs to enable the commuter to get past the site, The commuter knows that when the construction is complete it will be a big improvement - but in the meantime the trip takes longer and is more difficult.

#Local servers

Sugaractivities was developed as a means to support deployments with limited or no access to the internet. This requires that the Sugar Activities collection by stored on a local server so that users can select activites to try and have them downloaded and installed by the Browse activity. This capability has been available for years. 

Fortunately GitHub supports direct access to static web sites which in the end is what Sugaractivities is. Therefore it is possible to offer this capability as a 'detour' while a new ASLO is under construction.

#Usage

The simplest way to use Sugaractivities is to open Browse in Sugar and enter the url: 

	http://github.com/tony37/Sugaractivities/index.html.

This will open the main page with nine tiles:

1. README
	
>	Displays this README.

2. Fructose
	
	 
>	 Displays the Fructose collection of activities and is an example of a custom collection. 
	 
3. GTK3
	 
>	 This tile displays Sugar Web activities or those which have been ported to GTK+3 and work on both Sugar with Ubuntu 18.04 LTS and Sugar on the XO. 

4. GTK3x

>This tile displays activities which would be in the GTK3 collectsion except they do not execute correctly. Information on the problem is provided by the Note button for each activity.

5. GTK2

>This tile displays activities from ASLO which have not been ported to GTK3 and so only work on the XO or in environments compatible with build 13.2.9 with Sugar 0.112.

6. GTK2x

>This tile displays activities which would be in the GTK2 collection except that they do not execute correctly. Information on the problem is provided by the Note button for each activity.

7. Github

>This tile displays activities which have repositories on github: http://github.com/Sugarlabs. In general, they are the same as the corresponding activity in ASLO except that the bundle id was changed. These activities work in the XO environment.

8. Githubx

>This tile displays activities that would be in the GitHub collection except that they do not execute correctly. Information on the problem is provided by the Note button for the activity.
>
9. Admin

>This tile opens a page with some utilities to help support maintenance of the site. One option is to use the Make CSV from remote repository tile to download a python script. Use the Links tile to download the file 'aslo.js'. The command python makecsv.py will create a file 'aslo.csv'. This file can be opened with the Calc Spreadsheed to display detailed information on the complete set of activities.

The tiles 2-7 partition the complete collection of activities based on their current status. Clicking on a button - say GTK2 - opens a page with rows of tiles, one tile per activity in that collection. Unlike ASLO there is not search - the user scrolls down the page. Any tile can be clicked to download that activity.
The main tiles show the entire library partitioned into six sets. The first are the Sugar Web activities and activities ported to GTK+3 which should work in all Sugar environments. The second has activities which have been ported to GTK+3 but currently do not work. The note button provides some information on the problem. The next four form pairs with the first (gtk and github) showing the working activities (gtk work only with XO Sugar 0.112). The second in the pair shows ones which currently do not work.

Clicking on a main page tile opens that collection. Clicking on an activity tile downloads and installs the activity. Tiles may have a 'help' button and/or a 'notes' button. The first shows the 'help' page associated with the activity. The second shows the notes describing the current status of the activity. The tile itself may show a brief description of the activity.

#Usage on a local device

Go to http://github.com/tony37/Sugaractivites. This page provides the ability to download a clone of the repository. This is useful for contributors to the maintenance of this library.

For users of Sugar on Ubuntu 18.04, there usally ample storage space available. On this page, choose to download the zip. Save it, for example, in /home/username/ (i.e. your ~ directory). Unzip the file (e.g. ~/Sugaractivities). The you can use the capability in Sugar from the Browse activity by entering the url: file:///home/username/Sugaractivities/index.html). This works offline. 

#Schoolserver usage

If the file is unzipped on a computer configured as a server ('schoolserver'), it should be possible to arrange it to be used via Apache with a url like: http://schoolserver/Sugaractivities/index.html.

#How Sugaractivities works

There is an html file: index.html in the root of the Sugaractivities directory. This file includes aslo.js and jquery.js. The file aslo.js provides the information for the tiles.

##tiles

A tile is defined by a 'link':

["4418","display title", "image.svg", "activities/helloworld-7.xo","description", "help/helloworld.html","notes/helloworld.html"],

This forms a list with from five to seven members.

	1. The ASLO id number for the activity (http://activities.sugarlabs.org/activities).
	2. The display name of the activity.
	3. The activity icon.
	4. Link to the activity
	5. Short description of the activity.
	6. (optional) link to a help file.
	7. (optional) link to a note about the activity (such as why it doesn't work). 

These links are in a list which defines a page. 

var aslo = [
]

where aslo is the name of the main page.

var gtk3 = [
["4418","display title", "image.svg", "activities/helloworld-7.xo","description", "help/helloworld.html","notes/helloworld.html"],
]

shows that the Helloworld activity is shown in the gtk3 page.

#Contributors

There are many ways that users can help to make Sugar better.

##comments

Send a message to http://tony_anderson@usa.net about any problems you may have in using it or with any of the activities you install in Sugar.
An attempt will be made to respond as quickly as possible.

##Non-technical

Send a proposed description for an activity.
Send a proposed note or addtion to a note for an activity.

## Somewhat technical
Add or improve the help page for an activity. See https://help.sugarlabs.org/en/how_to_help.html for information on how to prepare a help page.

Currently less than 50 out of over 500 have help pages - so lots of opportunity.

## More technical
Add a new version of an activity. If a new activity - make it version 1. If a fix to an activity or a new capability for an activity, make the version number += 1 from the current version. Avoid, if possible, version numbers like 6.2.1 which are not integers.  

There are two types of activities: Python and Web. Python activities now require use of GTK+3. Fortunately web activities work in all Sugar environments. 

The book [Make your own Sugar activities!](http://write.flossmanuals.net/make-your-own-sugar-activities) provides a simple introduction to developing Sugar activities. The Helloworld activity for Python and Helloweb activity for web activities provide a simple example of what is needed. [A tutorial on how to port a Sugar activity to GTK+3](https://github.com/sugarlabs/sugar-docs/blob/master/src/gtk3-porting-guide.md) is available.

An activity does not have to feature advanced interactivity - there is plenty of need for lessons - explanatory text with images as in a textbook.

For example, a teacher could create a lesson by using the Helloweb activity. 

1. Download and install the HelloWeb activity.
2. It is in /home/olpc/Activities on an XO and in /home/username/Activities in Ubuntu Sugar. Using the Terminal activity, copy this directory to Lesson1.activity (cp -r HelloWeb.activity Lesson1.activity.
3. Change to this new activity.
4. Change to the 'activity' directory in this directory.
5. Using nano: nano activity.info - update the registration information.

>[Activity]
name = HelloWeb
activity_version = 4
bundle_id = org.sugarlabs.HelloWeb
exec = sugar-activity-web
icon = activity-helloweb
license = GPLv3

>[Activity]
name = Lesson 1. Big Cats
activity_version = 1
bundle_id = org.sugarlabs.Lesson1
exec = sugar-activity-web
icon = activity-lesson1
license = GPLv3

6. In the activity folder, mv activity-helloweb.svg to activity-lesson1.svg This will use that same icon for your activity as HelloWeb. You can replace this with a new icon.
7. Change to the main folder. Edit index.html to present the lesson. 
8. Restart Sugar (on an XO, reboot, in Ubuntu, logout and then login again.
8. Find your activity in Sugar's home view or list view. Launch it to see how you are doing.

A similar procedure can be used for Python activities.
