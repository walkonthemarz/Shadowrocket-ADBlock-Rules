## The most complete iOS Shadowrocket rules

### Update notice

The original author [h2y](https://github.com/h2y) has stopped maintaining [Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules), leaving Shadowrocket without such carefully categorized and refined rules. I have therefore decided to use my limited ability and understanding to update and maintain this project. **All rules are updated and published daily at 08:00 Beijing time.**

### Before you start — protect yourself

Google's search experience in both Chinese and English is better than Baidu's, and binge-watching American shows, following celebrities on Instagram, and checking out Trump on Twitter are all quite interesting. However, the more people and things I see, the more I want to say something here to warn everyone who passes by:

**Please protect yourself.** We think we are breaking down information barriers, but in fact we are breaking down the barriers that protect us. Because the outside internet really does contain a lot of misleading speech, from various interest groups frantically brainwashing Chinese netizens, and they often like to call themselves champions of equality and freedom — but think about it carefully: is that really the case? I only know that the United States is the country best at using public opinion, combining big data to subtly change your views. If you accidentally see certain viewpoints while browsing, be sure to retain your ability to think independently. If you are someone who is easily led astray, I suggest returning behind the barrier.

These rules are provided only to help everyone study and work more conveniently. If you are an extreme political person who opposes the above views, or if you have already been brainwashed, please leave immediately; this project is not open to you.

------------------------------------------------------

This is a collection of useful Shadowrocket rules, developed for [Shadowrocket](https://liguangming.com/Shadowrocket), with ad filtering support. The rules define which sites can be accessed directly and which must go through a proxy. A rule is a plain text file and cannot provide magical internet access. It is generated periodically by Python according to certain rules and templates, and is gradually improved with the power of open source and community contributions.

**If you are viewing this page on a phone, [please click here](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules) to view the full documentation.**

**These rules have the following features:**

- The blacklist is automatically converted from the latest [GFWList](https://github.com/gfwlist/gfwlist);
- Includes blocked domains detected by [Greatfire Analyzer](https://github.com/Loyalsoldier/cn-blocked-domain);
- Automatically converts the latest `EasyList`, `EasyList China`, `Peter Lowe's ad and tracking server list`, and `Chengfeng rules` into SR rules, thoroughly removing ads and duplicates;
- Includes custom ad-filtering rules for iOS web ads, in-app ads, and video ads;
- Provides multiple rule files for you to choose from or switch between freely;
- Developed specifically for Shadowrocket, ensuring compatibility;
- Optimizes [Apple and its CDN domains](https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/apple.china.conf);
- Convenient Shortcuts and automation integration, with daily automatic rule updates;
- Adds lazy configs that use proxy groups;
- Since the world's top 500 website list is no longer available without an account or for free, the original top500 detection method no longer works. I have reconstructed a new top500 website connectivity table based on the old top500 list. **At the same time, I hope everyone can help submit a pull request with the latest top500 list: [format](https://github.com/walkonthemarz/Shadowrocket-ADBlock-Rules/blob/build/factory/resultant/top500_manual.list)**
- **All published rules are updated and released daily at 08:00 Beijing time**

## Rule list

![Rule selection guide](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/guide.png)

Rule | Sites forced through proxy | Sites forced direct
--- | ----------- | -------------
[Blacklist + Ads](#blacklist--ads) | Blocked sites (GFWList) | Normal sites
[Blacklist](#blacklist) | |
[Whitelist + Ads](#whitelist--ads) | Other sites | Directly accessible top500 sites, Chinese sites
[Whitelist](#whitelist) | |
[China/Global split + Ads](#china-and-global-split--ads) | Foreign sites | Chinese sites
[China/Global split](#china-and-global-split) | |
[Direct + Ads](#direct--ads) | / | All
[Proxy + Ads](#proxy--ads) | All | /
[Back to China + Ads](#back-to-china--ads) | Chinese sites | Foreign sites
[Back to China](#back-to-china) | |
[Ads only](#ads-only) | |
[Lazy config](#lazy-config) | Foreign sites | Chinese sites
[Lazy config with policy groups](#lazy-config-with-policy-groups) | Foreign sites | Chinese sites

- For all the rules above, LAN requests are always direct.
- You can download multiple rules and switch between them.

## How to use these rules

Method 1: Scan the QR code with Safari or Shadowrocket.
Method 2: In the Shadowrocket app, go to the [Config] page, tap the plus button in the top-right corner, paste the rule file URL into the URL field, and tap "Download".

It is best to disconnect and reconnect Shadowrocket once to ensure the new rule file takes effect.

## How to update automatically
Step 1: Install the [Shortcut](https://www.icloud.com/shortcuts/20bd590bc99e4ef0a157d2fe6e8c273d) and fill in the rule file URL.
Step 2: Open "Automation" under "Shortcuts", tap the plus button in the top-right corner, tap "Create Personal Automation", choose "Time of Day", set the time to 08:05 or later (rule generation takes some time), tap Next, tap Add Action, select the Apps tab, find Shortcuts, choose "Run Shortcut", tap the light-colored "Shortcut", choose "Shadowrocket rule auto-update", tap Next, turn off "Ask Before Running" (optional), and tap Done.

If Safari cannot properly redirect requests to google.cn, after each update tap the ℹ️ next to the rule, tap HTTPS Decryption, turn HTTPS Decryption off, go back, and turn it on again; redirects should then work normally.

## Recommended sites

**[IP111](http://ip111.cn/)**

A great IP lookup site that can query your domestic and overseas IPs at the same time, as well as your Google IP.

**[hzy's blog](https://hzy.pw/)**

I am a university student addicted to technology. This is my personal blog where I share interesting things and my own views. Welcome to visit~

**[DuckSoft's blog](https://www.ducksoft.site/)**

INTP | Jack of all trades | I use Arch BTW

**[Blog](https://diazepam.cc/)**

A child who loves life and sunshine.

## FAQ

- **Will thousands of lines of proxy rules affect internet speed?**

> No.
>
> I used to think this was a rule file executed for every network packet, matching rules line by line, so it needed to be as concise as possible. But after talking with the SR author, I realized this was a misunderstanding. When SR loads rules, it builds a search tree, which can be understood as a finite state machine DFA that processes hostnames from right to left, not line-by-line matching, and it also caches each match result with a hash.
>
> In other words, a 2,000-line rule and a 50-line rule both have the same order of time complexity O(1) in SR.

- **You provide so many rules; how do I choose the right one for me?**

> The most commonly used rules are the blacklist and whitelist. The difference is how they treat `unknown websites`: the blacklist defaults to direct, while the whitelist defaults to proxy. If your choice anxiety flares up, just download both and switch between the blacklist and whitelist; then you're all set.

- **You provide so many rules, but none of them is what I want o(>.<)o**

> If you have any suggestions or questions, [please contact me](#feedback).

- **Ad filtering is not complete?**

> These rules do not guarantee 100% filtering of all ads, especially video ads. Unlike web ads, apps such as Youku may change their ad strategy with every update, so it is difficult to guarantee real-time effectiveness of ad blocking. YouTube ads, in particular, cannot be completely removed through simple URL matching.

- **Apple Podcasts from other regions fail to load** (thanks to [@jesuiseric](https://t.me/jesuiseric))

> Please add `podcasts.apple.com`, `bookkeeper.itunes.apple.com`, `play.itunes.apple.com`, and `xp.apple.com` to the proxy. See [#214](https://github.com/DivineEngine/Profiles/issues/214) for details.

- **Safari cannot properly redirect requests to google.cn**

> Tap Config -> tap the ℹ️ next to the rule file currently in use under Local Files -> HTTPS Decryption -> turn on the switch in the top-right corner -> Install Certificate -> Allow -> open System Settings -> Downloaded Profile -> Install -> enter passcode -> Install -> General -> About -> Certificate Trust Settings -> fully trust the newly installed root certificate, and redirects will work normally.

## Feedback

Any issues are welcome in [Issues](https://github.com/walkonthemarz/Shadowrocket-ADBlock-Rules/issues).

Your feedback will make these rules even better.

**How to contribute code?**

Usually, you only need to modify the three `manual_*.txt` files under the [factory directory](https://github.com/walkonthemarz/Shadowrocket-ADBlock-Rules/tree/build/factory). **Please send pull requests to the build branch.**

**How to have your own customized rules?**

Click Fork in the top-right corner, uncheck `Copy the release branch only`, and enable Actions in your own repository.

## Donations

This project does not accept donations of any kind, because free access to the internet is everyone's right, and there is no need to pay more for it.

However, as a censorship-circumvention rule set, it will inevitably miss some websites, and we need everyone to help improve it. When you find something that does not work well, please turn on SR's logging, check which blocked domain is going direct, or which directly accessible domain is going through the proxy.

Send the information that needs to be changed back to me, and everyone's efforts will make these rules better and better!

----------------------------------------

## Blacklist + Ads

The blacklist includes overseas websites that cannot be accessed, and defaults to direct for uncertain websites.

- Proxy: blocked websites (GFWList)
- Direct: normal websites
- Includes ad filtering

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_top500_banlist_ad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_top500_banlist_ad.png)

## Whitelist + Ads

The whitelist includes overseas websites that can be accessed, and defaults to proxy for uncertain websites.

- Direct: directly accessible overseas websites among the top500 sites, and Chinese websites
- Proxy: all other overseas websites are proxied by default
- Includes ad filtering

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_top500_whitelist_ad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_top500_whitelist_ad.png)

## Blacklist

Many browsers now have built-in ad filtering, and ad-filtering rules are actually quite bloated. If you do not need to globally filter in-app ads and video ads, you can choose this version without ad filtering.

- Proxy: blocked websites (GFWList)
- Direct: normal websites
- No ad filtering

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_top500_banlist.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_top500_banlist.png)

## Whitelist

Many browsers now have built-in ad filtering, and ad-filtering rules are actually quite bloated. If you do not need to globally filter in-app ads and video ads, you can choose this version without ad filtering.

- Direct: directly accessible overseas websites among the top500 sites, and Chinese websites
- Proxy: all other overseas websites are proxied by default
- No ad filtering

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_top500_whitelist.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_top500_whitelist.png)

## China and Global split + Ads

Splits China and the rest of the world: Chinese websites go direct, foreign websites go through the proxy. Includes ad filtering. Foreign websites always go through the proxy; for some Hong Kong, Macau, and Taiwan websites, this can actually be faster than a direct connection.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_cnip_ad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_cnip_ad.png)

## China and Global split

Splits China and the rest of the world: Chinese websites go direct, foreign websites go through the proxy. No ad filtering. Foreign websites always go through the proxy; for some Hong Kong, Macau, and Taiwan websites, this can actually be faster than a direct connection.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_cnip.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_cnip.png)

## Direct + Ads

If you want to use SR as a global iOS ad-blocking tool, this rule will help.

- Direct: all requests
- Includes ad filtering

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_direct_banad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_direct_banad.png)

## Proxy + Ads

If you want to use SR as a global iOS ad-blocking and global censorship-circumvention tool, this rule will help.

- Direct: LAN requests
- Proxy: all other requests
- Includes ad filtering

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_proxy_banad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_proxy_banad.png)

## Back to China

For overseas Chinese, allowing them to return inside the firewall and enjoy some domestic internet services.

- Direct: foreign websites
- Proxy: Chinese websites
- No ad filtering

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_backcn.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_backcn.png)

## Back to China + Ads

For overseas Chinese, allowing them to return inside the firewall and enjoy some domestic internet services.

- Direct: foreign websites
- Proxy: Chinese websites
- Includes ad filtering

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_backcn_ad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_backcn_ad.png)

## Ads only

Contains only ad-filtering rules, with no proxy/direct rules. Used together with other rules.

- Contains only ad-filtering rules, with no proxy/direct rules. No other configuration.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_ad_only.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_ad_only.png)

----------------------------------------

The following rules are generated based on [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script):

## Lazy config

Synced from [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket). No fiddling required; works out of the box.

- Simple configuration
- Broad rule coverage
- Separate routing for common domestic and foreign apps

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/lazy.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/lazy.png)

## Lazy config with policy groups

Synced from [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket). No fiddling required; works out of the box. After downloading the rules, you can configure it yourself under i -> Proxy Groups.

- Simple configuration
- Broad rule coverage
- Separate routing for common domestic and foreign apps
- Adds automatic switching to the lowest-latency node type
- Flexibly adjusts streaming traffic routing through "Proxy Groups"

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/lazy_group.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/lazy_group.png)

## Acknowledgements

- Thanks to [@h2y](https://github.com/h2y) and all community developers who have selflessly helped [Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules);
- Thanks to the creators and maintainers of the lazy rules;
- Thanks to [@hfdem](https://github.com/hfdem) for their help, recognition, and support!

### Referenced by this project
- [gfwlist](https://github.com/gfwlist/gfwlist)
- [Greatfire Analyzer](https://github.com/Loyalsoldier/cn-blocked-domain)
- [Chengfeng ad-filtering rules](https://github.com/xinggsf/Adblock-Plus-Rule)
- [EasyList China](https://adblockplus.org/)
- [Peter Lowe's ad and tracking server list](https://pgl.yoyo.org/)
- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)
- [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket)

## Stargazers over time

[![Stargazers over time](https://starchart.cc/walkonthemarz/Shadowrocket-ADBlock-Rules.svg)](https://starchart.cc/walkonthemarz/Shadowrocket-ADBlock-Rules)
