Documentaion of Bugs found
1. snippets/__init__.py
    - import code in snippets.__init__ had been commented out and so the import were not happening
2. loop.py
    - line 9: initialize dict instead of list
3. loop.py
    - line 11: forgot to add range(10)
    - line 13: NameError cause of using undefined variable
    - line 13: use list.push instead of list.append
4. io.py
    - line 16: list comprehension should use the [] symbols instead of {}
    - line 18: syntax error, there is no such operator as !===, instead use '==' operator
    - line 20: use python inbuilt sum
    - line 29: use python inbuilt sum
    - line 38: use python inbuilt sum
    - line 39: use python inbuilt len
    - line 15, 24, 34
        - use [] to access the values of the dict
    - line 18: should avoid using is operator for immutable types such as strings and numbers, the result is unpredictable, instead use ==
    - line 45: test for division by zero, by checking if sum is zero

5. foobar.py
    - line 8: remove default list argument and initialize it inside the function (explanation below)
    
    Please note: Any expressions in default arguments are always calculated when the function is defined and not when it is called. So when function is called the first time the 'bar' list is created, any subsequntial calls will still use the same list. To avoid this just define bar inside the function and not as a default argument. 
    
