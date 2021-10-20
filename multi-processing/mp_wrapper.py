'''
Multi-processing wrapper

Provide cpu_count, current proc info, easy way to create processes
'''


import multiprocessing as mp
from functools import wraps

# for IPC
queue = mp.SimpleQueue()
# number of current processors
proc_count = mp.cpu_count()
# sync
lock = mp.Lock()
# default context
spawn_ctx = mp.get_context('spawn')

def procs_sync(func):
    '''
    function lock decorator
    '''
    @wraps(func)
    def decorated(*args, **kwargs):
        lock.acquire()
        result = func(*args, **kwargs)
        lock.release()
        return result
    return decorated

def create_processes(fargs, context=None):
    '''
    Create len(fargs) processes and start
    target func: fargs[i][0](*fargs[i][1])

    fargs: ex. [(func,(args...)), (func,(args...)), ...]
    context: context. available value - None, 'spawn', 'fork', 'forkserver'. default None(spawn)

    Return: started processes list
    '''
    # Set context
    if context == None:
        ctx = spawn_ctx
    else:
        ctx = mp.get_context(context)
    
    # create proc and start
    num_of_proc = len(fargs)
    proc_list = []
    for i in range(num_of_proc):
        p = ctx.Process(target=fargs[i][0], args=fargs[i][1])
        proc_list.append(p)
        p.start()
    
    # join
    #for proc in proc_list:
    #    proc.join()
    #    proc.close()

    return proc_list

def get_cpu_count():
    '''
    Return current system cpu count
    '''
    return cpu_count

def curr_proc_info():
    '''
    Return current process's (name, pid)
    '''
    curr = mp.current_process()
    return curr.name, curr.pid

def pool(num_of_proc, func, map_list, context=None):
    '''
    num_of_proc processes execute map(func, map_list).
    
    num_of_proc: number of processes
    func: function
    map_list: list data
    context: context. available value - None, 'spawn', 'fork', 'forkserver'. default None(spawn)
    '''
    # Set context
    if context == None:
        ctx = spawn_ctx
    else:
        ctx = mp.get_context(context)
    
    # 
    with ctx.Pool(num_of_proc) as pool:
        pool.map(func, map_list)
