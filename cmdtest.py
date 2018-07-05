#!/usr/bin/python
import os
import subprocess as sp
import re
import oom_adj
import dps_meminfo
import category
import time

import proc_meminfo

from pandas import Series, DataFrame, ExcelWriter



#p = sp.Popen("adb shell dumpsys -t 60 meminfo", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
#p = sp.Popen("cat ./dpmeminfo.txt", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
#dumpsys_meminfo = p.stdout.readlines()
#print dumpsys_meminfo

process  = {}
oom_adj  = oom_adj.oom_adj()
category = category.category()
dps_meminfo_0 = dps_meminfo.dps_meminfo(process, oom_adj, category)



#'''

df_OOM_ADJ = DataFrame()
df_OOM_ADJ_Persist = DataFrame()
df_category = DataFrame()
df_all = DataFrame()

writer = ExcelWriter('output.xlsx')
index = 0
Persist_len = 0

while index < 100:
    index = index + 1
    print "SampleCount:", "{:0>8} ".format(index),  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #p = sp.Popen("cat ./dpmeminfo.txt", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    p = sp.Popen("adb shell dumpsys -t 60 meminfo", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    dumpsys_meminfo = p.stdout.readlines()
    #print dumpsys_meminfo
    dps_meminfo_0.parse_dumpsys_meminfo(dumpsys_meminfo)

    columns_OOM_ADJ         = []
    columns_OOM_ADJ_Persist = []
    columns_category        = []
    columns_all             = []
    values_OOM_ADJ          = []
    values_OOM_ADJ_Persist  = []
    values_category         = []
    values_all              = []
    
    #append Native data
    columns_OOM_ADJ.append("OOM_ADJ.Native")
    values_OOM_ADJ.append(dps_meminfo_0.oom_adj.Native.Total/1024)

    #
    columns_OOM_ADJ.append("OOM_ADJ.SystemServer")
    values_OOM_ADJ.append(int(dps_meminfo_0.oom_adj.System.Total)/1024)

    #append persistent data
    columns_OOM_ADJ.append("OOM_ADJ.Persist")
    values_OOM_ADJ.append(int(dps_meminfo_0.oom_adj.Persistent.Total)/1024)

    if Persist_len != len(dps_meminfo_0.oom_adj.Persistent.content.keys()):
        Persist_len = len(dps_meminfo_0.oom_adj.Persistent.content.keys())
        #print dps_meminfo_0.oom_adj.Persistent.content.keys()
    
    for item in sorted(dps_meminfo_0.oom_adj.Persistent.content.keys()):
        #print item, "---", int(dps_meminfo_0.oom_adj.Persistent.content[item])/1024
        columns_OOM_ADJ_Persist.append("OOM_ADJ.Persist."+re.subn(" \(.*\).*","",item)[0])
        values_OOM_ADJ_Persist.append(int(dps_meminfo_0.oom_adj.Persistent.content[item])/1024)

    #append oom_adj.Foreground data
    columns_OOM_ADJ.append("OOM_ADJ.Foreground")
    values_OOM_ADJ.append(int(dps_meminfo_0.oom_adj.Foreground.Total)/1024)

    #append oom_adj.Visible data
    columns_OOM_ADJ.append("OOM_ADJ.Visible")
    values_OOM_ADJ.append(int(dps_meminfo_0.oom_adj.Visible.Total)/1024)

    #append oom_adj.Perceptible data
    columns_OOM_ADJ.append("OOM_ADJ.Perceptible")
    values_OOM_ADJ.append(int(dps_meminfo_0.oom_adj.Perceptible.Total)/1024)

    #append oom_adj.AService data
    columns_OOM_ADJ.append("OOM_ADJ.AServices")
    values_OOM_ADJ.append(int(dps_meminfo_0.oom_adj.AServices.Total)/1024)

    #append oom_adj.Home data
    columns_OOM_ADJ.append("OOM_ADJ.Home")
    values_OOM_ADJ.append(int(dps_meminfo_0.oom_adj.Home.Total)/1024)

    #append oom_adj.BService data
    columns_OOM_ADJ.append("OOM_ADJ.BServices")
    values_OOM_ADJ.append(int(dps_meminfo_0.oom_adj.BServices.Total)/1024)

    #append oom_adj.Cached dYata
    columns_OOM_ADJ.append("OOM_ADJ.Cached")
    values_OOM_ADJ.append(int(dps_meminfo_0.oom_adj.Cached.Total)/1024)
    
    #append PPS by category data
    columns_category.append("category.Native")
    columns_category.append("category.Dalvik")
    columns_category.append("category.dex_mmap")
    columns_category.append("category.so_mmap")
    columns_category.append("category.unknown")
    columns_category.append("category.oat_mmap")
    columns_category.append("category.art_mmap")
    columns_category.append("category.dalvik_other")
    columns_category.append("category.apk_mmap")
    columns_category.append("category.egl_mtrack")
    columns_category.append("category.gl_mtrack")
    columns_category.append("category.stack")
    columns_category.append("category.gfx_dev")
    columns_category.append("category.other_mmap")
    columns_category.append("category.jar_mmap")
    columns_category.append("category.cursor")
    columns_category.append("category.other_mtrack")
    
    values_category.append(int(dps_meminfo_0.category.Native)/1024)
    values_category.append(int(dps_meminfo_0.category.Dalvik)/1024)
    values_category.append(int(dps_meminfo_0.category.dex_mmap)/1024)
    values_category.append(int(dps_meminfo_0.category.so_mmap)/1024)
    values_category.append(int(dps_meminfo_0.category.unknown)/1024)
    values_category.append(int(dps_meminfo_0.category.oat_mmap)/1024)
    values_category.append(int(dps_meminfo_0.category.art_mmap)/1024)
    values_category.append(int(dps_meminfo_0.category.dalvik_other)/1024)
    values_category.append(int(dps_meminfo_0.category.apk_mmap)/1024)
    values_category.append(int(dps_meminfo_0.category.egl_mtrack)/1024)
    values_category.append(int(dps_meminfo_0.category.gl_mtrack)/1024)
    values_category.append(int(dps_meminfo_0.category.stack)/1024)
    values_category.append(int(dps_meminfo_0.category.gfx_dev)/1024)
    values_category.append(int(dps_meminfo_0.category.other_mmap)/1024)
    values_category.append(int(dps_meminfo_0.category.jar_mmap)/1024)
    values_category.append(int(dps_meminfo_0.category.cursor)/1024)
    values_category.append(int(dps_meminfo_0.category.other_mtrack)/1024)


    #append FreeRam data
    columns_all.append("FreeRam")
    values_all.append(dps_meminfo_0.freeram/1024)
    columns_all.append("FreeRam.Cached_pss")
    values_all.append(dps_meminfo_0.cached_pss/1024)
    columns_all.append("FreeRam.Cached_kernel")
    values_all.append(dps_meminfo_0.cached_kernel/1024)
    columns_all.append("FreeRam.free")
    values_all.append(dps_meminfo_0.free/1024)

    #append UsedRam data
    columns_all.append("UsedRam")
    values_all.append(dps_meminfo_0.usedram/1024)
    columns_all.append("UsedRam.usedpss")
    values_all.append(dps_meminfo_0.used_pss/1024)
    columns_all.append("UsedRam.kernel")
    values_all.append(dps_meminfo_0.kernel/1024)

    #append LostRam data
    columns_all.append("LostRam")
    values_all.append(dps_meminfo_0.lostram/1024)

    #append Zram data
    columns_all.append("ZRAM.physical_used")
    columns_all.append("ZRAM.in_swap")
    columns_all.append("ZRAM.total_swap")
    #print dps_meminfo_0.zram
    if len(dps_meminfo_0.zram) is not 0:
        values_all.append(dps_meminfo_0.zram[0]/1024)
        values_all.append(dps_meminfo_0.zram[1]/1024)
        values_all.append(dps_meminfo_0.zram[2]/1024)
    else:
        print "zram error parsed!"
        exit()
        
    df_OOM_ADJ = DataFrame(columns = columns_OOM_ADJ)
    df_OOM_ADJ.loc[0] = values_OOM_ADJ
    df_OOM_ADJ_Persist = DataFrame(columns = columns_OOM_ADJ_Persist)
    df_OOM_ADJ_Persist.loc[0] = values_OOM_ADJ_Persist
    df_category = DataFrame(columns = columns_category)
    df_category.loc[0] = values_category
    df_all = DataFrame(columns = columns_all)
    df_all.loc[0] = values_all
    
    #print columns
    #print values

    #dump meminfo to specific file
    if index == 1:
        df_OOM_ADJ.to_excel(excel_writer=writer,         sheet_name='OOM_ADJ',         header=True,  index=False, startrow=index, startcol=1)
        df_OOM_ADJ_Persist.to_excel(excel_writer=writer, sheet_name='OOM_ADJ_Persist', header=True,  index=False, startrow=index, startcol=1)
        df_category.to_excel(excel_writer=writer,        sheet_name='category',        header=True,  index=False, startrow=index, startcol=1)
        df_all.to_excel(excel_writer=writer,             sheet_name='All',             header=True,  index=False, startrow=index, startcol=1)
    else:
        df_OOM_ADJ.to_excel(excel_writer=writer,         sheet_name='OOM_ADJ',         header=False, index=False, startrow=index+1, startcol=1) 
        df_OOM_ADJ_Persist.to_excel(excel_writer=writer, sheet_name='OOM_ADJ_Persist', header=False, index=False, startrow=index+1, startcol=1) 
        df_category.to_excel(excel_writer=writer,        sheet_name='category',        header=False, index=False, startrow=index+1, startcol=1)
        df_all.to_excel(excel_writer=writer,             sheet_name='All',             header=False, index=False, startrow=index+1, startcol=1)
