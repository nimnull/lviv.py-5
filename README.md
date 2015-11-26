# Fork test
```
PID   Command                  USS      PSS      RSS
23088 python fork_test.py     4892    12122    22196  <-- parent process
23089 python fork_test.py      840     7808    15736  <-- child #1
23309 python fork_test.py      796     7788    15740  <-- child #2


28181 vagrant  python fork_test.py                0     4724    15836    29792
# before copy on wright
28182 vagrant  python fork_test.py                0      836    11701    23560
# after copy on wright
28182 vagrant  python fork_test.py                0     8756    15853    23944

# matrix.nbytes - 8000000
(если матрицы не содержат объекты, т.к. не инкрементится refcount при операциях обращения (взятия ссылки))

```

# Serialize test
## converted to array, then serialized
json test1: 16.321614345069975 ms
ujson test1: 2.8908381939399987 ms
msgpack test1: 1.4039006591774523 ms
pickle test1: 1.4961050520651042 ms

## base64 encoded & serialized
json test2: 1.5896962771657854 ms
ujson test2: 1.910914566833526 ms
msgpack test2: 1.2236832270864397 ms
pickle test2: 1.2019711039029062 ms
