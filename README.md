# Gunicorn benchmark
## Benchmarks

### Benchmark #1
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


### Benchmark #2
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

### Benchmark #3
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

### Benchmark #4
- __request_time__: 1 second
- __worker_count__: 9
- __worker_class__: gevent
- __concurrency__: 100
- __duration__: 1 minute


```
Lifting the server siege...
Transactions:                     5900 hits
Availability:                   100.00 %
Elapsed time:                    59.48 secs
Data transferred:         0.08 MB
Response time:                    1.00 secs
Transaction rate:        99.19 trans/sec
Throughput:                       0.00 MB/sec
Concurrency:                     99.65
Successful transactions:        5900
Failed transactions:                 0
Longest transaction:              1.06
Shortest transaction:             1.00
```

### Benchmark #5
- __request_time__: `random.random() * 60`
- __worker_count__: 9
- __worker_class__: gevent
- __concurrency__: 100
- __duration__: 1 minute


```
Lifting the server siege...
Transactions:                      168 hits
Availability:                   100.00 %
Elapsed time:                    59.56 secs
Data transferred:         0.00 MB
Response time:                   23.78 secs
Transaction rate:         2.82 trans/sec
Throughput:                       0.00 MB/sec
Concurrency:                     67.07
Successful transactions:         168
Failed transactions:                 0
Longest transaction:             59.52
Shortest transaction:             0.11
```

### Benchmark #6
- __request_time__: `random.random() * 60`
- __worker_count__: 2
- __worker_class__: gevent
- __concurrency__: 100
- __duration__: 1 minute

```
Lifting the server siege...
Transactions:                      167 hits
Availability:                   100.00 %
Elapsed time:                    59.86 secs
Data transferred:         0.00 MB
Response time:                   23.63 secs
Transaction rate:         2.79 trans/sec
Throughput:                       0.00 MB/sec
Concurrency:                     65.92
Successful transactions:         167
Failed transactions:                 0
Longest transaction:             59.05
Shortest transaction:             0.04
```

## Explanation

First read the terminal output and note that I ran siege with a concurrency of 10, a duration of 1 minute and in benchmark mode so that there is zero (or as minimal as possible) delay between requests.

```
New configuration template added to /root/.siege
Run siege -C to view the current settings in that file
** SIEGE 4.0.4
** Preparing 10 concurrent users for battle.
The server is now under siege...
siege_1     |
Lifting the server siege...
Transactions:                       18 hits
Availability:                   100.00 %
Elapsed time:                    59.19 secs
Data transferred:         0.00 MB
Response time:                   23.71 secs
Transaction rate:         0.30 trans/sec
Throughput:                       0.00 MB/sec
Concurrency:                      7.21
Successful transactions:          18
Failed transactions:                 0
Longest transaction:             54.30
Shortest transaction:             2.95
siege_1     |
HTTP/1.1 200     2.95 secs:      14 bytes ==> GET  /
HTTP/1.1 200     3.00 secs:      14 bytes ==> GET  /
HTTP/1.1 200     9.36 secs:      14 bytes ==> GET  /
HTTP/1.1 200    12.48 secs:      14 bytes ==> GET  /
HTTP/1.1 200    13.33 secs:      14 bytes ==> GET  /
HTTP/1.1 200    24.32 secs:      14 bytes ==> GET  /
HTTP/1.1 200    26.96 secs:      14 bytes ==> GET  /
HTTP/1.1 200    27.63 secs:      14 bytes ==> GET  /
HTTP/1.1 200    35.07 secs:      14 bytes ==> GET  /
HTTP/1.1 200     8.99 secs:      14 bytes ==> GET  /
HTTP/1.1 200    23.78 secs:      14 bytes ==> GET  /
HTTP/1.1 200    25.36 secs:      14 bytes ==> GET  /
HTTP/1.1 200    42.44 secs:      14 bytes ==> GET  /
HTTP/1.1 200    22.10 secs:      14 bytes ==> GET  /
HTTP/1.1 200    49.21 secs:      14 bytes ==> GET  /
HTTP/1.1 200    11.19 secs:      14 bytes ==> GET  /
HTTP/1.1 200    54.30 secs:      14 bytes ==> GET  /
HTTP/1.1 200    34.38 secs:      14 bytes ==> GET  /
python-load_siege_1 exited with code 0
```

You see that in one minute time with a concurrency of 10, only 18 requests are done.
Because our "app" randomly takes between 0 and 60 seconds, it can be explained as follows:
- the pseudo random generator ideally behaves like a uniform distribution U(0,60)
- a uniform dist. has a mean of `1/2 (0+60) = 30`
- 10 clients (concurrently), on average, will wait 30 seconds. after that they can fire another request
- so the transaction count can be predicted and explained by: `concurrency * (60 seconds / mean_unif(0,60))` which in this case is `10 * (60 / 30) = 10 * 2 = 20` which roughly equals 18 for this particular benchmark.

This also explains the 5900 for benchmark number 4:
- concurrency: 100
- benchmark duration: 60 seconds
- request duration: 1 second

In general:

`concurrency * (benchmark_duration / mean_request_time)`
`100 * (60 sec / 1 sec)` = 6000

which is off by 100 hits, but this can easily be explained by looking at siege's startup overhead
and the fact that is runs for a little less that 60 seconds.
