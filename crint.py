import yaml
import pyeapi
file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)
def create_vlans():
    for switch in vlan_dict['switches']:
     print(f"Connecting to {switch}")
     connect = pyeapi.connect_to(switch)
     vlan_api = connect.api('vlans')
     for vlan in vlan_dict['vlans']:
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Adding VLAN {vlan_id} to {switch}")
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id, vlan_name)
        print(vlan_api.get(vlan_id))



def create_int_vlans():
    for switch in vlan_dict['switches']:
        print(f"Connecting to {switch}")
        node  = pyeapi.connect_to(switch)
        vlan_api = node.api('vlans')
        interface_api = node.api('ipinterfaces')
        configured_vlans = vlan_api.getall()
        # print (configured_vlans)
        for configured_vlan in configured_vlans: 
            commands = ["interface vlan {}".format(configured_vlan), "ip address 192.168.{}.254/24" .format(configured_vlan), "no shutdown"]
            config = node.config(commands)
            intname = ("Vlan{}".format(configured_vlan))
            print (interface_api.get(intname))


          
create_vlans()
create_int_vlans()