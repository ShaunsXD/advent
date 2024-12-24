def part1():
    with open("24.txt", "r") as file:
        data = file.read().split("\n")

    def bitAnd(x, y):
        return x & y

    def bitOr(x, y):
        return x | y

    def bitXOR(x, y):
        return x ^ y

    registers = {}
    rules = []
    for rule in data[data.index("") + 1:]:
        rule = rule.split(" ")
        rules.append(rule)

        register1 = rule[0]
        register2 = rule[2]
        register3 = rule[-1]

        if register1 not in registers:
            registers[register1] = None
        if register2 not in registers:
            registers[register2] = None
        if register3 not in registers:
            registers[register3] = None

    var = data[0:data.index("")]
    for bit in var:
        bit = bit.split(": ")
        registers[bit[0]] = int(bit[1])

    print(registers)

    while rules:
        for rule in rules:
            register1 = rule[0]
            register2 = rule[2]
            register3 = rule[-1]
            operation = rule[1]

            if registers[register1] is not None and registers[register2] is not None:
                if operation == "AND":
                    registers[register3] = bitAnd(registers[register1], registers[register2])
                elif operation == "OR":
                    registers[register3] = bitOr(registers[register1], registers[register2])
                elif operation == "XOR":
                    registers[register3] = bitXOR(registers[register1], registers[register2])

                rules.pop(rules.index(rule))

    registers = dict(sorted(registers.items()))
    byte_str = ""
    for key, value in registers.items():
        if key[0] == "z":
            byte_str += str(value)
    byte_str = byte_str[::-1]
    print(int(byte_str, 2))


# djg,dsd,hjm,mcq,sbg,z12,z19,z37
#
# S0 = A0 ^ B0
# C0 = A0 & B0
# S1 = (A1 ^ B1) ^ C0
# C1 = (A1 & B1) | ((A1 ^ B1) & C0)
#
#
# jsb AND njf -> z12
# S0 = A0 ^ B0
# C0 = A0 & B0
# S1 = jsb ^ C0
# C1 = djr | (jsb & C0)
#
# z00 = x00 XOR y00
# C0 = ktt
#
# S1 = rvb ^ ktt = z01
# C1 = kgp | kmb = rkn
#
# S2 = ssq ^ rkn = z02
# C2 = kwm | vsc = ntj
#
# S3 = fbk ^ ntj = z03
# C3 = jmr | dps = mpf
#
# S4 = jjc ^ mpf = z04
# C4 = csm | gvt = cgt
#
# S5 = kdm ^ cgt = z05
# C5 = fjd | (sch) = ftg
#
# S6 = mhv ^ ftg = z06
# C6 = kfb | njj = gpv
#
# S7 = dts ^ gpv = z07
# C7 = qss | whm = mtm
#
# S8 = wqw ^ mtm = z08
# C8 = wvw | rdt = trw
#
# S9 = pmb ^ trw = z09
# C9 = fhf | pvb = rqp
#
# S10 = hcd ^ rqp = z10
# C10 = wnv | sqt = hww
#
# S11 = fkc ^ hww = z11
# C11 = wkn | dcc = njf
#
# S12 = jsb ^ njf = z12        (MISSMATCH z12 djg)
# C12 = djr | djg = nbf
#
# S13 = fnc ^ nbf = z13
# C13 = ntm | mwj = tnq
#
#
# S14 = nbp ^ tnq = z14
# C14 = tmw | cpr = dhb
#
# S15 = ktv ^ dhb = z15
# C15 = ptm | pks = dnd
#
# S16 = nqd ^ dnd = z16
# C16 = mgr | stm = cpv
#
# S17 = wjh ^ cpv = z17
# C17 = bpg | jtp = pft
#
# S18 = qcp ^ pft = z18
# C18 = fsc | bcq = qjc
#
# S19 = kbs ^ qjc = z19 			(MISSMATCH z19 sbg)
# C19 = sbg | bnh = jwg
#
# S20 = ckt ^ jwg = z20
# C20 = rpc | bgs = nqq
#
# S21 = hgv ^ nqq = z21
# C21 = nqk | mdk = tbs
#
# S22 = kvp ^ tbs = z22
# C22 = bsr | njd = cpq
#
# S23 = tkb ^ cpq = z23
# C23 = mks | jqs = jrr
#
# S24 = mcq ^ jrr = z24 			(MISSMATCH hjm mcq)
# C24 = hjm | rpj = sqr
#
# S25 = wpd ^ sqr = z25
# C25 = ffg | tpj = jrb
#
# S26 = tmk ^ jrb = z26
# C26 = jjp | wcc = fqp
#
# S27 = qdg ^ fqp = z27
# C27 = jqg | trd = nrd
#
# S28 = gkk ^ nrd = z28
# C28 = kgm | smk = rmg
#
# S29 = hhm ^ rmg = z29
# C29 = rwk | ktc = dmn
#
# S30 = rkw ^ dmn = z30
# C30 = bfn | gwm = smd
#
# S31 = qvw ^ smd = z31
# C31 = jsf | dkq = frt
#
# S32 = pgs ^ frt = z32
# C32 = psb | vfq = wrg
#
# S33 = jkm ^ wrg = z33
# C33 = jpc | vsk = hqv
#
# S34 = bcf ^ hqv = z34
# C34 = gbk | cwc = dgv
#
# S35 = kbm ^ dgv = z35
# C35 = mwp | vsb = jqc
#
# S36 = qmj ^ jqc = z36
# C36 = hjs | vwj = hhp
#
# S37 = tjm ^ hhp 		(MISSMATCH dsd z37)
# C37 = gqf | (tjm & hhp)