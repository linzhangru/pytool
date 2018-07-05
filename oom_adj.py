import re

class BLOCK:
    def __init__(self, Total=0, content={}, count=0):
        self.Total = Total
        self.content  = content
        self.count = count
        
    def append_list(self, line):
        #print line, "in append_list"
        #if len(strip(line)):
        #    print "line is printable", len(strip(line))
        #else:
        #    print "line is not printable"
        line = line.replace(",","").replace("K:","K:")
        pattern = re.compile(r'([0-9].*)K:(.*)')
        item = pattern.search(line)
        if item is not None:
            key = pattern.search(line).group(2).strip()
            self.content[key] = pattern.search(line).group(1)
            #print self.content[key],"---", key


class oom_adj:
    def __init__(self,
                 Native=0, System=0, Persistent=0,
                 Foreground=0, Visible=0, Perceptible=0,
                 AServices=0, Home=0, BServices=0, Cached=0):
        self.Native      = BLOCK(Native, {})
        self.System      = BLOCK(System, {})
        self.Persistent  = BLOCK(Persistent,{})
        self.Foreground  = BLOCK(Foreground,{})
        self.Visible     = BLOCK(Visible,{})
        self.Perceptible = BLOCK(Perceptible,{})
        self.AServices   = BLOCK(AServices,{})        
        self.Home        = BLOCK(Home,{})
        self.BServices   = BLOCK(BServices,{})
        self.Cached      = BLOCK(Cached,{})
