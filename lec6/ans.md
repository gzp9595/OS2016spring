#lec6

##第二题第5组

```
Virtual Address 390e:
  --> pde index:0xe  pde contents:(valid 0, pfn 0x7f)
       --> Fault (page directory entry not valid)
       
```

```
Virtual Address 748b:
	--> pde index:0x1d pde contents:(valid 1, pfn 0x00)
		--> pte index:0x04 pte contents:(valid 0, pfn 0x7f)
			--> Fault (page table entry not valid)
```