# -*- coding:UTF-8 -*-

from googletrans import Translator

translator = Translator(service_urls=['translate.google.cn'])
source = '''
<p>*We have a preview of OWN’s new unscripted drama “To Have  To Hold: Charlotte,” an hour-long series from Truly Original that will take a candid look inside the lives of five high-powered Black couples in Charlotte, North Carolina.</p>
<p>The series follows the couples and the real challenges they face, from financial stress, to issues with intimacy, to the ups and downs of parenthood.</p>
<p>“These tight-knit friends like to let loose and have fun, and while the passionate and often opinionated couples may have their differences, they will ultimately do anything for each other,” reads the official synopsis. “As marriages and friendships are put to the test, will they have the love and strength needed to thrive or will some of these relationships crack under the pressure?”</p>
<p>OTHER NEWS YOU MIGHT HAVE MISSED:?Willow Smith in Put Up or Shut Up Predicament After Being Offered Creative Control of Adult Film Project</p>
<p><img src='https://i0.wp.com/eurweb.com/wp-content/uploads/2019/05/oiuhg.jpg?resize=630%2C504ssl=1' ></p>
<p>“To Have  To Hold: Charlotte” is produced by Truly Original, part of Endemol Shine North America. Executive producers are Steven Weinstock, Glenda Hersh, Lauren Eskelin, Stephen Mintz, Lucas Howe, Shari Ortner and Wendy Credle.</p>
<p>Check out two advance clips from the first episode “All That Glitters Isn’t Gold” below, and tune-in to the series premiere on Saturday, June 1 at 10:00 p.m. ET/PT.</p>
<p>OWN’s Saturday night unscripted programming lineup also includes “Iyanla: Fix My Life,” “Ready to Love,” “Love  Marriage: Huntsville,” “Black Love,” and “The Book of John Gray.”</p>
<p>About Truly Original
Truly Original creates a broad range of scripted and unscripted programming for television and digital platforms. Run by Emmy? Award-winning producers Glenda Hersh and Steven Weinstock, who serve as Truly Original’s co-presidents and CEOs, the company is a subsidiary of Endemol Shine North America. In addition to To Have  To Hold: Charlotte for OWN, Truly Original’s series include Deal or No Deal for CNBC, hosted by Howie Mandel; The Real Housewives of Atlanta, The Real Housewives of Potomac, Dont Be Tardy, Shahs of Sunset and Summer House, and the upcoming Indian-ish for Bravo; Ink Master and Ink Master: Grudge Match for Paramount; Teen Mom: Young Moms Club for MTV; Basketball Wives for VH1; Swamp People for History; and many others.</p>

<p>Tyyawdi Introduces the Concept of “Nesting” to David:</p>
<p></p>
<p>Christine and Darhyl Are Not Seeing Eye to Eye on Kids:?</p>
<p></p>
<h3>Share this:</h3>Click to share on Twitter (Opens in new window)Click to share on Facebook (Opens in new window)'''

#text = translator.translate(source,src='zh-cn',dest='en').text

text = translator.translate(source,src='en',dest='zh-cn').text
print(text)
