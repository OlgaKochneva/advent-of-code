# Solutions not worth their own script file
## Task 4 
Used brute force, iterating through the numbers `n` until the valid md5 was found.
```python
md5((input + str(n)).encode()).hexdigest()
```
