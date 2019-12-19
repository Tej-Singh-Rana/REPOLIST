import os

print('''
Enter the keyword for following process : 
-> Press 1 Check details of running state.
-> Press 2 Check details of all machine.
-> Press 3 To shutdown your machine.
-> Press 4 Create your own image.
-> Press 5 Create your Instance.
-> Press 6 
->
->''')
press = int(input("Enter your key : "))
if press == 1:
    os.system('virsh list --state-running')
elif press == 2:
    os.system('virsh list --all')
elif press == 3:
    machine=input("Enter machine name to shutdown : ")
    os.system('virsh shutdown {}'.format(machine))
elif press == 4:
    name=input('Enter your image name : ')
    os.system('qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhvmdnd.qcow2 /var/lib/libvirt/images/{}.qcow2'.format(name))
elif press == 5:
    ID=input("Enter your machine name : ")
    ram=int(input("Enter ram size : "))
    vcpu=int(input("Enter cpu count : "))
    name=input("Enter your created image name : ")
    os.system('virt-install --name {} --ram {}  --vcpu {} --disk path=/var/lib/libvirt/images/{}.qcow2  --noautoconsole --import'.format(ID,ram,vcpu,name))