#print columns
#print oom_adj.Persistent.Total
#'''

'''
#while True:
    i = i + 1
    p = sp.Popen("cat ./dpmeminfo.txt", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    dumpsys_meminfo = p.stdout.readlines()
    #print "calling parse_dumpsys_meminfo"
    #print "hello"
    #p = File()
    dps_meminfo_0.parse_dumpsys_meminfo(dumpsys_meminfo)
    df.loc[0] = [dps_meminfo_0.oom_adj.System,\
                 dps_meminfo_0.oom_adj.Persistent.content[],   ]
    #print "{:<32}".format("oom_adj.System"),      "{:>8}".format(oom_adj.System.Total)
    retval = p.wait()
'''    



#this part is for dumpsys meminfo parsing
'''
process  = {}
oom_adj  = oom_adj.oom_adj()
category = category.category()
dps_meminfo_0 = dps_meminfo.dps_meminfo(process, oom_adj, category)
#print "calling parse_dumpsys_meminfo"
#print "hello"
#p = File()
p = sp.Popen("adb shell dumpsys -t 60 meminfo", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
dumpsys_meminfo = p.stdout.readlines()
print "test2"
dps_meminfo_0.parse_dumpsys_meminfo(dumpsys_meminfo)
print "{:<32}".format("oom_adj.System"),      "{:>8}".format(oom_adj.System.Total)
retval = p.wait()


#if True:
while (True):
    #global p
    #print "test"
    p = sp.Popen("adb shell dumpsys -t 60 meminfo", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    #print "test1"
    dumpsys_meminfo = p.stdout.readlines()
    #print "test2"
    dps_meminfo_0.parse_dumpsys_meminfo(dumpsys_meminfo)
    print "{:<32}".format("oom_adj.System"),      "{:>8}".format(oom_adj.System.Total)
    retval = p.wait()

#print ""
'''



