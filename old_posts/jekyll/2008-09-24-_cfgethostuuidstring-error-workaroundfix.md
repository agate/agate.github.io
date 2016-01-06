--- 
layout: post
title: "_CFGetHostUUIDString Error WORKAROUND/FIX"
wordpress_id: 208
wordpress_url: http://www.agatezone.cn/code/?p=208
---
<blockquote>This workaround will help you to remove the "_CFGetHostUUIDString: unable to determine UUID for host. Error: 35" error.

1.) BACKUP your /Library/Preferences/SystemConfiguration/NetworkInterfaces.plist
2.) Open /Library/Preferences/SystemConfiguration/NetworkInterfaces.plist
3.) ADD AFTER &lt;string&gt;Ethernet&lt;/string&gt;&lt;/dict&gt; the following:
&lt;dict&gt;
&lt;key&gt;BSD Name&lt;/key&gt;
&lt;string&gt;en3&lt;/string&gt;
&lt;key&gt;IOBuiltin&lt;/key&gt;
&lt;false/&gt;
&lt;key&gt;IOInterfaceType&lt;/key&gt;
&lt;integer&gt;6&lt;/integer&gt;
&lt;key&gt;IOInterfaceUnit&lt;/key&gt;
&lt;integer&gt;3&lt;/integer&gt;
&lt;key&gt;IOLocation&lt;/key&gt;
&lt;string&gt;&lt;/string&gt;
&lt;key&gt;IOMACAddress&lt;/key&gt;
&lt;data&gt;
ABbPoF5V
&lt;/data&gt;
&lt;key&gt;IOPathMatch&lt;/key&gt;
&lt;string&gt;IOService:/AppleACPIPlatformExpert/PCI0@0/AppleACPIPCI/P0P3@1C,2/
IOPCI2PCIBridge/pci14e4,4311@0/AirPort_Brcm43xx/IO80211Interface&lt;/string&gt;
&lt;key&gt;SCNetworkInterfaceType&lt;/key&gt;
&lt;string&gt;IEEE80211&lt;/string&gt;
&lt;/dict&gt;
4.) IF you have more than 3 interfaces or there is an "en3" interface change it to "en4" or a higher number, don't forget to change this "&lt;integer&gt;3&lt;/integer&gt;" to "&lt;integer&gt;4&lt;/integer&gt;".
5.) You need to REBOOT
6.) If this work for you please tell me.
7.) If this workaround did not work please provide your system.log and your NetworkInterfaces.plist.

Why does this error happen?
Well at looking at the source code of the configd there is a plugin "InterfaceNamer" it seams the plugin will always skip interfaces
that are IOBuiltin = false. The "&lt;key&gt;IOBuiltin&lt;/key&gt;" cannot be changed because the plugin will check and restore it on next boot.
But it does not check if wireless interfaces &lt;key&gt;SCNetworkInterfaceType&lt;/key&gt;&lt;string&gt;IEEE80211&lt;/string&gt; are IOBuiltin.
Like I say this is only a workaround and there will be more need of testing.</blockquote>

from url: <a href="http://sneosx86.freeflux.net/blog/archive/2007/11/10/_cfgethostuuidstring-error-workaround-fix.html">http://sneosx86.freeflux.net/blog/archive/2007/11/10/_cfgethostuuidstring-error-workaround-fix.html</a>
