cookies = {"ucsd.edu": {"pwd": "abc"},
           "python-news.com": {"font-pref": "courier", "session": "XGKE"}}

def set_cookie(cookies, site, name, value):
    if site not in cookies:
        cookies[site] = {}
    site_cookies = cookies[site]
    site_cookies[name] = value

##def get_cookie(cookies, site, name):
##    if site not in cookies:
##        return "site name not found: " + site
##    site_cookies = cookies[site]
##    if name not in site_cookies:
##        return "cookie name " + name + " not found in site " + site
##    return site_cookies[name]

def get_cookie(cookies, site, name, default):
    if site not in cookies:
        return default
    site_cookies = cookies[site]
    if name not in site_cookies:
        return default
    return site_cookies[name]

##def get_cookie_names_for_site(cookies, site):
##    if site not in cookies:
##        return []
##    return list(cookies[site].keys())

def get_cookie_names_for_site(cookies, site):
    names = []
    for website in cookies:
        if website == site:
            for cnames in cookies[website]:
                names.append(cnames)
    return names







    
