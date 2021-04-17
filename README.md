# FiveMpy

A python wrapper in order to interact with FiveM API & FiveM servers

**How-to install :**

```
pip install fivempy
```

**How-to use :**
There is two class : `Server` and `Fivem`

### Server

```python
import fivempy

server = fivempy.Server("ip:port")
#default port is 30120
```

It initialize a Server Class with those attributes:

```
players: [{
        "endpoint"; string,
        "id": int,
        "identifiers": array,
        "name": string,
        "ping": int,
}],
info: {
    "enhancedHostSupport": boolean,
    "icon": string, // Icon of the server (Base64)
    "resources": array, // All started resources
    "server": string, // FXServer's version (string format)
    "vars": { // Some convars defined in server.cfg
        "sv_enhancedHostSupport": boolean,
        "sv_lan": boolean,
        "sv_licenseKeyToken": string,
        "sv_maxClients": int,
        "sv_scriptHookAllowed": boolean,
        "sv_hostname": string,
    },
    "version": int, // FXServer's version (numeric format)
},
dynamic: {
    "clients": int, // number of online player
    "gametype": string,
    "hostname": string,
    "iv": string, // FXServer's version (string format)
    "mapname": string,
    "sv_maxclients": string // number of maximum players
},
ip : string, // server's ip:port
player_count: int, // number of online players
player_max: int, // number of maximum players
player_list: list // list of online players
```

### Fivem

```python
import fivempy

fivem = fivempy.Fivem()
```

It initialize a Fivem Class with those attributes:

```
status: {
    "indicator": string, // "none", "minor", "major", or "critical"
    "description": string // "All Systems Operational", "Partial System Outage", or "Major Service Outage"
},
forum_status, policy_status, cnl_status, keymaster_status, serverlist_status, runtime_status: {
    "name": string, // names of different components
    "status": string, // operational, degraded_performance, partial_outage, or major_outage
    "description": string, // description of the service
}
```
