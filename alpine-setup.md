## Get Alpine ready for Ansible

### Enable root ssh login

in ``/etc/ssh/sshd_config``
    
    PermitRootLogin yes

### Post-install packages

    apk update &&
    apk add doas && 
    apk add python3 &&
    apk add nano


### Create non-root user and give root privileges

    adduser ccalifice &&
    adduser ccalifice wheel

If not present alreadym, add the following line to ``/etc/doas.d/doas.conf``

    permit persist :wheel


## Networking

### Static IP

contents of ``/etc/network/interfaces``

    
    auto lo
    iface lo inet loopback

    auto eth0
    iface eth0 inet static
            address 192.168.1.201
            netmask 255.255.255.0
            gateway 192.168.1.254


### DNS

Usually done through ``alpine-setup``, but in case it's needed:

in ``/etc/resolv.conf`` add

    nameserver 192.168.1.199

### Restart networking

    rc-service networking restart

### Check local ip

    ifconfig


## Settup services

### Docker

First enable the community repo in ``/etc/apk/repositories``

       http://mirror.uepg.br/alpine/v3.18/community

### Then install docker and docker compose

    doas apk update &&
    doas apk add docker &&
    doas apk add docker-cli-compose

### Add current user to docker group

    doas addgroup ccalifice docker

### Start docker on boot and start it

    doas rc-update add docker default &&
    doas service docker start


## Mount disks

### Pass the disk to VM

In PVE, Get the disk id and pass it to the VM

    ls -l /dev/disk/by-id/
    qm set <VM_ID> --scsi1 /dev/disk/by-id/<DISK_ID>
    qm reboot <VM_ID>

In Alpine, install ``lsblk`` and get the new disk

    doas apk add lsblk &&
    lsblk -f

Create mount points and give user permissions

    doas mkdir /mnt/hdd_1tb &&
    doas chown ccalifice:ccalifice /mnt/hdd_1tb


Edit ``/etc/fstab`` to add

    /dev/sdb /mnt/hdd_1tb ext4 rw,user,exec 0 1


Mount the disk and change ownership

    doas mount -a &&
    doas chown ccalifice:ccalifice /mnt/hdd_1tb


Create folder structure if id doesn't exist

    mkdir -p \
    /mnt/hdd_1tb/data/media/movies \
    /mnt/hdd_1tb/data/media/tv \
    /mnt/hdd_1tb/data/media/music \
    /mnt/hdd_1tb/data/torrents/movies \
    /mnt/hdd_1tb/data/torrents/tv \
    /mnt/hdd_1tb/data/torrents/music \
    /mnt/hdd_1tb/data/torrents/games


### Mount NAS

Create mount point

    doas mkdir -p /mnt/servarr &&
    doas chown ccalifice:ccalifice /mnt/servarr

Add to ``/etc/fstab``

    //192.168.1.65/servarr /mnt/servarr cifs vers=3,user=servarr,password=<password>,uid=ccalifice,gid=ccalifice 0 0

Install ``cifs-utils`` and mount with

    doas apk add cifs-utils &&
    doas mount -a