'''
proc_meminfo_0 = proc_meminfo.proc_meminfo()

while True:

    p = sp.Popen("adb shell cat /proc/meminfo", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    #p = sp.Popen("cat proc_meminfo.txt", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    prc_meminfo = p.stdout.readlines()
    #for line in proc_meminfo:
    #    print line,
    proc_meminfo_0.parse_proc_meminfo(prc_meminfo)

    #print "{:<16}".format("MemFree "),  "{:>8}".format(proc_meminfo_0.MemFree), " kB"         
    #print "{:<16}".format("MemAvailable "), "{:>8}".format(proc_meminfo_0.MemAvailable), " kB"    
    #print "{:<16}".format("Buffers "), "{:>8}".format(proc_meminfo_0.Buffers), " kB"         
    #print "{:<16}".format("Cached "),  "{:>8}".format(proc_meminfo_0.Cached), " kB"          
    #print "{:<16}".format("SwapCached "), "{:>8}".format(proc_meminfo_0.SwapCached), " kB"      
    print "{:>8}".format((int(proc_meminfo_0.MemFree) +\
                          int(proc_meminfo_0.Buffers) +\
                          int(proc_meminfo_0.Cached)  +\
                          int(proc_meminfo_0.SwapCached))/1024)

retval = p.wait()
'''


