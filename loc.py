import reverse_geocoder as rg 
import pprint 
  
def reverseGeocode(coordinates):
    name = rg.search(coordinates)[0]
    return name
 
  
# Driver function 
if __name__=="__main__": 
      
    # Coorinates tuple.Can contain more than one pair. 
    coordinates =(28.7041,77.1025), (31.76, 35.21)
    a = reverseGeocode(coordinates)
    print('hello')
    print(a)
    '''
    {"lat":28.7041,"long":77.1025}
    '''