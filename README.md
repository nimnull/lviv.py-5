## Serialize test.
### converted to array, then serialized
```
json test1: 16.321614345069975 ms
ujson test1: 2.8908381939399987 ms
msgpack test1: 1.4039006591774523 ms
pickle test1: 1.4961050520651042 ms
```

### base64 encoded & serialized
```
json test2: 1.5896962771657854 ms
ujson test2: 1.910914566833526 ms
msgpack test2: 1.2236832270864397 ms
pickle test2: 1.2019711039029062 ms
```

## Communication

    RSS - Resident Set Size. This is the amount of shared memory plus unshared memory used by each process. If any processes share memory, this will over-report the amount of memory actually used, because the same shared memory will be counted more than once - appearing again in each other process that shares the same memory. Thus it is fairly unreliable, especially when high-memory processes have a lot of forks - which is common in a server, with things like Apache or PHP(fastcgi/FPM) processes.

    USS - Unique Set Size. This is the amount of unshared memory unique to that process (think of it as U for unique memory). It does not include shared memory. Thus this will under-report the amount of memory a process uses, but is helpful when you want to ignore shared memory.

    PSS - Proportional Set Size. This is what you want. It adds together the unique memory (USS), along with a proportion of its shared memory divided by the number of other processes sharing that memory. Thus it will give you an accurate representation of how much actual physical memory is being used per process - with shared memory truly represented as shared. Think of the P being for physical memory.


### Fork test
```
PID   Command                  USS      PSS      RSS
23088 python fork_test.py     4892    12122    22196  <-- parent process
23089 python fork_test.py      840     7808    15736  <-- child #1
23309 python fork_test.py      796     7788    15740  <-- child #2


28181 python fork_test.py     4724    15836    29792
28182 python fork_test.py      836    11701    23560  <-- before copy on write
28182 python fork_test.py     8756    15853    23944  <-- after copy on write

# matrix.nbytes - 8000000
(если матрицы не содержат объекты, т.к. не инкрементится refcount при операциях обращения (взятия ссылки))

```

### multiprocessing
```
PID   Command                  USS
20363 python multiproc_test.py 13368    <- keep matrix
# -- child process
20367 python multiproc_test.py 1484     <- no matrix
20367 python multiproc_test.py 10056    <- matrix passed
```

### memory-mapped file
```
16737 vagrant  python mmap_test.py                0    26540    26914    29968  <-- before mmap write
16737 vagrant  python mmap_test.py                0     8096    19782    34200  <-- after mmap write
16795 vagrant  python mmap_test.py                0     5484    16920    29656  <-- child processing
```

## Links:
    * An introduction to parallel programming (http://sebastianraschka.com/Articles/2014_multiprocessing_intro.html)
    * Runtime Memory Measurement (http://elinux.org/Runtime_Memory_Measurement)
    * https://github.com/vmlaker/benchmark-sharedmem
