###下面的log是在stride调度算法中的相关信息。

```
++ setup timer interrupts
Stride_enqueue PID: 1, name:init, stride: 2147483647
Stride_enqueue PID: 1, name:init, stride: 2147483647
Stride_enqueue PID: 2, name:, stride: 0
Stride_enqueue PID: 2, name:, stride: 2147483647
Stride_enqueue PID: 2, name:, stride: 2147483647
kernel_execve: pid = 2, name = "exit".
I am the parent. Forking the child...
Stride_enqueue PID: 3, name:, stride: 0
I am parent, fork a child pid 3
I am the parent, waiting now..
Stride_enqueue PID: 3, name:, stride: 2147483647
Stride_enqueue PID: 3, name:, stride: 2147483647
I am the child.
Stride_enqueue PID: 3, name:, stride: 2147483647
Stride_enqueue PID: 3, name:, stride: 4294967294
Stride_enqueue PID: 3, name:, stride: 4294967294
Stride_enqueue PID: 3, name:, stride: 4294967294
Stride_enqueue PID: 3, name:, stride: 2147483645
Stride_enqueue PID: 3, name:, stride: 2147483645
Stride_enqueue PID: 3, name:, stride: 2147483645
Stride_enqueue PID: 3, name:, stride: 4294967292
Stride_enqueue PID: 3, name:, stride: 4294967292
Stride_enqueue PID: 3, name:, stride: 4294967292
Stride_enqueue PID: 3, name:, stride: 2147483643
Stride_enqueue PID: 3, name:, stride: 2147483643
Stride_enqueue PID: 3, name:, stride: 2147483643
Stride_enqueue PID: 3, name:, stride: 4294967290
Stride_enqueue PID: 3, name:, stride: 4294967290
Stride_enqueue PID: 3, name:, stride: 4294967290
Stride_enqueue PID: 3, name:, stride: 2147483641
Stride_enqueue PID: 3, name:, stride: 2147483641
Stride_enqueue PID: 3, name:, stride: 2147483641
Stride_enqueue PID: 3, name:, stride: 4294967288
Stride_enqueue PID: 3, name:, stride: 4294967288
Stride_enqueue PID: 2, name:exit, stride: 2147483647
Stride_enqueue PID: 2, name:exit, stride: 4294967294
Stride_enqueue PID: 2, name:exit, stride: 4294967294
waitpid 3 ok.
exit pass.
Stride_enqueue PID: 1, name:init, stride: 2147483647
Stride_enqueue PID: 1, name:init, stride: 4294967294
Stride_enqueue PID: 1, name:init, stride: 4294967294
Stride_enqueue PID: 1, name:init, stride: 4294967294
Stride_enqueue PID: 1, name:init, stride: 2147483645
Stride_enqueue PID: 1, name:init, stride: 2147483645
all user-mode processes have quit.
init check memory pass.
kernel panic at kern/process/proc.c:460:
    initproc exit.

Welcome to the kernel debug monitor!!
```

###stride调度算法是如何避免stride溢出问题的？

因为在程序运行的过程中，整数之间的差值始终是在一个范围之类的。当其中一个数值越界的话，越界的值与其他数值的差距会很大且越界后的值一定是小的那一个。通过分析两者的差值，以及每个值的大小，就可以分析越界的问题，从而消除越界的影响。