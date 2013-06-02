---
layout: post
title: "Trying out Pixate - CSS for iOS app Development"
date: 2013-01-23 22:09
comments: true
author: "Patrick Goddi"
categories: 
---
Recently I have been using RubyMotion for iOS development; I really  appreciate developing in Ruby, and prefer Emacs to Xcode. Compared to using interface builder, styling apps can be a challenge. It is possible to use RubyMotion with XIB files created in Xcode's Interface Builder, but I have been trying to avoid this. I am striving for a more web-app like design and development workflow. 

I have been using [teacup](https://github.com/rubymotion/teacup), which takes a declarative approach to styling and uses a CSS-like DSL. Although I liked teacup, I had been anxiously awaiting the arrival of [Pixate](http://www.pixate.com/) because of its support for CSS-based styling. Pixate became generally available this month, and I purchased a license. The license is $199, and although expensive, a small price compared to time saved if it works. Since I already do a lot of CSS work on the web side it seems like a nice way to leverage my CSS skills and experience. The Pixate team along with the RubyMotion team created a [RubyMotion-Pixate gem](https://github.com/Pixate/RubyMotion-Pixate) that makes it easy to get Pixate working with RubyMotion. 

After 2 days of coding I have my basic controllers in place as well as several TableViewControllers. I have used Pixate to style many of the elements. With Pixate you can style with four types of selectors:

* element type selector - Select a control by element name
* universal selector - Select any control
* class selector - Select a control by class name
* id selector - Select a control by ID

It also supports attribute selectors and pseudo classes. See the [complete list](http://cdn.pixate.com/docs/engine/ios/1.0/Pixate%20Engine%20for%20iOS%20Styling%20Reference.html) for more information on selectors and styling.

One really nice feature is the ability to set up Pixate to dynamically change your app in the simulator when you update the CSS. This is an awesome feature. To set it up add these two  _PXStylesheet_ lines to your app_delegate.rb file near the end of the _application_ method:
     
     def application(application, didFinishLaunchingWithOptions:launchOptions)
        ...
        PXStylesheet.styleSheetFromFilePath('path-to/default.css', withOrigin:0)
        PXStylesheet.currentApplicationStylesheet.monitorChanges = true  
        true
     end


I was only able to get it to work by providing the absolute path to the css file, so add your absolute path in place of _path-to_ in the above method call. I will post if I figure out how to do a relative path, I hate putting in absolute paths. 

**Warning**: I found that Pixate 1.0.2 does not work properly on the device if these two statements are left in the app delegate when compiling for the device. If your styles are not being picked up on the device this may be the reason. To get around this during development I put in a test for simulator using the _Device.simulator?_ method in [Bubblewrap](https://github.com/rubymotion/BubbleWrap),

     def setup_pixate_monitor 
       PXStylesheet.styleSheetFromFilePath('path-to/default.css', withOrigin:0)
       PXStylesheet.currentApplicationStylesheet.monitorChanges = true
     end

Then include this conditional call:
     
     setup_pixate_monitor if Device.simulator?

So far Pixate has mostly worked as expected, but there was one odd issue. I had expected that I could create zero-sized frames and allow CSS to style them to the correct size. For example creating a new label object might look like this.

     @name_label = UILabel.alloc.initWithFrame(CGRectZero)
     @name_label.styleId = 'name_label'


CGRectZero, a CGRect constant, will set the frame to size [0,0][0,0]. Then the CSS style definition below should set the frame size correctly.

     #name_label { 
	   position:fixed;
	   top              :20px;
	   left             :5px;
 	   width            :300px;
	   height           :30px;  
	   font-size        :16px;
	   font-align       :center;  
     } 


I would expect the frame to be set to [5,20][300, 30] when the application is run. Instead the frame remains set to [0,0][0,0], so the text in the label is not displayed in the interface. This [0,0][0,0] frame size is confirmed with REPL using the tree command that comes with the [sugarcube gem](https://github.com/rubymotion/sugarcube). 

When I set the frame to a non-zero size when creating the UI object, then the CSS style is picked up and the frame size is set correctly by Pixate. Very odd, I am assuming this to be a bug, but maybe there was a reason to leave zero-sized frames unaltered by CSS. Typically CGRectZero frames are used to hide UI elements until they are ready to be used, or until the dimensions are known based on content.  If a CSS selector matched zero-sized frames I suppose this could lead to some unexpected behavior for iOS developers accustom to zero-sized frames not being displayed until the specifically resize them in code.

In the end I created a new global constant
   
     CSSRect = [0, 0], [1, 0] 

and this allows the CSS to do its job. So

     @name_label = UILabel.alloc.initWithFrame(CSSRect)
     @name_label.styleId = 'name_label'

allows me to create frames that are then altered to the correct size via CSS. I also found that using CGRectInfinite works as well. Basically it sets a huge rectangle but the CSS resizes it as expected.

The  [RubyMotion-Pixate gem](https://github.com/Pixate/RubyMotion-Pixate) also adds REPL support for changing the style via REPL. This is handy, but I find the dynamic updating via the CSS file to be easier to use.

The Pixate Engine consists of two core technologies: a 2D graphics engine and a CSS styling engine. So far my focus has been using the CSS styling engine.  By using a styling rendering engine, design execution can be pushed to run-time. One of the benefits of this approach is the ability to dynamically modify the look of an app, which can be useful in user testing, including A/B testing. For this, Pixate allows CSS to be loaded via a URL, much like a web browser. I am sure there will be performance implications of this dynamic rendering approach, so this will also have to be explored as a cost versus the benefit of dynamic styling.

I really liked Colin Gray's ideas around teacup, and the rubyesque way it integrated with rubymotion. 

     @search = subview(UITextField, :search)


It would be interesting if this syntax could be used with Pixate versus the less elegant: 

     @search = UITextField.alloc.initWithFrame(CSSRect)
     @search.styleId = 'search'


I have only just begun to use Pixate, there may be possibilities for making the calls a bit more elegant without writing too many helpers. 

I will add more posts as I learn more.


 