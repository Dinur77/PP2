import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
x={
    "totalCount": "400",
    "imdata": [
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/33",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/34]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/34",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/35]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/35",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/36]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/36",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/1]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/1",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2017-06-30T06:35:49.634-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "enabled",
                    "trunkLog": "default",
                    "usage": "fabric"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/2]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/2",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2017-06-30T06:36:08.122-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "enabled",
                    "trunkLog": "default",
                    "usage": "fabric"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/3]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/3",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2017-06-30T06:36:10.100-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "enabled",
                    "trunkLog": "default",
                    "usage": "fabric"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/4]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/4",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2017-06-30T06:36:03.247-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "enabled",
                    "trunkLog": "default",
                    "usage": "fabric"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/5]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/5",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/6]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/6",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/7]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/7",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/8]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/8",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/9]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/9",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/10]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/10",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/11]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/11",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/12]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/12",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/13]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/13",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/14]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/14",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        }
    ]
}
for item in x["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    descr=item["l1PhysIf"]["attributes"]["descr"]
    speed=item["l1PhysIf"]["attributes"]["speed"]
    mtu=item["l1PhysIf"]["attributes"]["mtu"]
    print(dn,"                           ",descr,speed,mtu)