cookies = {("ucsd.edu", "pwd"): "abc",
           ("python-news.com", "font-pref"): "courier",
           ("python-news.com", "session"): "XGKE"
           }

def set_cookie(cookies, site, name, value):
    cookies[(site, name)] = value

def get_cookie(cookies, site, name, default):
    if (site, name) not in cookies:
        return default
    return cookies[(site, name)]

def get_cookie_names_for_site(cookies, site):
    names = []
    for key in cookies:
        if key[0] == site:
            names.append(key[1])
    return names
