# Chapter 1
## Getting to know asyncio


### What is asyncio?
In a synchronous application, code runs sequentially. The next line of code runs as
soon as the previous one has finished, and only one thing is happening at once. This
model works fine for many, if not most, applications. However, what if one line of code
is especially slow? In that case, all other code after our slow line will be stuck waiting
for that line to complete. These potentially slow lines can block the application from
running any other code. Many of us have seen this before in buggy user interfaces,
where we happily click around until the application freezes, leaving us with a spinner
or an unresponsive user interface.  

While any operation can block an application if it takes long enough, many applications
will block waiting on I/O. I/O refers to a computer’s input and output devices such as a
keyboard, hard drive, and, most commonly, a network card. These operations wait for user
input or retrieve the contents from a web-based API.  


### What is I/O-bound and what is CPU-bound?
CPU-bound operations are typically computations and processing code in the
Python world. An example of this is computing the digits of pi or looping over the
contents of a dictionary, applying business logic. In an I/O-bound operation we spend
most of our time waiting on a network or other I/O device. An example of an I/O-
bound operation would be making a request to a web server or reading a file from our
machine’s hard drive.  

Asynchronous I/O allows us to pause execution of a particular method when we
have an I/O operation; we can run other code while waiting for our initial I/O to
complete in the background. This allows us to execute many I/O operations concurrently,
potentially speeding up our application.  


### Understanding concurrency, parallelism, and multitasking
With concurrency, we have multiple tasks happening at the same time, but only one we’re
actively doing at a given point in time. With parallelism, we have multiple tasks happening 
and are actively doing more than one simultaneously.  

With concurrency, we switch between running two applications. With parallelism, we actively 
run two applications simultaneously.  

Concurrency is about multiple tasks that can happen independently of one another. We can have
concurrency on a CPU with only one core, as the operation will employ preemptive multitasking 
to switch between tasks. Parallelism, however, means that we must be executing two or more
tasks at the same time. On a machine with one core, this is not possible. To make this possible,
we need a CPU with multiple cores that can run two tasks together.  


#### What is multitasking?
Multitasking is everywhere in today’s world. We multitask while making breakfast by
taking a call or answering a text while we wait for water to boil to make tea. We even
multitask while commuting to work, by reading a book while the train takes us to our
stop. Two main kinds of multitasking are discussed in this section: preemptive multitasking
and cooperative multitasking.

##### PREEMPTIVE MULTITASKING:
In this model, we let the operating system decide how to switch between which work is
currently being executed via a process called time slicing. When the operating system
switches between work, we call it preempting.  

##### COOPERATIVE MULTITASKING:
In this model, instead of relying on the operating system to decide when to switch
between which work is currently being executed, we explicitly code points in our
application where we can let other tasks run. The tasks in our application operate in a
model where they cooperate, explicitly saying, “I’m pausing my task for a while; go ahead
and run other tasks.  

##### The benefits of cooperative multitasking:
asyncio uses cooperative multitasking to achieve concurrency. When our application
reaches a point where it could wait a while for a result to come back, we explicitly
mark this in code. This allows other code to run while we wait for the result to come
back in the background. Once the task we marked has completed, we in effect “wake
up” and resume executing the task. This gives us a form of concurrency because we
can have multiple tasks started at the same time but, importantly, not in parallel
because they aren’t executing code simultaneously.  
Cooperative multitasking has benefits over preemptive multitasking. First, cooperative
multitasking is less resource intensive. When an operating system needs to switch
between running a thread or process, it involves a context switch. Context switches are
intensive operations because the operating system must save information about the
running process or thread to be able to reload it.  
A second benefit is granularity. An operating system knows that a thread or task
should be paused based on whichever scheduling algorithm it uses, but that might not
be the best time to pause. With cooperative multitasking, we explicitly mark the areas
that are the best for pausing our tasks. This gives us some efficiency gains in that we
are only switching tasks when we explicitly know it is the right time to do so. Now that
we understand concurrency, parallelism, and multitasking, we’ll use these concepts to
understand how to implement them in Python with threads and processes.  


### Understanding processes, threads, multithreading, and multiprocessing
#### Process:
A process is an application run that has a memory space that other applications cannot
access. An example of creating a Python process would be running a simple “hello world” 
application.  

Multiple processes can run on a single machine. If we are on a machine that has a
CPU with multiple cores, we can execute multiple processes at the same time. If we
are on a CPU with only one core, we can still have multiple applications running
simultaneously, through time slicing. When an operating system uses time slicing, it
will switch between which process is running automatically after some amount of time.
The algorithms that determine when this switching occurs are different, depending
on the operating system.

#### Threads:
Threads can be thought of as lighter-weight processes. In addition, they are the smallest
construct that can be managed by an operating system. They do not have their own
memory as does a process; instead, they share the memory of the process that created
them. Threads are associated with the process that created them. A process will always
have at least one thread associated with it, usually known as the main thread. A process
can also create other threads, which are more commonly known as worker or background
threads. These threads can perform other work concurrently alongside the main thread.  

Multithreading and multiprocessing may seem like magic bullets to enable concurrency with 
Python. However, the power of these concurrency models is hindered by an implementation 
detail of Python—the global interpreter lock.  


### Understanding the global interpreter lock
The global interpreter lock, abbreviated GIL and pronounced gill, is a controversial
topic in the Python community. Briefly, the GIL prevents one Python process from
executing more than one Python bytecode instruction at any given time. This means
that even if we have multiple threads on a machine with multiple cores, a Python
process can have only one thread running Python code at a time. In a world where we
have CPUs with multiple cores, this can pose a significant challenge for Python developers
looking to take advantage of multithreading to improve the performance of their application.  

