###########
# Imports #
###########

import urllib2
from bs4 import BeautifulSoup
import re
import os


###########
# Library #
###########

# gets web page and reads the data
def get_page_data(url):
    page = urllib2.urlopen(url)
    contents = page.read()
    return contents


# scrapes the data from the website, and searches for <tr> tags
def get_soup_body(contents):
    soup = BeautifulSoup(contents, "html.parser")
    body = soup.findAll("tr")
    return body


# opens a file and writes get_soup_body() with extract_data() filters
def add_cleaned_courses_body(body, path):
    with open(path, 'w') as fhandle:
        for item in extract_data(body):
            fhandle.write(str(item))


# filters what gets written to file - cleans the data into proper format
def extract_data(body):
    for i in body:
        a = re.sub('<[^<]+?>', '', str(i))
        b = re.sub('view\xc2\xa0book\xc2\xa0info', '', str(a))
        c = re.sub('key', '', str(b))
        d = re.sub('Key', '', str(c))
        e = re.sub('\xc2', ' ', str(d))
        f = re.sub('\xa0', '', str(e))
        yield f


##########
# Script #
##########

def main():
    school_name = 'York College of Pennsylvania'
    file_name = school_name.replace(' ', '_')
    new_file_location = os.path.join('/Users/.../data_mining',
                                     '%s.txt' % file_name)
    url = r'http://ycpweb.ycp.edu/schedule-of-classes/index.html?term=201610&dept=CS_12&stype=A&ord=1&lev=0'
    funnel = reduce(lambda x, y: y(x), [get_page_data, get_soup_body], url)
    add_cleaned_courses_body(funnel, new_file_location)


if __name__ == '__main__':
    main()
