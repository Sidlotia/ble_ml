import MarkovChain
import numpy as np



import argparse
import dbus
import dbus.exceptions
import dbus.mainloop.glib
import dbus.service
import time
import threading

try:
    from gi.repository import GObject  # python3
except ImportError:
    import gobject as GObject  # python2

sample_index=0


############BLE part starts here
############BLE part starts here
############BLE part starts here
############BLE part starts here
############BLE part starts here
############BLE part starts here
############BLE part starts here
############BLE part starts here
############BLE part starts here
############BLE part starts here

mainloop = None

BLUEZ_SERVICE_NAME = 'org.bluez'
LE_ADVERTISING_MANAGER_IFACE = 'org.bluez.LEAdvertisingManager1'
DBUS_OM_IFACE = 'org.freedesktop.DBus.ObjectManager'
DBUS_PROP_IFACE = 'org.freedesktop.DBus.Properties'

LE_ADVERTISEMENT_IFACE = 'org.bluez.LEAdvertisement1'


class InvalidArgsException(dbus.exceptions.DBusException):
    _dbus_error_name = 'org.freedesktop.DBus.Error.InvalidArgs'


class NotSupportedException(dbus.exceptions.DBusException):
    _dbus_error_name = 'org.bluez.Error.NotSupported'


class NotPermittedException(dbus.exceptions.DBusException):
    _dbus_error_name = 'org.bluez.Error.NotPermitted'


class InvalidValueLengthException(dbus.exceptions.DBusException):
    _dbus_error_name = 'org.bluez.Error.InvalidValueLength'


class FailedException(dbus.exceptions.DBusException):
    _dbus_error_name = 'org.bluez.Error.Failed'


class Advertisement(dbus.service.Object):
    PATH_BASE = '/org/bluez/example/advertisement'

    def __init__(self, bus, index, advertising_type):
        self.path = self.PATH_BASE + str(index)
        self.bus = bus
        self.ad_type = advertising_type
        self.service_uuids = None
        self.manufacturer_data = None
        self.solicit_uuids = None
        self.service_data = None
        self.local_name = None
        self.include_tx_power = None
        self.data = None
        dbus.service.Object.__init__(self, bus, self.path)

    def get_properties(self):
        properties = dict()
        properties['Type'] = self.ad_type
        if self.service_uuids is not None:
            properties['ServiceUUIDs'] = dbus.Array(self.service_uuids,
                                                    signature='s')
        if self.solicit_uuids is not None:
            properties['SolicitUUIDs'] = dbus.Array(self.solicit_uuids,
                                                    signature='s')
        if self.manufacturer_data is not None:
            properties['ManufacturerData'] = dbus.Dictionary(
                self.manufacturer_data, signature='qv')
        if self.service_data is not None:
            properties['ServiceData'] = dbus.Dictionary(self.service_data,
                                                        signature='sv')
        if self.local_name is not None:
            properties['LocalName'] = dbus.String(self.local_name)
        if self.include_tx_power is not None:
            properties['IncludeTxPower'] = dbus.Boolean(self.include_tx_power)

        if self.data is not None:
            properties['Data'] = dbus.Dictionary(
                self.data, signature='yv')
        return {LE_ADVERTISEMENT_IFACE: properties}

    def get_path(self):
        return dbus.ObjectPath(self.path)

    def add_service_uuid(self, uuid):
        if not self.service_uuids:
            self.service_uuids = []
        self.service_uuids.append(uuid)

    def add_solicit_uuid(self, uuid):
        if not self.solicit_uuids:
            self.solicit_uuids = []
        self.solicit_uuids.append(uuid)

    def add_manufacturer_data(self, manuf_code, data):
        if not self.manufacturer_data:
            print('No manufacturer data found...')
            self.manufacturer_data = dbus.Dictionary({}, signature='qv')
        self.manufacturer_data[manuf_code] = dbus.Array(data, signature='y')

    def add_service_data(self, uuid, data):
        if not self.service_data:
            #print('No service data found...')
            self.service_data = dbus.Dictionary({}, signature='sv')
        self.service_data[uuid] = dbus.Array(data, signature='y')

    def add_local_name(self, name):
        if not self.local_name:
            self.local_name = ""
        self.local_name = dbus.String(name)

    def add_data(self, ad_type, data):
        print(data)
        if not self.data:
            #print('No self data found...')
            self.data = dbus.Dictionary({}, signature='yv')
        self.data[ad_type] = dbus.Array(data, signature='y')
        #print(dbus.Array(data, signature='y'))
        #print(ad_type)
        #print(dbus.Dictionary({}, signature='yv'))
        #print(self.data[ad_type])

    @dbus.service.method(DBUS_PROP_IFACE,
                         in_signature='s',
                         out_signature='a{sv}')
    def GetAll(self, interface):
        #print('GetAll')
        if interface != LE_ADVERTISEMENT_IFACE:
            raise InvalidArgsException()
        #print('returning props')
        return self.get_properties()[LE_ADVERTISEMENT_IFACE]

    @dbus.service.method(LE_ADVERTISEMENT_IFACE,
                         in_signature='',
                         out_signature='')
    def Release(self):
        print('%s: Released!' % self.path)