**Multiprocessing can run multiple bytecode instructions concurrently because each Python 
process has its own GIL.**  

So why does the GIL exist? The answer lies in how memory is managed in CPython. In
CPython, memory is managed primarily by a process known as reference counting. Reference
counting works by keeping track of who currently needs access to a particular
Python object, such as an integer, dictionary, or list.  

The conflict with threads arises in that the implementation in CPython is not thread
safe. When we say CPython is not thread safe, we mean that if two or more threads modify
a shared variable, that variable may end in an unexpected state. This unexpected
state depends on the order in which the threads access the variable, commonly known
as a race condition. Race conditions can arise when two threads need to reference a
Python object at the same time.  

If two threads increment the reference count at one time, we could face a situation where 
one thread causes the reference count to be zero when the object is still in use by the 
other thread. The likely result of this would be an application crash when we try to read 
the potentially deleted memory.  

#### Is the GIL ever released?
The global interpreter lock is released when I/O operations happen. This lets us
employ threads to do concurrent work when it comes to I/O, but not for CPU-bound
Python code itself (there are some notable exceptions that release the GIL for CPU-bound work 
in certain circumstances).  

So how is it that we can release the GIL for I/O but not for CPU-bound operations
The answer lies in the system calls that are made in the background. In the case
of I/O, the low-level system calls are outside of the Python runtime. This allows the
GIL to be released because it is not interacting with Python objects directly.  

#### asyncio and the GIL
asyncio exploits the fact that I/O operations release the GIL to give us concurrency,
even with only one thread. When we utilize asyncio we create objects called coroutines.
A coroutine can be thought of as executing a lightweight thread. Much like we can
have multiple threads running at the same time, each with their own concurrent I/O
operation, we can have many coroutines running alongside one another. While we are
waiting for our I/O-bound coroutines to finish, we can still execute other Python
code, thus, giving us concurrency.  


### How single-threaded concurrency works
We don’t need multiple threads to achieve this kind of concurrency. We can do it all within
the confines of one process and one thread. We do this by exploiting the fact that, at the 
system level, I/O operations can be completed concurrently.  

#### What is a socket?
A socket is a low-level abstraction for sending and receiving data over a network. It is
the basis for how data is transferred to and from servers. Sockets support two main
operations: sending bytes and receiving bytes.  

Sockets are blocking by default. Simply put, this means that when we are waiting for a
server to reply with data, we halt our application or block it until we get data to read.
Thus, our application stops running any other tasks until we get data from the server,
an error happens, or there is a timeout.  

At the operating system level, we don’t need to do this blocking. Sockets can operate
in non-blocking mode. In non-blocking mode, when we write bytes to a socket, we can just
fire and forget the write or read, and our application can go on to perform other tasks.
Later, we can have the operating system tell us that we received bytes and deal with it at
that time. This lets the application do any number of things while we wait for bytes to
come back to us. Instead of blocking and waiting for data to come to us, we become
more reactive, letting the operating system inform us when there is data for us to act on.  

In the background, this is performed by a few different event notification systems,
depending on which operating system we’re running.  

* *kqueue* - FreeBSD and MacOS
* *epoll* - Linux
* *IOCP* - Windows

These systems keep track of our non-blocking sockets and notify us when they are
ready for us to do something with them.  

In asyncio’s model of concurrency, we have only one thread executing Python at any given time.
When we hit an I/O operation, we hand it over to our operating system’s event notification 
system to keep track of it for us. Once we have done this handoff, our Python thread is free 
to keep running other Python code or add more non-blocking sockets for the OS to keep track of 
for us. When our I/O operation finishes, we “wake up” the task that was waiting for the result 
and then proceed to run any other Python code that came after that I/O operation.  


### How an event loop works
An event loop is at the heart of every asyncio application. Event loops are a fairly common
design pattern in many systems and have existed for quite some time.  

In asyncio, the event loop keeps a queue of tasks. Tasks are wrappers around a coroutine.
A coroutine can pause execution when it hits an I/O-bound operation and will let the event 
loop run other tasks that are not waiting for I/O operations to complete.  

When we create an event loop, we create an empty queue of tasks. We can then add
tasks into the queue to be run. Each iteration of the event loop checks for tasks that need
to be run and will run them one at a time until a task hits an I/O operation. At that time
the task will be “paused,” and we instruct our operating system to watch any sockets for
I/O to complete. We then look for the next task to be run. On every iteration of the
event loop, we’ll check to see if any of our I/O has completed; if it has, we’ll “wake up”
any tasks that were paused and let them finish running.  


### Summary
* CPU-bound work is work that primarily utilizes our computer’s processor whereas
I/O-bound work primarily utilizes our network or other input/output devices.
asyncio primarily helps us make I/O-bound work concurrent, but it exposes
APIs for making CPU-bound work concurrent as well.  
* Processes and threads are the basic most units of concurrency at the operating
system level. Processes can be used for I/O and CPU-bound workloads and
threads can (usually) only be used to manage I/O-bound work effectively in
Python due to the GIL preventing code from executing in parallel.  
* We’ve seen how, with non-blocking sockets, instead of stopping our application
while we wait for data to come in, we can instruct the operating system to tell us
when data has come in. Exploiting this is part of what allows asyncio to achieve
concurrency with only a single thread.  
* We’ve introduced the event loop, which is the core of asyncio applications. The
event loop loops forever, looking for tasks with CPU-bound work to run while
also pausing tasks that are waiting for I/O.  
