#!/usr/bin/python
import re


class proc_meminfo:
    def __init__(self):
        self.MemTotal       = 0
        self.MemFree        = 0
        self.MemAvailable   = 0
        self.Buffers        = 0
        self.Cached         = 0
        self.SwapCached     = 0
        self.Active         = 0
        self.Inactive       = 0
        self.Active_anon    = 0
        self.Inactive_anon  = 0
        self.Active_file    = 0
        self.Inactive_file  = 0
        self.Unevictable    = 0
        self.Mlocked        = 0
        self.HighTotal      = 0
        self.HighFree       = 0
        self.LowTotal       = 0
        self.LowFree        = 0
        self.SwapTotal      = 0
        self.SwapFree       = 0
        self.Dirty          = 0
        self.Writeback      = 0
        self.AnonPages      = 0
        self.Mapped         = 0
        self.Shmem          = 0
        self.Slab           = 0
        self.SReclaimable   = 0
        self.SUnreclaim     = 0
        self.KernelStack    = 0
        self.PageTables     = 0
        self.NFS_Unstable   = 0
        self.Bounce         = 0
        self.WritebackTmp   = 0
        self.CommitLimit    = 0
        self.Committed      = 0
        self.VmallocTotal   = 0
        self.VmallocUsed    = 0
        self.VmallocChunk   = 0
        self.CmaTotal       = 0
        self.CmaFree        = 0


        
    def parse_proc_meminfo(self, meminfo):
        r_MemTotal       = re.compile(r'MemTotal:')
        r_MemFree        = re.compile(r'MemFree:')
        r_MemAvailable   = re.compile(r'MemAvailable:')
        r_Buffers        = re.compile(r'Buffers:')
        r_Cached         = re.compile(r'^Cached:')
        r_SwapCached     = re.compile(r'SwapCached:')
        r_Active         = re.compile(r'Active:')
        r_Inactive       = re.compile(r'Inactive:')
        r_Active_anon    = re.compile(r'Active\(anon\):')
        r_Inactive_anon  = re.compile(r'Inactive\(anon\):')
        r_Active_file    = re.compile(r'Active\(file\):')
        r_Inactive_file  = re.compile(r'Inactive\(file\):')
        r_Unevictable    = re.compile(r'Unevictable:')
        r_Mlocked        = re.compile(r'Mlocked:')
        r_HighTotal      = re.compile(r'HighTotal:')
        r_HighFree       = re.compile(r'HighFree:')
        r_LowTotal       = re.compile(r'LowTotal:')
        r_LowFree        = re.compile(r'LowFree:')
        r_SwapTotal      = re.compile(r'SwapTotal:')
        r_SwapFree       = re.compile(r'SwapFree:')
        r_Dirty          = re.compile(r'Dirty:')
        r_Writeback      = re.compile(r'Writeback:')
        r_AnonPages      = re.compile(r'AnonPages:')
        r_Mapped         = re.compile(r'Mapped:')
        r_Shmem          = re.compile(r'Shmem:')
        r_Slab           = re.compile(r'Slab:')
        r_SReclaimable   = re.compile(r'SReclaimable:')
        r_SUnreclaim     = re.compile(r'SUnreclaim:')
        r_KernelStack    = re.compile(r'KernelStack:')
        r_PageTables     = re.compile(r'PageTables:')
        r_NFS_Unstable   = re.compile(r'NFS_Unstable:')
        r_Bounce         = re.compile(r'Bounce:')
        r_WritebackTmp   = re.compile(r'WritebackTmp:')
        r_CommitLimit    = re.compile(r'CommitLimit:')
        r_Committed      = re.compile(r'Committed_AS:')
        r_VmallocTotal   = re.compile(r'VmallocTotal:')
        r_VmallocUsed    = re.compile(r'VmallocUsed:')
        r_VmallocChunk   = re.compile(r'VmallocChunk:')
        r_CmaTotal       = re.compile(r'CmaTotal:')
        r_CmaFree        = re.compile(r'CmaFree:')

        
        for line in meminfo:
            #print line,
            if r_MemTotal.search(line) is not None:
                self.MemTotal = re.compile(r'MemTotal: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_MemFree.search(line) is not None:
                self.MemFree = re.compile(r'MemFree: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_MemAvailable.search(line) is not None:
                self.MemAvailable = re.compile(r'MemAvailable: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Buffers.search(line) is not None:
                self.Buffers = re.compile(r'Buffers: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Cached.search(line) is not None:
                self.Cached = re.compile(r'Cached: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_SwapCached.search(line) is not None:
                self.SwapCached = re.compile(r'SwapCached: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Active.search(line) is not None:
                self.Active = re.compile(r'Active: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Inactive.search(line) is not None:
                self.Inactive =  re.compile(r'Inactive: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Active_anon.search(line) is not None:
                self.Active_anon = re.compile(r'Active\(anon\): .*?([0-9].*) kB').search(line).group(1).strip()
            if r_Inactive_anon.search(line) is not None:
                self.Inactive_anon = re.compile(r'Inactive\(anon\): .*?([0-9].*) kB').search(line).group(1).strip()
            if r_Active_file.search(line) is not None:
                self.Active_file = re.compile(r'Active\(file\): .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Inactive_file.search(line) is not None:
                self.Inactive_file = re.compile(r'Inactive\(file\): .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Unevictable.search(line) is not None:
                self.Unevictable = re.compile(r'Unevictable: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Mlocked.search(line) is not None:
                self.Mlocked = re.compile(r'Mlocked: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_HighTotal.search(line) is not None:
                self.HighTotal = re.compile(r'HighTotal: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_HighFree.search(line) is not None:
                self.HighFree = re.compile(r'HighFree: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_LowTotal.search(line) is not None:
                self.LowTotal = re.compile(r'LowTotal: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_LowFree.search(line) is not None:
                self.LowFree = re.compile(r'LowFree: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_SwapTotal.search(line) is not None:
                self.SwapTotal = re.compile(r'SwapTotal: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_SwapFree.search(line) is not None:
                self.SwapFree = re.compile(r'SwapFree: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Dirty.search(line) is not None:
                self.Dirty = re.compile(r'Dirty: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Writeback.search(line) is not None:
                self.Writeback = re.compile(r'Writeback: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_AnonPages.search(line) is not None:
                self.AnonPages = re.compile(r'AnonPages: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Mapped.search(line) is not None:
                self.Mapped = re.compile(r'Mapped: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Shmem.search(line) is not None:
                self.Shmem = re.compile(r'Shmem: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Slab.search(line) is not None:
                self.Slab = re.compile(r'Slab: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_SReclaimable.search(line) is not None:
                self.SReclaimable = re.compile(r'SReclaimable: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_SUnreclaim.search(line) is not None:
                self.SUnreclaim = re.compile(r'SUnreclaim: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_KernelStack.search(line) is not None:
                self.KernelStack = re.compile(r'KernelStack: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_PageTables.search(line) is not None:
                self.PageTables = re.compile(r'PageTables: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_NFS_Unstable.search(line) is not None:
                self.NFS_Unstable = re.compile(r'NFS_Unstable: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Bounce.search(line) is not None:
                self.Bounce = re.compile(r'Bounce: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_WritebackTmp.search(line) is not None:
                self.WritebackTmp = re.compile(r'WritebackTmp: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_CommitLimit.search(line) is not None:
                self.CommitLimit = re.compile(r'CommitLimit: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_Committed.search(line) is not None:
                self.Committed = re.compile(r'Committed_AS: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_VmallocTotal.search(line) is not None:
                self.VmallocTotal = re.compile(r'VmallocTotal: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_VmallocUsed.search(line) is not None:
                self.VmallocUsed = re.compile(r'VmallocUsed: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_VmallocChunk.search(line) is not None:
                self.VmallocChunk = re.compile(r'VmallocChunk: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_CmaTotal.search(line) is not None:
                self.CmaTotal = re.compile(r'CmaTotal: .*?([0-9].*)kB').search(line).group(1).strip()
            if r_CmaFree.search(line) is not None:
                self.CmaFree = re.compile(r'CmaFree: .*?([0-9].*)kB').search(line).group(1).strip()
        return self
