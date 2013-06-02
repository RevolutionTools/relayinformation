
import httplib2

#return False if image url is pointing to no image
def isImageValid(imgURL):
    h = httplib2.Http()
    resp,content = h.request(imgURL,"GET")
    print resp
    del content
    if resp and resp['status'] == '200' or  resp['status'] == '304' and  int(resp['content-length']) >  0:
        return True
    return False
