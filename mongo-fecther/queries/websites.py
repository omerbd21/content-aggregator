from classes import Website


def website_names():
    websites = list(Website.objects(__raw__={}))
    return [website.name for website in websites]


def get_headlines(website_name):
    # every website has only one entry in DB
    website = list(Website.objects(name=website_name))[0]
    return website.website


def get_last_update_time(website_name):
    # every website has only one entry in DB
    website = list(Website.objects(name=website_name))[0]
    return website.last_update
