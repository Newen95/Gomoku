Gomoku
===

### Launch Liskvork:

```
cd liskvork-0.5.1/
./zig-out/bin/liskvork
```

*> change parameters in "config.ini"*

### Make a Log file of Liskvork Process

```
cd liskvork-0.5.1/
strace ./zig-out/bin/liskvork > log.txt 2>&1
```