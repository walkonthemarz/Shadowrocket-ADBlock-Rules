## The most complete iOS Shadowrocket rules

A collection of Shadowrocket rules with ad filtering. The rules define which sites connect directly and which use a proxy. They are plain-text configs and do not provide proxy access themselves. Configs are generated automatically from maintained templates and public lists.

**All rules are rebuilt daily at 08:00 Beijing time.**

On a phone? Open the [documentation page](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules).

### Features

- Blacklist converted from the latest [GFWList](https://github.com/gfwlist/gfwlist)
- Blocked domains from [Greatfire Analyzer](https://github.com/Loyalsoldier/cn-blocked-domain)
- `EasyList`, `EasyList China`, `Peter Lowe's list`, and `Chengfeng rules` converted to SR rules, with ads and duplicates removed
- Custom ad filtering for iOS web, in-app, and video ads
- Multiple configs, freely switchable
- Built for Shadowrocket
- Optimized [Apple and CDN direct rules](https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/apple.china.conf)
- Shortcuts and automation support
- Lazy configs with proxy groups
- Rebuilt top500 connectivity table; [submit updates](https://github.com/walkonthemarz/Shadowrocket-ADBlock-Rules/blob/build/factory/resultant/top500_manual.list)

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

- LAN requests are always direct.

## Usage

1. Scan the QR code with Safari or Shadowrocket.
2. Or open Shadowrocket -> Config -> +, paste the rule URL, and tap Download.

Reconnect Shadowrocket after downloading to apply the new config.

## Auto-update

1. Install the [Shortcut](https://www.icloud.com/shortcuts/20bd590bc99e4ef0a157d2fe6e8c273d) and enter the rule URL.
2. In Shortcuts -> Automation -> + -> Create Personal Automation -> Time of Day, set 08:05 or later, add the "Run Shortcut" action, select "Shadowrocket rule auto-update", and disable "Ask Before Running" if desired.

If google.cn redirects fail: Config -> rule ℹ️ -> HTTPS Decryption -> turn it off and on again; install and fully trust the root certificate when prompted.

## FAQ

**Do thousands of rules slow down Shadowrocket?**

No. Shadowrocket builds a search tree and caches matches, so lookup is effectively O(1).

**Which config should I use?**

The blacklist defaults to direct for unknown sites; the whitelist defaults to proxy. If unsure, download both and switch.

**Can I request a site?**

Open an [issue](https://github.com/walkonthemarz/Shadowrocket-ADBlock-Rules/issues).

**Why are some ads still visible?**

App and video ad strategies change frequently, so 100% blocking is not guaranteed. YouTube ads cannot be removed by URL matching alone.

**Apple Podcasts from other regions will not load.**

Proxy `podcasts.apple.com`, `bookkeeper.itunes.apple.com`, `play.itunes.apple.com`, and `xp.apple.com`. See [#214](https://github.com/DivineEngine/Profiles/issues/214).

**Safari will not redirect google.cn.**

Config -> rule ℹ️ -> HTTPS Decryption -> turn it off and on again; install and fully trust the root certificate when prompted.

## Contributing

Report issues in [Issues](https://github.com/walkonthemarz/Shadowrocket-ADBlock-Rules/issues).

Edit the three `manual_*.txt` files in the [factory directory](https://github.com/walkonthemarz/Shadowrocket-ADBlock-Rules/tree/build/factory). Send pull requests to the `build` branch.

To use your own copy: fork the repo, uncheck "Copy the release branch only", and enable Actions.

----------------------------------------

## Blacklist + Ads

Proxy: blocked sites (GFWList). Direct: normal sites. Includes ad filtering.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_top500_banlist_ad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_top500_banlist_ad.png)

## Whitelist + Ads

Direct: directly accessible top500 sites and Chinese sites. Proxy: all other foreign sites. Includes ad filtering.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_top500_whitelist_ad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_top500_whitelist_ad.png)

## Blacklist

Proxy: blocked sites (GFWList). Direct: normal sites. No ad filtering.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_top500_banlist.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_top500_banlist.png)

## Whitelist

Direct: directly accessible top500 sites and Chinese sites. Proxy: all other foreign sites. No ad filtering.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_top500_whitelist.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_top500_whitelist.png)

## China and Global split + Ads

Direct: Chinese sites. Proxy: foreign sites. Includes ad filtering. Foreign sites always use the proxy; some Hong Kong, Macau, and Taiwan sites may be faster this way.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_cnip_ad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_cnip_ad.png)

## China and Global split

Direct: Chinese sites. Proxy: foreign sites. No ad filtering. Foreign sites always use the proxy; some Hong Kong, Macau, and Taiwan sites may be faster this way.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_cnip.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_cnip.png)

## Direct + Ads

Direct: all requests. Includes ad filtering.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_direct_banad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_direct_banad.png)

## Proxy + Ads

Direct: LAN requests. Proxy: all other requests. Includes ad filtering.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_proxy_banad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_proxy_banad.png)

## Back to China

For overseas users. Direct: foreign sites. Proxy: Chinese sites. No ad filtering.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_backcn.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_backcn.png)

## Back to China + Ads

For overseas users. Direct: foreign sites. Proxy: Chinese sites. Includes ad filtering.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_backcn_ad.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_backcn_ad.png)

## Ads only

Ad filtering only; no proxy or direct rules. Combine with another config.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/sr_ad_only.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/sr_ad_only.png)

----------------------------------------

The following configs are generated from [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script):

## Lazy config

Synced from [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket). Simple config, broad coverage, and separate routing for common domestic and foreign apps.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/lazy.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/lazy.png)

## Lazy config with policy groups

Synced from [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket). Adds automatic selection of the lowest-latency node type and flexible streaming routing through "Proxy Groups". Configure under i -> Proxy Groups after downloading.

Rule URL: <https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/lazy_group.conf>

![QR code](https://walkonthemarz.github.io/Shadowrocket-ADBlock-Rules/figure/lazy_group.png)

## Acknowledgements

- Thanks to [@h2y](https://github.com/h2y) and the [Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) community.
- Thanks to the maintainers of the lazy configs.
- Thanks to [@hfdem](https://github.com/hfdem).

### References

- [gfwlist](https://github.com/gfwlist/gfwlist)
- [Greatfire Analyzer](https://github.com/Loyalsoldier/cn-blocked-domain)
- [Chengfeng ad-filtering rules](https://github.com/xinggsf/Adblock-Plus-Rule)
- [EasyList China](https://adblockplus.org/)
- [Peter Lowe's ad and tracking server list](https://pgl.yoyo.org/)
- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)
- [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket)
