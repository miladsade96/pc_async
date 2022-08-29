# Chapter 2
## Asyncio basics



### Introducing coroutines
Think of a coroutine like a regular Python function but with the superpower that it
can pause its execution when it encounters an operation that could take a while to
complete. When that long-running operation is complete, we can “wake up” our
paused coroutine and finish executing any other code in that coroutine. While a
paused coroutine is waiting for the operation it paused for to finish, we can run other
code. This running of other code while waiting is what gives our application concurrency
We can also run several time-consuming operations concurrently, which can give our 
applications big performance improvements.  

#### Creating coroutines with the async keyword
Creating a coroutine is straightforward and not much different from creating a normal
Python function. The only difference is that, instead of using the def keyword, we
use async def. The async keyword marks a function as a coroutine instead of a normal
Python function.  

This is an important point, as coroutines aren’t executed when we call them directly. Instead, 
we create a coroutine object that can be run later. To run a coroutine, we need to explicitly 
run it on an event loop.  

#### Pausing execution with the await keyword
Using the await keyword will cause the coroutine following it to be run, unlike
calling a coroutine directly, which produces a coroutine object. The await expression
will also pause the coroutine where it is contained in until the coroutine we awaited
finishes and returns a result. When the coroutine we awaited finishes, we’ll have
access to the result it returned, and the containing coroutine will “wake up” to handle
the result.  


### Running concurrently with tasks
Tasks are wrappers around a coroutine that schedule a coroutine to run on the
event loop as soon as possible. This scheduling and execution happen in a non-blocking
fashion, meaning that, once we create a task, we can execute other code instantly
while the task is running. This contrasts with using the await keyword that acts in a
blocking manner, meaning that we pause the entire coroutine until the result of the
await expression comes back.  

The fact that we can create tasks and schedule them to run instantly on the event
loop means that we can execute multiple tasks at roughly the same time. When these
tasks wrap a long-running operation, any waiting they do will happen concurrently. To
illustrate this, let’s create two tasks and try to run them at the same time.  

#### Running multiple tasks concurrently
Given that tasks are created instantly and are scheduled to run as soon as possible, this
allows us to run many long-running tasks concurrently. We can do this by sequentially
starting multiple tasks with our long-running coroutine.  

**Note:** This benefit compounds as we add more tasks; if we had launched 10 of these tasks, 
we would still take roughly 3 seconds, giving us a 10-fold speedup.  


### Canceling tasks and setting timeouts
Network connections can be unreliable. A user’s connection may drop because of a
network slowdown, or a web server may crash and leave existing requests in limbo.
When making one of these requests, we need to be especially careful that we don’t
wait indefinitely. Doing so could lead to our application hanging, waiting forever for a
result that may never come.  

Additionally, we may want to allow our users a choice if a task continues to run. A user may 
proactively decide things are taking too long, or they may want to stop a task they made in 
error.  

#### Canceling tasks
Canceling a task is straightforward. Each task object has a method named cancel ,
which we can call whenever we’d like to stop a task. Canceling a task will cause that
task to raise a CancelledError when we await it, which we can then handle as
needed.  

#### Setting a timeout and canceling with wait_for
asyncio provides this functionality through a function called asyncio.wait_for .
This function takes in a coroutine or task object, and a timeout specified in seconds. It
then returns a coroutine that we can await . If the task takes more time to complete
than the timeout we gave it, a TimeoutException will be raised. Once we have reached
the timeout threshold, the task will automatically be canceled.  

Canceling tasks automatically if they take longer than expected is normally a good
idea. Otherwise, we may have a coroutine waiting indefinitely, taking up resources
that may never be released. However, in certain circumstances we may want to keep
our coroutine running. For example, we may want to inform a user that something is
taking longer than expected after a certain amount of time but not cancel the task
when the timeout is exceeded.  

To do this we can wrap our task with the asyncio.shield function. This function will prevent 
cancellation of the coroutine we pass in, giving it a “shield,” which cancellation requests 
then ignore.  


### Tasks, coroutines, futures, and awaitables
Coroutines and tasks can both be used in await expressions. So what is the common thread 
between them? To understand, we’ll need to know about both a future as well as an awaitable.  

#### Introducing futures
A future is a Python object that contains a single value that you expect to get at some
point in the future but may not yet have. Usually, when you create a future , it does
not have any value it wraps around because it doesn’t yet exist. In this state, it is 
considered incomplete, unresolved, or simply not done. Then, once you get a result, you
can set the value of the future . This will complete the future ; at that time, we can
consider it finished and extract the result from the future .  

**NOTE:** We don’t call the result method before the result is set because the result method 
will throw an invalid state exception if we do so.  

In the world of asyncio, you should rarely need to deal with futures. That said, you
will run into some asyncio APIs which return futures, and you may need to work with
callback-based code, which can require futures.  

#### The relationship between futures, tasks, and coroutines
There is a strong relationship between tasks and futures. In fact, task directly inherits
from future . A future can be thought as representing a value that we won’t have for
a while. A task can be thought as a combination of both a coroutine and a future .
When we create a task , we are creating an empty future and running the coroutine.
Then, when the coroutine has completed with either an exception or a result, we set
the result or exception of the future.  


