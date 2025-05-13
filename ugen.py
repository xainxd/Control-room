for tt in range(10000):
    rr=random.randint
    rc=random.choice
    mob=rc(["zh","en","km","de","id","fr","my","it","pl","sv"])
    iphone=rc(["15_5","10_0_2","10_1_1","15_6","10_3_3","10_3_2","10_2_1","10_2","15_6_1","14_8_1","15_4_1"])
    iphone1=rc(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
    iphone2=rc(["14A456","15E148","14B100","14C92","14E304","10B144","9B206","14G60","13E233","13F69","13E238"])
    zx1=f"Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/14.0.{str(rr(1,10))} Mobile/{iphone2} Safari/60{str(rr(1,10))}.1"
    zx2=f"SAMSUNG-GT-E2252 Opera/9.80 (J2ME/MIDP; Opera Mini/{str(rr(1,20))}.{str(rr(1,20))}.{str(rr(10000,90000))}/{str(rr(100,199))}.{str(rr(200,300))}; U; {mob}) Presto/{str(rr(1,9))}.{str(rr(5,49))}.{str(rr(20,999))} Version/12.16"
    uaku2 = rc([zx1,zx2])
    ugen.append(uaku2)    
