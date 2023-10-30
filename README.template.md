Notice:
This project is a forked version from https://github.com/h2y/Shadowrocket-ADBlock-Rules.  
Following changes have been made to keep updating the rules as the original repo was archived years ago and the rules are outdated.
* Replaced the top500 sites data source with top 10,000 sites from [Amazon Alex top 1million sites](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip).
* Optimized the `factory/auto_build.sh` to prevent the local changes to the repo from being discarded without prompt when running the script. 
* Updated the below QR codes to link to this repo config files instead of an outdated rule address. 
* Added Github Actions to automatically build the latest rules nightly.
------------------------------------------------------

## Rule list 


Rules | Proxied Sites | Direct Sites 
--- | ----------- | ------------- 
[Blacklist + Removing Ads](#Blacklist--Ads) |  Blocked sites by GFWList | Normal sites
[Blacklist](#Blacklist) |   |  
[Whitelist + Removing Ads](#Whitelist--Ads) | Other sites | Top500 sites that can be accessed directly
[Whitelist](#Whitelist) |   |  
[Separate sites foreign + Removing Ads](#Separate sites foreign--Ads) |  Foreign sites | Chines sites 
[Separate sites foreign](#Separate sites foreign) |   |  
[Direct globally + Removing Ads](#Direct globally) | / | All 
[Proxy globally + Removing Ads](#Proxy globally + Removing Ads) | All | /
[Going back to China + Removing Ads](#Going back to China--Ads) | Chines sites | foreign sites 
[Going back to China](#Going back to China) |   |  


## Sponsorship

This project doesn't accept any donations!
----------------------------------------

## Blacklist + Removing Ads

Including foreign sites cann't be accessed, others direct mode default.

- proxy: Blocked sites by GFWList
- direct: Normal sites
- Including ads removing

URL:[{{github_raw_content_endpoint}}sr_top500_banlist_ad.conf]({{github_raw_content_endpoint}}sr_top500_banlist_ad.conf)

![QR Code]({{qr_service_endpoint}}{{url_encoded_github_raw_content_endpoint}}sr_top500_banlist_ad.conf)

## Whitelist + Ads

Including foreign sites that can be accessed directly. Other sites applied proxy mode default.

- Direct: Sites in Top500 that can be accessed directly and Chinese sites
- Proxy: Other all foreign sites
- Including removing Ads

URL:[{{github_raw_content_endpoint}}sr_top500_whitelist_ad.conf]({{github_raw_content_endpoint}}sr_top500_whitelist_ad.conf)

![QR Code]({{qr_service_endpoint}}{{url_encoded_github_raw_content_endpoint}}sr_top500_whitelist_ad.conf)


## Blacklist

- Proxy: Sites blocked by GFWList
- Direct: Normal sites
- No Ads removing

URL:[{{github_raw_content_endpoint}}sr_top500_banlist.conf]({{github_raw_content_endpoint}}sr_top500_banlist.conf)

![QR Code]({{qr_service_endpoint}}{{url_encoded_github_raw_content_endpoint}}sr_top500_banlist.conf)


## Whitelist

- Direct: Sites in Top500 that can be accessed directly and Chinese sites
- Proxy: Other all foreign sites
- No Ads removing

URL:[{{github_raw_content_endpoint}}sr_top500_whitelist.conf]({{github_raw_content_endpoint}}sr_top500_whitelist.conf)

![QR Code]({{qr_service_endpoint}}{{url_encoded_github_raw_content_endpoint}}sr_top500_whitelist.conf)


## Separate sites foreign + Ads

Separate sites foreign. No proxy for Chinese sites, proxy applied for foreign sites. 

URL:[{{github_raw_content_endpoint}}sr_cnip_ad.conf]({{github_raw_content_endpoint}}sr_cnip_ad.conf)

![QR Code]({{qr_service_endpoint}}{{url_encoded_github_raw_content_endpoint}}sr_cnip_ad.conf)


## Separate sites foreign

Separate sites foreign. No proxy for Chinese sites, proxy applied for foreign sites. 

URL:[{{github_raw_content_endpoint}}sr_cnip.conf]({{github_raw_content_endpoint}}sr_cnip.conf)

![QR Code]({{qr_service_endpoint}}{{url_encoded_github_raw_content_endpoint}}sr_cnip.conf)


## Direct globally

- Direct: All requests
- Including Ads removing

URL:[{{github_raw_content_endpoint}}sr_direct_banad.conf]({{github_raw_content_endpoint}}sr_direct_banad.conf)

![QR Code]({{qr_service_endpoint}}{{url_encoded_github_raw_content_endpoint}}sr_direct_banad.conf)


## Proxy globally + Removing Ads

- Direct: Local network
- Proxy: Other requests
- Ads removing

URL:[{{github_raw_content_endpoint}}sr_proxy_banad.conf]({{github_raw_content_endpoint}}sr_proxy_banad.conf)

![QR Code]({{qr_service_endpoint}}{{url_encoded_github_raw_content_endpoint}}sr_proxy_banad.conf)


## Going back to China

- Direct: Foreign sites
- Proxy: China sites
- No Ads Removing

URL:[{{github_raw_content_endpoint}}sr_backcn.conf]({{github_raw_content_endpoint}}sr_backcn.conf)

![QR Code]({{qr_service_endpoint}}{{url_encoded_github_raw_content_endpoint}}sr_backcn.conf)


## Going back to China + Ads

- Direct: Foreign sites
- Proxy: China sites
- Ads Removing

URL:[{{github_raw_content_endpoint}}sr_backcn_ad.conf]({{github_raw_content_endpoint}}sr_backcn_ad.conf)

![QR Code]({{qr_service_endpoint}}{{url_encoded_github_raw_content_endpoint}}sr_backcn_ad.conf)
