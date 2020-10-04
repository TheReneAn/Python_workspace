''' Way 1 '''
import travel.thailand

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

''' Way 2 '''
from travel.thailand import ThailandPackage

trip_to = ThailandPackage()
trip_to.detail()

''' Way 3 '''
from travel import vietnam

trip_to = vietnam.VietnamPackage()
trip_to.detail()