class TestAdvertisement(Advertisement):

    def __init__(self, bus, index):
        global sample_index
        global x
        Advertisement.__init__(self, bus, index, 'peripheral')
##        Data = imubus.read_i2c_block_data(MPU9250_I2C_ADDR,SENSOR_BASE_ADDR)
##        ax = Data[0]<<8 | Data[1]
##        ay = Data[2]<<8 | Data[3]
##        az = Data[4]<<8 | Data[5]
##        print(ax)
##        list = []
##        list.append((Data[0]))
##        list.append((Data[1]))
##        list.append((Data[2]))
##        list.append((Data[3]))
##        list.append((Data[4]))
##        list.append((Data[5]))
##        print(list)


        
##        h = hex(331122313).split('x')[-1]       
##        list=[]
##        list.append(h[0])
##        list.append(h[1])
##        list.append(h[2])
##        list.append(h[3])
##        list.append(h[4])
##        list.append(h[5])
##        
##        print('hex', list)
##        self.add_service_uuid('183D')
##        self.add_service_data('183D', list)

#######################
        #print('data',x[sample_index])
##        h = hex(x[0]).split('x')[-1]
        h = x[sample_index]
        sample_index=sample_index+1
        #print(h[0],h[1],h[2])
        #print(sample_index)
        list=[]
        list.append(h[0])
        list.append(h[1])
        list.append(h[2])

        
               
##        self.add_service_uuid('180D')
##        self.add_service_uuid('180F')
##        self.add_manufacturer_data(0x44, list)
        self.add_service_uuid('183D')
        self.add_service_data('183D', list)
##        self.add_local_name('TestAdvertisement')
##        self.include_tx_power = True
##        self.add_data(0x3d, list)

def register_ad_cb():
    a=1
    #print('Advertisement registered')

def register_ad_error_cb(error):
    print('Failed to register advertisement: ' + str(error))
    mainloop.quit()

def find_adapter(bus):
    remote_om = dbus.Interface(bus.get_object(BLUEZ_SERVICE_NAME, '/'),
                               DBUS_OM_IFACE)
    objects = remote_om.GetManagedObjects()

    for o, props in objects.items():
        if LE_ADVERTISING_MANAGER_IFACE in props:
            return o

    return None


def shutdown(timeout):
    print('Advertising for {} seconds...'.format(timeout))
    time.sleep(timeout)
    mainloop.quit()

######################

