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