### The pitfalls of coroutines and tasks
When seeing the performance improvements we can obtain from running some of
our longer tasks concurrently, we can be tempted to start to use coroutines and tasks
everywhere in our applications. While it depends on the application you’re writing,
simply marking functions async and wrapping them in tasks may not help application
performance. In certain cases, this may degrade performance of your applications.
Two main errors occur when trying to turn your applications asynchronous. The first
is attempting to run CPU-bound code in tasks or coroutines without using multiprocessing;
the second is using blocking I/O-bound APIs without using multithreading.  

#### Running CPU-bound code
We may have functions that perform computationally expensive calculations, such as
looping over a large dictionary or doing a mathematical computation. Where we have
several of these functions with the potential to run concurrently, we may get the idea
to run them in separate tasks. In concept, this is a good idea, but remember that
asyncio has a single-threaded concurrency model. This means we are still subject to
the limitations of a single thread and the global interpreter lock.  

#### Running blocking APIs
We may also be tempted to use our existing libraries for I/O-bound operations by
wrapping them in coroutines. However, this will generate the same issues that we saw
with CPU-bound operations. These APIs block the main thread. Therefore, when we
run a blocking API call inside a coroutine, we’re blocking the event loop thread itself,
meaning that we stop any other coroutines or tasks from executing. Examples of
blocking API calls include libraries such as requests , or time.sleep . Generally, any
function that performs I/O that is not a coroutine or performs time-consuming CPU
operations can be considered blocking.  

You need to use a library that supports coroutines and utilizes non-blocking sockets. This 
means that if the library you are using does not return coroutines and you aren’t using await 
in your own coroutines, you’re likely making a blocking call.  


### Accessing and manually managing the event loop
Until now, we have used the convenient asyncio.run to run our application and create
the event loop for us behind the scenes. Given the ease of use, this is the preferred
method to create the event loop. However, there may be cases in which we don’t want
the functionality that asyncio.run provides. As an example, we may want to execute
custom logic to stop tasks that differ from what asyncio.run does, such as letting any
remaining tasks finish instead of stopping them.  

#### Creating an event loop manually
We can create an event loop by using the asyncio.new_event_loop method. This will
return an event loop instance. With this, we have access to all the low-level methods
that the event loop has to offer. With the event loop we have access to a method
named run_until_complete , which takes a coroutine and runs it until it finishes.  

#### Accessing the event loop
From time to time, we may need to access the currently running event loop. asyncio
exposes the asyncio.get_running_loop function that allows us to get the current
event loop. As an example, let’s look at call_soon , which will schedule a function to
run on the next iteration of the event loop.  


### Using debug mode
When we run in debug mode, we’ll see a few helpful log messages when a coroutine
or task takes more than 100 milliseconds to run. In addition, if we don’t await a
coroutine, an exception is thrown, so we can see where to properly add an await .
There are a few different ways to run in debug mode.  

#### Using asyncio.run
The asyncio.run function we have been using to run coroutines exposes a debug
parameter. By default, this is set to False , but we can set this to True to enable
debug mode:
```text
asyncio.run(coroutine(), debug=True)
```

#### Using command-line arguments
Debug mode can be enabled by passing a command-line argument when we start our
Python application. To do this we apply -X dev :
```text
python3 -X dev program.py
```

#### Using environment variables
We can also use environment variables to enable debug mode by setting the
PYTHONASYNCIODEBUG variable to 1 :
```text
PYTHONASYINCIODEBUG=1 python3 program.py
```

In debug mode, we’ll see informative messages logged when a coroutine takes too long.  


### Summary
* We’ve learned how to create coroutines with the async keyword. Coroutines can suspend their 
execution on a blocking operation. This allows for other coroutines to run. Once the operation 
where the coroutine suspended completes , our coroutine will wake up and resume where it left
off.  
* We learned to use await in front of a call to a coroutine to run it and wait for it to 
return a value. To do so, the coroutine with the await inside it will suspend its execution, 
while waiting for a result. This allows other coroutines to run while the first coroutine is 
awaiting its result.
* We’ve learned how to use asyncio.run to execute a single coroutine. We can use this function 
to run the coroutine that is the main entry point into our application.  
* We’ve learned how to use tasks to run multiple long-running operations concurrently. Tasks 
are wrappers around coroutines that will then be run on the event loop. When we create a task,
it is scheduled to run on the event loop as soon as possible.  
* We’ve learned how to cancel tasks if we want to stop them and how to add a timeout to a task 
to prevent them from taking forever. Canceling a task will make it raise a CancelledError 
while we await it. If we have time limits on how long a task should take, we can set timeouts 
on it by using asycio.wait_for .  
* We’ve learned to avoid common issues that newcomers make when using asyncio. The first is 
running CPU-bound code in coroutines. CPU-bound code will block the event loop from running 
other coroutines since we’re still single-threaded. The second is blocking I/O, since we can’t 
use normal libraries with asyncio, and you must use asyncio-specific ones that return 
coroutines. If your coroutine does not have an await in it, you should consider it suspicious. 
There are still ways to use CPU-bound and blocking I/O with asyncio.  
* We’ve learned how to use debug mode. Debug mode can help us diagnose common issues in 
asyncio code, such as running CPU-intensive code in a coroutine.
