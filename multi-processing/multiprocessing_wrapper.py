'''
Multi-processing wrapper

Defined vars: queue, cpu_count
Defined funcs: procs(*args, context=None), pool(func_with_arg, arg_list, num_of_proc, context=None)
Defined classes: 
'''


import multiprocessing as mp

queue = mp.Queue()
cpu_count = mp.cpu_count()


def procs(fargs, context=None):
    '''
    Fork fargs[i][0](fargs[i][1]) processes.
    
    fargs: ex. [(func,(args...)), (func,(args...)), ...]
    context: context. available Value - None, 'spawn', 'fork', 'forkserver'
    '''
    # Set context
    ctx = mp.get_context(context)
    
    # create proc and start
    num_of_proc = len(fargs)
    proc_list = []
    for i in range(num_of_proc):
        p = ctx.Process(target=fargs[i][0], args=fargs[i][1])
        proc_list.append(p)
        p.start()
    
    # join
    for proc in proc_list:
        proc.join()


def pool(func_with_arg, arg_list, num_of_proc, context=None):
    '''
    Process func_with_arg(arg_list[0]), func_with_arg(arg_list[1]), ...
        with num_of_proc processes.
    
    func_with_arg: Function with least one arg
    arg_list: (list) args
    num_of_proc: number of processes
    context: context. available Value - None, 'spawn', 'fork', 'forkserver'
    '''
    ctx = mp.get_context(context)
    
    pool = ctx.Pool(num_of_proc)
    pool.map(func_with_arg, arg_list)
    pool.close()