#print /proc/meminfo
'''
print dir(proc_meminfo_0)

print "{:<16}".format("MemTotal "), "{:>8}".format(proc_meminfo_0.MemTotal), " kB"
print "{:<16}".format("MemFree "),  "{:>8}".format(proc_meminfo_0.MemFree), " kB"         
print "{:<16}".format("MemAvailable "), "{:>8}".format(proc_meminfo_0.MemAvailable), " kB"    
print "{:<16}".format("Buffers "), "{:>8}".format(proc_meminfo_0.Buffers), " kB"         
print "{:<16}".format("Cached "),  "{:>8}".format(proc_meminfo_0.Cached), " kB"          
print "{:<16}".format("SwapCached "), "{:>8}".format(proc_meminfo_0.SwapCached), " kB"      

print "{:<16}".format("Active "),     "{:>8}".format(proc_meminfo_0.Active), " kB"          
print "{:<16}".format("Inactive "),   "{:>8}".format(proc_meminfo_0.Inactive), " kB"        
print "{:<16}".format("Active_anon "),   "{:>8}".format(proc_meminfo_0.Active_anon), " kB"          
print "{:<16}".format("Inactive_anon "), "{:>8}".format(proc_meminfo_0.Inactive_anon), " kB"   
print "{:<16}".format("Active_file "),   "{:>8}".format(proc_meminfo_0.Active_file), " kB"     
print "{:<16}".format("Inactive_file "), "{:>8}".format(proc_meminfo_0.Inactive_file), " kB"

print "{:<16}".format("Unevictable "),   "{:>8}".format(proc_meminfo_0.Unevictable), " kB"     
print "{:<16}".format("Mlocked "),   "{:>8}".format(proc_meminfo_0.Mlocked), " kB"         
print "{:<16}".format("HighTotal "), "{:>8}".format(proc_meminfo_0.HighTotal), " kB"       
print "{:<16}".format("HighFree "), "{:>8}".format(proc_meminfo_0.HighFree), " kB"        
print "{:<16}".format("LowTotal "), "{:>8}".format(proc_meminfo_0.LowTotal), " kB"        
print "{:<16}".format("LowFree "), "{:>8}".format(proc_meminfo_0.LowFree), " kB"         
print "{:<16}".format("SwapTotal "), "{:>8}".format(proc_meminfo_0.SwapTotal), " kB"       
print "{:<16}".format("SwapFree "), "{:>8}".format(proc_meminfo_0.SwapFree), " kB"        
print "{:<16}".format("Dirty "), "{:>8}".format(proc_meminfo_0.Dirty), " kB"           
print "{:<16}".format("Writeback "), "{:>8}".format(proc_meminfo_0.Writeback), " kB"       
print "{:<16}".format("AnonPages "), "{:>8}".format(proc_meminfo_0.AnonPages), " kB"       
print "{:<16}".format("Mapped "), "{:>8}".format(proc_meminfo_0.Mapped), " kB"          
print "{:<16}".format("Shmem "), "{:>8}".format(proc_meminfo_0.Shmem), " kB"           
print "{:<16}".format("Slab "), "{:>8}".format(proc_meminfo_0.Slab), " kB"            
print "{:<16}".format("SReclaimable "), "{:>8}".format(proc_meminfo_0.SReclaimable), " kB"    
print "{:<16}".format("SUnreclaim "), "{:>8}".format(proc_meminfo_0.SUnreclaim), " kB"      
print "{:<16}".format("KernelStack "), "{:>8}".format(proc_meminfo_0.KernelStack), " kB"     
print "{:<16}".format("PageTables "), "{:>8}".format(proc_meminfo_0.PageTables), " kB"      
print "{:<16}".format("NFS_Unstable "), "{:>8}".format(proc_meminfo_0.NFS_Unstable), " kB"             
print "{:<16}".format("Bounce "), "{:>8}".format(proc_meminfo_0.Bounce), " kB"          
print "{:<16}".format("WritebackTmp "), "{:>8}".format(proc_meminfo_0.WritebackTmp), " kB"    
print "{:<16}".format("CommitLimit "), "{:>8}".format(proc_meminfo_0.CommitLimit), " kB"     
print "{:<16}".format("Committed_AS "), "{:>8}".format(proc_meminfo_0.Committed), " kB"       
print "{:<16}".format("VmallocTotal "), "{:>8}".format(proc_meminfo_0.VmallocTotal), " kB"    
print "{:<16}".format("VmallocUsed "), "{:>8}".format(proc_meminfo_0.VmallocUsed), " kB"     
print "{:<16}".format("VmallocChunk "), "{:>8}".format(proc_meminfo_0.VmallocChunk), " kB"    
print "{:<16}".format("CmaTotal "), "{:>8}".format(proc_meminfo_0.CmaTotal), " kB"        
print "{:<16}".format("CmaFree "), "{:>8}".format(proc_meminfo_0.CmaFree), " kB"         

retval = p.wait()
'''



