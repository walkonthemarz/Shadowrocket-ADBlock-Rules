## Rules for iOS

This project is a forked version from https://github.com/h2y/Shadowrocket-ADBlock-Rules.  
Following changes have been made to keep updating the rules as the original repo was archived years ago and the rules are outdated.
* Replaced the top500 sites data source with top 10,000 sites from [Amazon Alex top 1million sites](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip).
* Optimized the `factory/auto_build.sh` to prevent the local changes to the repo from being discarded without prompt when running the script. 
* Updated the below QR codes to link to this repo config files instead of an outdated rule address. 
* Added Github Actions to automatically build the latest rules nightly.
------------------------------------------------------


----------------------------------------

## Black list + ads

黑名单中包含了境外网站中无法访问的那些，对不确定的网站则默认直连。

- proxy：GFWList
- direct：normal sites
- filtering ads

Rule URL：[https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_top500_banlist_ad.conf](https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_top500_banlist_ad.conf)

![QR code](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https%3A%2F%2Fraw.githubusercontent.com%2Fwalkonthemarz%2FShadowrocket-ADBlock-Rules%2Fmaster%2Fsr_top500_banlist_ad.conf)

## White list + ads
- direct：sites in top500 can be accessed directly, and sites in CN
- proxy：rest sites affshore
- filtering ads

Rule URL：[https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist_ad.conf](https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist_ad.conf)

![QR code](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https%3A%2F%2Fraw.githubusercontent.com%2Fwalkonthemarz%2FShadowrocket-ADBlock-Rules%2Fmaster%2Fsr_top500_whitelist_ad.conf)


## Filtering black list

- 代理：被墙的网站（GFWList）
- 直连：正常的网站
- 不包含广告过滤

规则地址：[https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_top500_banlist.conf](https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_top500_banlist.conf)

![二维码](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https%3A%2F%2Fraw.githubusercontent.com%2Fwalkonthemarz%2FShadowrocket-ADBlock-Rules%2Fmaster%2Fsr_top500_banlist.conf)


## 白名单过滤

现在很多浏览器都自带了广告过滤功能，而广告过滤的规则其实较为臃肿，如果你不需要全局地过滤 App 内置广告和视频广告，可以选择这个不带广告过滤的版本。

- 直连：top500 网站中可直连的境外网站、中国网站
- 代理：默认代理其余的所有境外网站
- 不包含广告过滤

规则地址：[https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist.conf](https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist.conf)

![二维码](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https%3A%2F%2Fraw.githubusercontent.com%2Fwalkonthemarz%2FShadowrocket-ADBlock-Rules%2Fmaster%2Fsr_top500_whitelist.conf)


## 国内外划分 + 广告

国内外划分，对中国网站直连，外国网站代理。包含广告过滤。国外网站总是走代理，对于某些港澳台网站，速度反而会比直连更快。

规则地址：[https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_cnip_ad.conf](https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_cnip_ad.conf)

![二维码](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https%3A%2F%2Fraw.githubusercontent.com%2Fwalkonthemarz%2FShadowrocket-ADBlock-Rules%2Fmaster%2Fsr_cnip_ad.conf)


## 国内外划分

国内外划分，对中国网站直连，外国网站代理。不包含广告过滤。国外网站总是走代理，对于某些港澳台网站，速度反而会比直连更快。

规则地址：[https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_cnip.conf](https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_cnip.conf)

![二维码](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https%3A%2F%2Fraw.githubusercontent.com%2Fwalkonthemarz%2FShadowrocket-ADBlock-Rules%2Fmaster%2Fsr_cnip.conf)


## 直连去广告

如果你想将 SR 作为 iOS 全局去广告工具，这个规则会对你有所帮助。

- 直连：所有请求
- 包含广告过滤

规则地址：[https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_direct_banad.conf](https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_direct_banad.conf)

![二维码](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https%3A%2F%2Fraw.githubusercontent.com%2Fwalkonthemarz%2FShadowrocket-ADBlock-Rules%2Fmaster%2Fsr_direct_banad.conf)


## 代理去广告

如果你想将 SR 作为 iOS 全局去广告 + 全局翻墙工具，这个规则会对你有所帮助。

- 直连：局域网请求
- 代理：其余所有请求
- 包含广告过滤

规则地址：[https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_proxy_banad.conf](https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_proxy_banad.conf)

![二维码](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https%3A%2F%2Fraw.githubusercontent.com%2Fwalkonthemarz%2FShadowrocket-ADBlock-Rules%2Fmaster%2Fsr_proxy_banad.conf)


## 回国规则

提供给海外华侨使用，可以回到墙内，享受国内的一些互联网服务。

- 直连：国外网站
- 代理：中国网站
- 不包含广告过滤

规则地址：[https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_backcn.conf](https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_backcn.conf)

![二维码](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https%3A%2F%2Fraw.githubusercontent.com%2Fwalkonthemarz%2FShadowrocket-ADBlock-Rules%2Fmaster%2Fsr_backcn.conf)


## 回国规则 + 广告

提供给海外华侨使用，可以回到墙内，享受国内的一些互联网服务。

- 直连：国外网站
- 代理：中国网站
- 包含广告过滤

规则地址：[https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_backcn_ad.conf](https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/sr_backcn_ad.conf)

![二维码](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https%3A%2F%2Fraw.githubusercontent.com%2Fwalkonthemarz%2FShadowrocket-ADBlock-Rules%2Fmaster%2Fsr_backcn_ad.conf)
