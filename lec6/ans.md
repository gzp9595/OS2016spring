#lec6

##第二题第5组

```
Virtual Address 390e:
  --> pde index:0xe  pde contents:(valid 0, pfn 0x7f)
    --> pte index:0x  pte contents:(valid 0, pfn 0x7f)
       --> Fault (page directory entry not valid)
       
```

```
Virtual Address 0x748b:
    --> pde index: 0x1d pde contens:(valid 1, pfn 0x0)
      --> pde index: 0x4 pde contens:(valid 0, pfn 0x7f)
        --> Fault (page directory entry not valid)
```