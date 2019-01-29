# Practice with Python Multithreading


### Thread Module
`import thread` or `import _thread`
* Although it is very effective for low-level threading, but the thread module is very limited compared to the newer threading module.

### Threading Module
`import threading`
* The `threading` module exposes all the methods of the thread module and provides some additional methods

* run() − The run() method is the entry point for a thread.

* start() − The start() method starts a thread by calling the run method.

* join([time]) − The join() waits for threads to terminate.

* isAlive() − The isAlive() method checks whether a thread is still executing.

* getName() − The getName() method returns the name of a thread.

* setName() − The setName() method sets the name of a thread.