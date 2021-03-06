Python script to analyze and plot multiple algorithms.

This was developed in: 

PyCharm 2020.3.3 (Professional Edition)
Build #PY-203.7148.72
Runtime version: 11.0.9.1+11-b1145.77 aarch64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.

with Python 3.9 using matplotlib on an M1 Mac Mini running macOS 11.2.

I noticed that trying to run this on my Macbook Pro using the Community Edition of Pycharm resulted in 
needing to close each graph generated by matplotlib before the program continues.  Not sure if this was just a setting I had wrong on 
that particular machine, but it runs on my Mac Mini and Windows 10 machines with Python 3.9 with normal behavior and all 
graphs are able to be subsequently generated without closing each to continue. It's worth noting that the edition of PyCharm that exhibits normal
behavior in terms of not having to close the graphs to continue is the Professional Edition. 

Everything is contained in main.py. 
Once the program has started, the user is prompted to either enter User Input Mode or Stats Mode.
You must enter the corresponding integer to progress through the menus. Failure to do so will terminate the program.
In Stats Mode, the user can select which graphs they want generated.
The user can simply run main.py to access the program menu. Relevant graphs are sent to the SciView viewer.