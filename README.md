## Benchmarks

### 1
- __request_time__: `1 second`
- __worker_count__: 9
- __worker_class__: sync (default)
- __concurrency__: 100
- __duration__: 1 minute

```
Lifting the server siege...
Transactions:                      531 hits
Availability:                   100.00 %
Elapsed time:                    59.83 secs
Data transferred:         0.01 MB
Response time:                   10.20 secs
Transaction rate:         8.88 trans/sec
Throughput:                       0.00 MB/sec
Concurrency:                     90.56
Successful transactions:         531
Failed transactions:                 0
Longest transaction:             12.06
Shortest transaction:             1.02
```


### 2
- __request_time__: `random.random() * 60`
- __worker_count__: 9
- __worker_class__: sync (default)
- __concurrency__: 100
- __duration__: 1 minute

```
Lifting the server siege...
Transactions:                       16 hits
Availability:                    76.19 %
Elapsed time:                    59.81 secs
Data transferred:         0.00 MB
Response time:                   32.47 secs
Transaction rate:         0.27 trans/sec
Throughput:                       0.00 MB/sec
Concurrency:                      8.69
Successful transactions:          16
Failed transactions:                 5
Longest transaction:             58.06
Shortest transaction:             0.00
```

## 3
- __request_time__: 1 second
- __worker_count__: 9
- __worker_class__: eventlet
- __concurrency__: 100
- __duration__: 1 minute


```
Lifting the server siege...
Transactions:                      529 hits
Availability:                    93.63 %
Elapsed time:                    59.24 secs
Data transferred:         0.01 MB
Response time:                    9.24 secs
Transaction rate:         8.93 trans/sec
Throughput:                       0.00 MB/sec
Concurrency:                     82.49
Successful transactions:         529
Failed transactions:                36
Longest transaction:             31.13
Shortest transaction:             1.00
```