'''
print "{:<32}".format("oom_adj.Native"),      "{:>8}".format(oom_adj.Native.Total)
print "{:<32}".format("oom_adj.System"),      "{:>8}".format(oom_adj.System.Total)
print "{:<32}".format("oom_adj.Persistent"),  "{:>8}".format(oom_adj.Persistent.Total)
print "----"
'''
'''
#show the "Total PSS by process:" part
for item in sorted(dps_meminfo_0.process.items(), key=lambda d:d[1], reverse=True):
    print "{:<64}".format(item[0]), "---", item[1]
'''

'''
#print "{:<32}".format("dps_meminfo_0.process"),      dps_meminfo_0.process 
print "{:<32}".format("dps_meminfo_0.oom_adj"),       dps_meminfo_0.oom_adj
print "{:<32}".format("dps_meminfo_0.category"),      dps_meminfo_0.category 
print "{:<32}".format("dps_meminfo_0.totalram"),      dps_meminfo_0.totalram
print "{:<32}".format("dps_meminfo_0.freeram"),       dps_meminfo_0.freeram
print "{:<32}".format("dps_meminfo_0.usedram"),       dps_meminfo_0.usedram
print "{:<32}".format("dps_meminfo_0.lostram"),       dps_meminfo_0.lostram
print "{:<32}".format("dps_meminfo_0.zram"),          dps_meminfo_0.zram 
print "{:<32}".format("dps_meminfo_0.oom"),           dps_meminfo_0.oom
print "{:<32}".format("dps_meminfo_0.restore_limit"), dps_meminfo_0.restore_limit
print "{:<32}".format("dps_meminfo_0.high_end_gfx"),  dps_meminfo_0.high_end_gfx

print "{:<32}".format("dps_meminfo_0.cached_pss"),    dps_meminfo_0.cached_pss
print "{:<32}".format("dps_meminfo_0.cached_kernel"), dps_meminfo_0.cached_kernel
print "{:<32}".format("dps_meminfo_0.free"),          dps_meminfo_0.free

print "{:<32}".format("dps_meminfo_0.used_pss"),      dps_meminfo_0.used_pss
print "{:<32}".format("dps_meminfo_0.kernel"),        dps_meminfo_0.kernel
'''

