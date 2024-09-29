# Ohjelmointiprojekti

### db.json
create `db.json` in the project root that has following schema
```json
{
  "host": "127.0.0.1",
  "port": 3306,
  "database": "flight_game",
  "username": string,
  "password": string
}
```

### current state
Flying between airports is working'ish
```
Flying to |EKBI| |Billund Airport| in |Denmark

Fly to |Billund Airport| in |Denmark| distance(you) 0 by selecting (1)
Fly to |Copenhagen Kastrup Airport| in |Denmark| distance(you) 220 by selecting (2)
Fly to |Hamburg Helmut Schmidt Airport| in |Germany| distance(you) 241 by selecting (3)
Fly to |Gothenburg-Landvetter Airport| in |Sweden| distance(you) 287 by selecting (4)
Fly to |Hannover Airport| in |Germany| distance(you) 366 by selecting (5)
Fly to |Stavanger Airport, Sola| in |Norway| distance(you) 408 by selecting (6)
Fly to |Berlin Brandenburg Airport| in |Germany| distance(you) 471 by selecting (7)
Fly to |Amsterdam Airport Schiphol| in |Netherlands| distance(you) 477 by selecting (8)
Selection: 7

Flying to |EDDB| |Berlin Brandenburg Airport| in |Germany

Fly to |Berlin Brandenburg Airport| in |Germany| distance(you) 0 by selecting (1)
Fly to |Leipzig/Halle Airport| in |Germany| distance(you) 134 by selecting (2)
Fly to |Václav Havel Airport Prague| in |Czech Republic| distance(you) 256 by selecting (3)
Fly to |Hannover Airport| in |Germany| distance(you) 259 by selecting (4)
Fly to |Hamburg Helmut Schmidt Airport| in |Germany| distance(you) 274 by selecting (5)
Fly to |Nuremberg Airport| in |Germany| distance(you) 360 by selecting (6)
Fly to |Copenhagen Kastrup Airport| in |Denmark| distance(you) 367 by selecting (7)
Fly to |Gda?sk Lech Wa??sa Airport| in |Poland| distance(you) 399 by selecting (8)
Fly to |Frankfurt am Main Airport| in |Germany| distance(you) 429 by selecting (9)
Fly to |Munich Airport| in |Germany| distance(you) 461 by selecting (10)
Fly to |Cologne Bonn Airport| in |Germany| distance(you) 468 by selecting (11)
Fly to |Billund Airport| in |Denmark| distance(you) 471 by selecting (12)
Fly to |Düsseldorf Airport| in |Germany| distance(you) 477 by selecting (13)
Selection:
```