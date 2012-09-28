##########################
# Program	:	Fetch the Visa Bulletin information for all the the given month
# Author	:	Aaditya Prakash (prakash@aaditya.info)
# Date		:	05 - Aug - 2012
#########################

## change this hyperlink to the current visa bulletin link
response = urllib2.urlopen('http://www.travel.state.gov/visa/bulletin/bulletin_4576.html')
html = response.read()

valdv=html.find('DIVERSITY IMMIGRANT (DV) CATEGORY')
valasia = html.find('ASIA',valdv)
valtd = html.find('<td>', valasia)
valtdcl=html.find('</td>',valtd)

valtitle = html.find('<title>')
valtitlecl = html.find('</title>')

print(html[(valtitle+7):valtitlecl] + '\t'+ html[(valtd+4):valtdcl])