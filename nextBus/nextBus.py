import xml.etree.ElementTree as ET
from collections import defaultdict


def intervalFormat(tmpTime): # seconds past midnight in local time?
    seconds = tmpTime % 60
    tmpTime -= seconds
    minutes = tmpTime / (60 * 60)
    tmpTime -= minutes * 60
    hours = tmpTime / (60 * 60)
    return("%02d:%02d:%02d" % (hours, minutes, seconds))

def nextbusToGTFS(filename):
    "turns a nextbus routeconfig into a GTFS csv list of stops"
    x = ET.iterparse(filename, ['start'])
    
    stopd={} # a dictionary of all the stops
    for i in x:
        
        
        if i[1].tag == 'stop':
            stopId = i[1].get('stopId', None)
            if stopId != None:
                try:
                    stopd[stopId]  = {
                        'title': i[1].get('title', None),
                        'lat' :  i[1].attrib['lat'],
                        'lon' : i[1].attrib['lon'] 
                        }
                except KeyError:
                    continue
            

    for x in sorted(stopd.keys()):
        print(x, stopd[x])





def print_all_stops():
    """prints a sorted list of stops"""
    x = ET.iterparse("routeconfig.xml", ['start'])
    #tagcounter = defaultdict(lambda :0)
    stopd={}
    for i in x:
        #tagcounter[i[1].tag] +=1
        stopId=i[1].get('stopId', None)
        if i[1].tag == 'stop' and  stopId != None:
            stopd[stopId] = i[1].get('title', None)
    #for k,v in stopd.items()    :

    for x in sorted(stopd.keys()):
        print(x, stopd[x])

    


    

def grab_files_from_bus_bucket():
    "downloads fields from przwy-bus, leaving them in the local directory"
    s3 = boto3.resource("s3")
    bucket = s3.Bucket("przwy-bus")
    for key in  bucket.objects.all():
        
        bucket.download_file(key.key, key.key)

def useless_interval_checker():
    x = ET.iterparse("messages.xml", ['start'])
    for i in x:
        if i[1].tag == "interval":

            
            endTime= int(i[1].get('endTime'))
            startTime= int(i[1].get('startTime'))
            print(intervalFormat(startTime), intervalFormat(endTime))
    

def get_messages(filename):
    x = ET.iterparse(filename, ['end'])
    messages = [i[1] for i in x if i[1].tag == "message"]
    return messages

    

def get_text_from_messages_full_response(filename):
    x = ET.iterparse(filename, ['end'])
    messages = [i for i in x if i[1].tag == "text"]
    msgDict = defaultdict(lambda:0)
    for x in messages:
        msgDict[x[1].text] += 1
    for j  in msgDict.keys():
        print ("{:<100.100} {}".format(j, msgDict[j]))


            
            

