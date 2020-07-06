### 1.重启243后
```
root@mash:/home/mash/qyq# hyctl port-list
Authentication required
```
原因：
```
/etc/neutron/neutron.conf的keystone模块被修改，导致无法正常认证
```

### 2.如何看neutron资源信息
```
cd /home/mash/qyq
source admin-openrc.sh
hyctl floatingip-list
```
### 3.浮动ip出问题？
在node1上
```
service neutron-l3-agent restart
```
重启后一般都能解决

如果还是不行的话，进入node1上对应router的network namespace， 查看iptables的nat规则，比如
```
ip netn exec qrouter-bb3face6 iptables -t nat -L
```
查看防火墙规则
```
ip netn exec qrouter-bb3face6 iptables -t filter  -L
```

直接在路由的network namespace里面ping 对应的ip
```
ip netn exec qrouter-bb3face6 ping 192.168.1.6
```
如果ping不通可能是网关端口的tag和容器端口的tag不一样
```
ovs-vsctl show
```
例如
```
    Bridge br-int
        fail_mode: secure
        Port "vqr-8ac32bf7"
            tag: 7
            Interface "vqr-8ac32bf7"
        Port "vqr-9320c471"
            tag: 2 // 网关端口 tag=2
            Interface "vqr-9320c471"
        Port "vqr-30385e0f"
            tag: 4
            Interface "vqr-30385e0f"
        Port "vqr-285b67e0"
            tag: 3
            Interface "vqr-285b67e0"
        Port "tape4b98"
            tag: 5
            Interface "tape4b98"
        Port "vqr-a6d79c40"
            tag: 1
            Interface "vqr-a6d79c40"
        Port "vqr-1ee1d7ee"
            tag: 5
            Interface "vqr-1ee1d7ee"
        Port br-int
            Interface br-int
                type: internal
        Port patch-int-tap
            Interface patch-int-tap
                type: patch
                options: {peer=patch-tap-int}
        Port "tap95efb"
            tag: 2 // tag = 2
            Interface "tap95efb"
        Port "vqr-38576899"
            tag: 6
            Interface "vqr-38576899"
        Port "tap838be"
            tag: 2 // tag = 2
            Interface "tap838be"
        Port patch-tun
            Interface patch-tun
                type: patch
                options: {peer=patch-int}

```