'''
for item in oom_adj.Persistent.content.keys():
    print "{:<48}".format(item), ":", "{:>8}".format(oom_adj.Persistent.content[item])
'''

'''
print "----"
print "{:<32}".format("oom_adj.Foreground"),  "{:>8}".format(oom_adj.Foreground.Total)
print "{:<32}".format("oom_adj.Visible"),     "{:>8}".format(oom_adj.Visible.Total)
print "{:<32}".format("oom_adj.Perceptible"), "{:>8}".format(oom_adj.Perceptible.Total)
print "{:<32}".format("oom_adj.AServices"),   "{:>8}".format(oom_adj.AServices.Total)
print "{:<32}".format("oom_adj.Home"),        "{:>8}".format(oom_adj.Home.Total)
print "{:<32}".format("oom_adj.BServices"),   "{:>8}".format(oom_adj.BServices.Total)
print "{:<32}".format("oom_adj.Cached"),      "{:>8}".format(oom_adj.Cached.Total)

print "---"


print "{:<32}".format("category.Native:"),       "{:>8}".format(dps_meminfo_0.category.Native)
print "{:<32}".format("category.Dalvik:"),       "{:>8}".format(dps_meminfo_0.category.Dalvik)
print "{:<32}".format("category.dex_mmap:"),     "{:>8}".format(dps_meminfo_0.category.dex_mmap)
print "{:<32}".format("category.so_mmap:"),      "{:>8}".format(dps_meminfo_0.category.so_mmap)
print "{:<32}".format("category.unknown:"),      "{:>8}".format(dps_meminfo_0.category.unknown)
print "{:<32}".format("category.oat_mmap:"),     "{:>8}".format(dps_meminfo_0.category.oat_mmap)
print "{:<32}".format("category.art_mmap:"),     "{:>8}".format(dps_meminfo_0.category.art_mmap)
print "{:<32}".format("category.dalvik_other:"), "{:>8}".format(dps_meminfo_0.category.dalvik_other)
print "{:<32}".format("category.apk_mmap:"),     "{:>8}".format(dps_meminfo_0.category.apk_mmap)
print "{:<32}".format("category.egl_mtrack:"),   "{:>8}".format(dps_meminfo_0.category.egl_mtrack)
print "{:<32}".format("category.gl_mtrack:"),    "{:>8}".format(dps_meminfo_0.category.gl_mtrack)
print "{:<32}".format("category.stack:"),        "{:>8}".format(dps_meminfo_0.category.stack)
print "{:<32}".format("category.gfx_dev:"),      "{:>8}".format(dps_meminfo_0.category.gfx_dev)
print "{:<32}".format("category.other_mmap:"),   "{:>8}".format(dps_meminfo_0.category.other_mmap)
print "{:<32}".format("category.jar_mmap:"),     "{:>8}".format(dps_meminfo_0.category.jar_mmap)
print "{:<32}".format("category.cursor:"),       "{:>8}".format(dps_meminfo_0.category.cursor)
print "{:<32}".format("category.other_mtrack:"), "{:>8}".format(dps_meminfo_0.category.other_mtrack)

'''





'''
print "---"
print dir(oom_adj)
print "--- Persist"
for item in oom_adj.Persistent.content.keys():
    print item, " : ", oom_adj.Persistent.content[item]
print "--- Foreground"
for item in oom_adj.Foreground.content.keys():
    print item, " : ", oom_adj.Foreground.content[item]
print "--- BService"
for item in oom_adj.BServices.content.keys():
    print item, " : ", oom_adj.BServices.content[item]
print "--- AService"
for item in oom_adj.AServices.content.keys():
    print item, " : ", oom_adj.AServices.content[item]
print "--- Cached"
for item in oom_adj.Cached.content.keys():
    print item, " : ", oom_adj.Cached.content[item]
print "--- Native"
for item in oom_adj.Native.content.keys():
    print item, " : ", oom_adj.Native.content[item]
'''
