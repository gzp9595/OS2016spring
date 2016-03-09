phy = []

def init():
    f = open("data.txt", "r")
    s = f.readlines()
    for i in s:
        tmp = i[:-2].split(" ")
        for j in tmp:
            phy.append(int(j, 16))

def find(x):
    print "Virtual Address " + x + ":"
    x = int(x, 16)
    off = x % 32
    x = x / 32
    pte = x % 32
    pde = x / 32

    pde_base = 544
    pde_con = phy[pde_base + pde]
    print "\t--> pde index:0x%02x pde contents:(valid %d, pfn 0x%02x)" % (pde, pde_con / 128, pde_con % 128)

    if(pde_con / 128 == 0):
        return

    pte_base = pde_con % 128
    pte_con = phy[pte_base * 32 + pde]

    print "\t\t--> pte index:0x%02x pte contents:(valid %d, pfn 0x%02x)" % (pte, pte_con / 128, pte_con % 128)

    if(pte_con / 128 == 0):
        print "\t\t\t--> Fault (page table entry not valid)"
        return

    base_phy = pte_con % 128
    phy_real = phy[base_phy * 32 + off]

    print "\t\t\t--> Translates to Physical Address 0x%02x --> Value: 0x%02x" % (base_phy  * 32 + off, phy_real)



init()
find("748b")
find("390e")