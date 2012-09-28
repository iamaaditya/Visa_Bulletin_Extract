##########################
# Program	:	Fetch the Visa Bulletin information for all past months
# Author	:	Aaditya Prakash (prakash@aaditya.info)
# Date		:	05 - Aug - 2012
#########################
import urllib2


rr = urllib2.urlopen('http://www.travel.state.gov/visa/bulletin/bulletin_1770.html')

html = rr.read()

pos = html.find('bulletin_')

fourll = []
resul = []
while(pos != -1):
    fourll.append(html[(pos+len('bulletin_')):(pos+len('bulletin_')+4)])
    ##fourll[0] = 1360
    pos = html.find('bulletin_', pos+1)

print(fourll)



for fourlink in fourll:

    response = urllib2.urlopen('http://www.travel.state.gov/visa/bulletin/bulletin_'+fourlink+'.html')
    ##response = urllib2.urlopen('http://www.travel.state.gov/visa/bulletin/bulletin_5572.html')
    #print(response.geturl())
    html = response.read()

    ## if looking for other category then change this accordingly (you will have to see some of the sample Bulletin Page for perfect keyword
	valdv=html.find('(DV)')

	## this can be changed to some other REGION
    valasia = html.find('ASIA',valdv)
    valtd = html.find('<td', valasia)
    valtdcl=html.find('</',valtd)
    if(valdv == -1 or valasia == -1 or valtd == -1 or valtdcl == -1):
        continue
    valtitle = html.find('<title>')
    valtitlecl = html.find('</title>')
    if(valdv != -1):
        resul.append((html[(valtitle+7):valtitlecl] + '\t'+ html[(valtd+4):valtdcl]))
        print((html[(valtitle+7):valtitlecl] + '\t'+ html[(valtd+4):valtdcl]))

#print(resul)