def main(timeout=0):
    global mainloop

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()

    adapter = find_adapter(bus)
    if not adapter:
        print('LEAdvertisingManager1 interface not found')
        return

    adapter_props = dbus.Interface(bus.get_object(BLUEZ_SERVICE_NAME, adapter),
                                   "org.freedesktop.DBus.Properties")

    adapter_props.Set("org.bluez.Adapter1", "Powered", dbus.Boolean(1))

    ad_manager = dbus.Interface(bus.get_object(BLUEZ_SERVICE_NAME, adapter),
                                LE_ADVERTISING_MANAGER_IFACE)


    timeout=0.1

    for index1 in range(1,2000):
        test_advertisement = TestAdvertisement(bus, 0)
        mainloop = GObject.MainLoop()
        ad_manager.RegisterAdvertisement(test_advertisement.get_path(), {},
                                     reply_handler=register_ad_cb,
                                     error_handler=register_ad_error_cb)
        if timeout > 0:
            threading.Thread(target=shutdown, args=(timeout,)).start()
        else:
            print('Advertising forever...')
        mainloop.run()  # blocks until mainloop.quit() is called
        ad_manager.UnregisterAdvertisement(test_advertisement)
        #print('Advertisement unregistered')
        dbus.service.Object.remove_from_connection(test_advertisement)
        time.sleep(0.1)

#############################################
class MarkovChain(object):
    def __init__(self, transition_prob, emission_prob):
        """
        Initialize the MarkovChain instance.
 
        Parameters
        ----------
        transition_prob: dict
            A dict object representing the transition 
            probabilities in Markov Chain. 
            Should be of the form: 
                {'state1': {'state1': 0.1, 'state2': 0.4}, 
                 'state2': {...}}
        """
        self.transition_prob = transition_prob
        self.states = list(transition_prob.keys())
        self.emission_prob = emission_prob
        self.emittedstates = list(emission_prob.keys())
        
    def next_state(self, current_state):
        """
        Returns the state of the random variable at the next time 
        instance.
 
        Parameters
        ----------
        current_state: str
            The current state of the system.
        """
        return np.random.choice(
            self.states, 
            p=[self.transition_prob[current_state][next_state] 
               for next_state in self.states]
        )

    def next_emitted_state(self, current_state):
        """
        Returns the state of the random variable at the next time 
        instance.
 
        Parameters
        ----------
        current_state: str
            The current state of the system.
        """
        return np.random.choice(
            self.emittedstates, 
            p=[self.emission_prob[emitted_state][current_state] 
               for emitted_state in self.emittedstates]
        )
 
    def generate_states(self, current_state, no=10):
        """
        Generates the next states of the system.
 
        Parameters
        ----------
        current_state: str
            The state of the current random variable.
 
        no: int
            The number of future states to generate.
        """
        future_states = []
        emitted_states=[]
        x = []
        for i in range(no):
            next_state = self.next_state(current_state)
            emitted_states.append(self.next_emitted_state(next_state))
            future_states.append(next_state)
            current_state = next_state
        #return future_states
            
        #return [emitted_states, future_states]
        #print (emitted_states)
        x = emitted_states
        return x
    
    


A_matrix = {'NH': {'NH': 0.5, 'Heat': 0.5},
 'Heat': {'NH': 0.5, 'Heat': 0.5}
}


B = { '0.1': {'NH': 0.2, 'Heat':0.0},
      '0.2': {'NH': 0.2, 'Heat':0.0},
      '0.3': {'NH': 0.2, 'Heat':0.0},
      '0.4': {'NH': 0.2, 'Heat':0.0},
      '0.5': {'NH': 0.2, 'Heat':0.0},
      '0.6': {'NH': 0.0, 'Heat':0.2},
      '0.7': {'NH': 0.0, 'Heat':0.2},
      '0.8': {'NH': 0.0, 'Heat':0.2},
      '0.9': {'NH': 0.0, 'Heat':0.2},
      '1.0': {'NH': 0.0, 'Heat':0.2}
      }

B = { '0.1': {'NH': 0.9, 'Heat':0.1},
      '0.2': {'NH': 0.1, 'Heat':0.9}
      }

weather_chain = MarkovChain(transition_prob= A_matrix, emission_prob=B )

x = []
x= weather_chain.generate_states(current_state='NH', no=200)
#print(x)

######################################


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', default=0.8, type=int, help="advertise " +
                        "for this many seconds then stop, 0=run forever " +
                        "(default: 0)")
    args = parser.parse_args()

    main(args.timeout)

#####################################

