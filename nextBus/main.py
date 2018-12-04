import nextbus
import downloader
import pdb

msgurl='http://webservices.nextbus.com/service/publicXMLFeed?command=messages&a=unitrans'
agencyurl = 'http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList'
    #downloader.save("http://webservices.nextbus.com/service/publicXMLFeed?command=messages&a=pgc")
if __name__ == "__main__":

    nextbus.nextbusToGTFS("routeconfig.xml")
    

