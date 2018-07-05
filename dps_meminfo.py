#import os
#import subprocess as sp
import re
import oom_adj
import category
#p = sp.Popen("adb shell dumpsys -t 60 meminfo", shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
#dumpsys_meminfo = p.stdout.readlines()



        
class dps_meminfo:
    def __init__(self, process, oom_adj, category, totalram=0, freeram=0, usedram=0, lostram=0, zram=[], oom=0, restore_limit=0, high_end_gfx=0):
        self.process       = process
        self.oom_adj       = oom_adj
        self.category      = category
        self.totalram      = totalram
        self.freeram       = freeram
        self.usedram       = usedram
        self.lostram       = lostram
        self.zram          = zram
        self.oom           = oom
        self.restore_limit = restore_limit
        self.high_end_gfx  = high_end_gfx

        self.cached_pss    = 0
        self.cached_kernel = 0
        self.free          = 0

        self.used_pss      = 0
        self.kernel        = 0

        
        
    def parse_dumpsys_meminfo(self, dumpsys_meminfo):

        oom_adj = self.oom_adj
        region=''
        subregion = ''

        #print "in parse_dumpsys_meminfo..."
        
        meminfo_region = ('process','OOM adjustment','category','Total RAM','Free RAM','Used RAM','Lost RAM','ZRAM','Tuning')
        
        r_total_pss_process             = re.compile(r'Total PSS by process:');
        r_total_pss_oom_adjustment      = re.compile(r'Total PSS by OOM adjustment:');
        r_total_pss_category            = re.compile(r'Total PSS by category:')
        
        r_total_ram                     = re.compile(r'Total RAM:')
        r_free_ram                      = re.compile(r'Free RAM:')
        r_used_ram                      = re.compile(r'Used RAM:')
        r_lost_ram                      = re.compile(r'Lost RAM:')
        r_zram                          = re.compile(r'ZRAM:')
        r_tuning                        = re.compile(r'Tuning:')

        meminfo_oom_adj_subregion = {"native":'Native', "system":'System', "persist":'Persistent',
                                     "fg":'Foreground', "visible":'Visible', "perceptible":'Perceptible',
                                     "aservice":'A Service', "home":'Home', "bservice":'B Services', "cached":'Cached'}
        
        r_oom_adj_subregion_native      = re.compile(r': Native')
        r_oom_adj_subregion_system      = re.compile(r': System')
        r_oom_adj_subregion_persistent  = re.compile(r': Persistent')
        r_oom_adj_subregion_foreground  = re.compile(r': Foreground')
        r_oom_adj_subregion_visible     = re.compile(r': Visible')
        r_oom_adj_subregion_perceptable = re.compile(r': Perceptible')
        r_oom_adj_subregion_home        = re.compile(r': Home')
        r_oom_adj_subregion_a_service   = re.compile(r': A Services')
        r_oom_adj_subregion_b_service   = re.compile(r': B Services')
        r_oom_adj_subregion_cached      = re.compile(r': Cached')


        r_category_subregion_native       = re.compile(r'([0-9].*)K: Native')
        r_category_subregion_dalvik       = re.compile(r'([0-9].*)K: Dalvik')
        r_category_subregion_dexmmap      = re.compile(r'([0-9].*)K: .dex mmap')
        r_category_subregion_sommap       = re.compile(r'([0-9].*)K: .so mmap')
        r_category_subregion_unknown      = re.compile(r'([0-9].*)K: Unknown')
        r_category_subregion_oatmmap      = re.compile(r'([0-9].*)K: .oat mmap')
        r_category_subregion_artmmap      = re.compile(r'([0-9].*)K: .art mmap')
        r_category_subregion_dalvik_other = re.compile(r'([0-9].*)K: Dalvik Other')
        r_category_subregion_apkmmap      = re.compile(r'([0-9].*)K: .apk mmap')
        r_category_subregion_eglmtrack    = re.compile(r'([0-9].*)K: EGL mtrack')
        r_category_subregion_glmtrack     = re.compile(r'([0-9].*)K: GL mtrack')
        r_category_subregion_stack        = re.compile(r'([0-9].*)K: Stack')
        r_category_subregion_gfxdev       = re.compile(r'([0-9].*)K: Gfx dev')
        r_category_subregion_othermmap    = re.compile(r'([0-9].*)K: Other mmap')
        r_category_subregion_jarmmap      = re.compile(r'([0-9].*)K: .jar mmap')
        r_category_subregion_cursor       = re.compile(r'([0-9].*)K: Cursor')
        r_category_subregion_othermtrack  = re.compile(r'([0-9].*)K: Other mtrack')
        
        is_total_pss_process = False;
        for line in dumpsys_meminfo:
            #print line
            #"""
            if r_total_pss_process.search(line) is not None:
                #print "pss process"
                region = meminfo_region[0]
            #else:
                #print "not pss process"
            if r_total_pss_oom_adjustment.search(line) is not None:
                #print "pss oom adj"
                region = meminfo_region[1]
            #else:
                #print "not pss oom adj"
            if r_total_pss_category.search(line) is not None:
                region = meminfo_region[2]
            if r_total_ram.search(line) is not None:
                region = meminfo_region[3]
            if r_free_ram.search(line) is not None:
                region = meminfo_region[4]
	    if r_used_ram.search(line) is not None:
	        region = meminfo_region[5]
	    if r_lost_ram.search(line) is not None:
	        region = meminfo_region[6]
	    if r_zram.search(line) is not None:
	        region = meminfo_region[7]
	    if r_tuning.search(line) is not None:
	        region = meminfo_region[8]
	    
	    if region == 'OOM adjustment':
	        line = line.replace(",","")
            #"""
            
	        #print line,
                #print "---------- in region OOM adjustment"
                if r_oom_adj_subregion_native.search(line) is not None:
                    #print "tagA:",line,
		    subregion = meminfo_oom_adj_subregion["native"]
                    #print subregion
		    oom_adj.Native.Total = int(re.search(r'([0-9]*)K: Native',line).group(1).strip())
		    #print "oom_adj.Native", oom_adj.Native.Total
	
	        if r_oom_adj_subregion_system.search(line) is not None:
		    subregion = meminfo_oom_adj_subregion["system"]
	            oom_adj.System.Total = re.search(r'([0-9]*)K: System',line).group(1)
		    #print "oom_adj.System", oom_adj.System.Total

	        if r_oom_adj_subregion_persistent.search(line) is not None:
	            subregion = meminfo_oom_adj_subregion["persist"]
		    oom_adj.Persistent.Total = re.search(r'([0-9]*)K: Persistent',line).group(1)
		    #print "oom_adj.Persistent", oom_adj.Persistent.Total
			
	        if r_oom_adj_subregion_foreground.search(line) is not None:
		    subregion = meminfo_oom_adj_subregion["fg"]
		    oom_adj.Foreground.Total = re.search(r'([0-9]*)K: Foreground',line).group(1)
		    #print "oom_adj.Foreground", oom_adj.Foreground.Total
				
	        if r_oom_adj_subregion_visible.search(line) is not None:
		    subregion = meminfo_oom_adj_subregion["visible"]
		    oom_adj.Visible.Total = re.search(r'([0-9]*)K: Visible',line).group(1)
		    #print "oom_adj.Visible", oom_adj.Visible.Total
				
	        if r_oom_adj_subregion_perceptable.search(line) is not None:
		    subregion = meminfo_oom_adj_subregion["perceptible"]
		    oom_adj.Perceptible.Total = re.search(r'([0-9]*)K: Perceptible',line).group(1)
		    #print "oom_adj.Perceptible", oom_adj.Perceptible.Total

	        if r_oom_adj_subregion_a_service.search(line) is not None:
		    subregion = meminfo_oom_adj_subregion["aservice"]
		    oom_adj.AServices.Total = re.search(r'([0-9]*)K: A Services',line).group(1)
		    #print "oom_adj.AServices", oom_adj.AServices.Total                    
                    
	        if r_oom_adj_subregion_home.search(line) is not None:
		    subregion = meminfo_oom_adj_subregion["home"]
		    oom_adj.Home.Total = re.search(r'([0-9]*)K: Home',line).group(1)
		    #print "oom_adj.Home", oom_adj.Home.Total
                    
	        if r_oom_adj_subregion_b_service.search(line) is not None:
		    subregion = meminfo_oom_adj_subregion["bservice"]
		    oom_adj.BServices.Total = re.search(r'([0-9]*)K: B Services',line).group(1)
		    #print "oom_adj.BServices", oom_adj.BServices.Total
				
	        if r_oom_adj_subregion_cached.search(line) is not None:
                    #print "tagA:"
		    subregion = meminfo_oom_adj_subregion["cached"]
		    oom_adj.Cached.Total = re.search(r'([0-9]*)K: Cached',line).group(1)
		    #print "oom_adj.Cached", oom_adj.Cached.Total
                    #print "subregion ---", subregion
				
	    else:
	        subregion = ''


            if region == 'process':
                line = line.replace(",","")
                #print line
                pattern = re.compile(r'([0-9].*)K: (.*)')
                if pattern.search(line) is not None:
                    self.process[pattern.search(line).group(2).strip()] = int(pattern.search(line).group(1))/1024
            #"""
            #print "tagA ", region, subregion
	    if region == 'OOM adjustment' and subregion == 'Native':
                #print "in Native subregion...."
                if len(line) > 1 :
	            if oom_adj.Native.count != 0:
                        #print "calling append_list ...... "
		        oom_adj.Native.append_list(line)
	            oom_adj.Native.count = oom_adj.Native.count + 1
	    if region == 'OOM adjustment' and subregion == 'System':
                if len(line) > 1 :
	            if oom_adj.System.count != 0:
	                oom_adj.System.append_list(line)
	            oom_adj.System.count = oom_adj.System.count + 1
	    if region == 'OOM adjustment' and subregion == 'Persistent':
                if len(line) > 1 :
	            if oom_adj.Persistent.count != 0 and re.compile('Persistent').search(line) is None:
		        oom_adj.Persistent.append_list(line)
	            oom_adj.Persistent.count = oom_adj.Persistent.count + 1
	    if region == 'OOM adjustment' and subregion == 'Foreground':
                if len(line) > 1 :
	            if oom_adj.Foreground.count != 0:
		        oom_adj.Foreground.append_list(line)
	            oom_adj.Foreground.count = oom_adj.Foreground.count + 1
	    if region == 'OOM adjustment' and subregion == 'Visible':
                if len(line) > 1 :
	            if oom_adj.Visible.count != 0:
		        oom_adj.Visible.append_list(line)
	            oom_adj.Visible.count = oom_adj.Visible.count + 1

	    if region == 'OOM adjustment' and subregion == 'Perceptible':
                if len(line) > 1 :
	            if oom_adj.Perceptible.count != 0:
		        oom_adj.Perceptible.append_list(line)
	            oom_adj.Perceptible.count = oom_adj.Perceptible.count + 1

	    if region == 'OOM adjustment' and subregion == 'Home':
                if len(line) > 1 :
	            if oom_adj.Home.count != 0:
		        oom_adj.Home.append_list(line)
	            oom_adj.Home.count = oom_adj.Home.count + 1
                
	    if region == 'OOM adjustment' and subregion == 'B Services':
                if len(line) > 1 :
	            if oom_adj.BServices.count != 0:
		        oom_adj.BServices.append_list(line)
	            oom_adj.BServices.count = oom_adj.BServices.count + 1
	    if region == 'OOM adjustment' and subregion == 'Cached':
	        if len(line) > 1 :
		    if oom_adj.Cached.count != 0:
		        oom_adj.Cached.append_list(line)
		    oom_adj.Cached.count = oom_adj.Cached.count + 1


            if region == 'category':
                if len(line) > 1 :
                    #print line,
                    line = line.replace(",","")
                    #print line,
                    if r_category_subregion_native.search(line) is not None:
                        self.category.Native = r_category_subregion_native.search(line).group(1).strip()
                    if r_category_subregion_dalvik.search(line) is not None:
                        self.category.Dalvik = r_category_subregion_dalvik.search(line).group(1).strip()
                    if r_category_subregion_dexmmap.search(line) is not None:
                        self.category.dex_mmap = r_category_subregion_dexmmap.search(line).group(1).strip()
                    if r_category_subregion_sommap.search(line) is not None:
                        self.category.so_mmap = r_category_subregion_sommap.search(line).group(1).strip()
                    if r_category_subregion_unknown.search(line) is not None:
                        self.category.unknown = r_category_subregion_unknown.search(line).group(1).strip()
                    if r_category_subregion_oatmmap.search(line) is not None:
                        self.category.oat_mmap = r_category_subregion_oatmmap.search(line).group(1).strip()
                    if r_category_subregion_artmmap.search(line) is not None:
                        self.category.art_mmap = r_category_subregion_artmmap.search(line).group(1).strip()
                    if r_category_subregion_dalvik_other.search(line) is not None:
                        self.category.dalvik_other = r_category_subregion_dalvik_other.search(line).group(1).strip()
                    if r_category_subregion_apkmmap.search(line) is not None:
                        self.category.apk_mmap = r_category_subregion_apkmmap.search(line).group(1).strip()
                    if r_category_subregion_eglmtrack.search(line) is not None:
                        self.category.egl_mtrack = r_category_subregion_eglmtrack.search(line).group(1).strip()
                    if r_category_subregion_glmtrack.search(line) is not None:
                        self.category.gl_mtrack = r_category_subregion_glmtrack.search(line).group(1).strip()
                    if r_category_subregion_stack.search(line) is not None:
                        #print line
                        self.category.stack = r_category_subregion_stack.search(line).group(1).strip()
                    if r_category_subregion_gfxdev.search(line) is not None:
                        self.category.gfx_dev = r_category_subregion_gfxdev.search(line).group(1).strip()
                    if r_category_subregion_othermmap.search(line) is not None:
                        self.category.other_mmap = r_category_subregion_othermmap.search(line).group(1).strip()
                    if r_category_subregion_jarmmap.search(line) is not None:
                        #print line
                        self.category.jar_mmap = r_category_subregion_jarmmap.search(line).group(1).strip()
                    if r_category_subregion_cursor.search(line) is not None:
                        #print line
                        self.category.cursor = r_category_subregion_cursor.search(line).group(1).strip()
                    if r_category_subregion_othermtrack.search(line) is not None:
                        #print line
                        self.category.other_mtrack = r_category_subregion_othermtrack.search(line).group(1).strip()

            line = line.replace(",","").strip()

            #print line,
            if region == 'Total RAM':
                pattern = re.compile(r'Total RAM:.*?([0-9].*)K ')
                #print line
                #print "Total RAM", "---", pattern.search(line).group(1)
                if pattern.search(line) is not None:
                    self.totalram = int(pattern.search(line).group(1).strip())
                else:
                    print "Total RAM parse failure"
                    exit()
                    #print "----------------------"
            if region == 'Free RAM':
                #print line
                pattern = re.compile(r'Free RAM: .*?([0-9].*)K.*?([0-9].*)K cached pss +.*?([0-9].*)K cached kernel +.*?([0-9].*)K free.*')
                #print "{:<16}".format(" Free RAM"),      "---", pattern.search(line).group(1)
                #print "{:<16}".format(" cached pss"),    "---", pattern.search(line).group(2)
                #print "{:<16}".format(" cached kernel"), "---", pattern.search(line).group(3)
                #print "{:<16}".format(" free         "), "---", pattern.search(line).group(4)
                if pattern.search(line) is not None:
                    self.freeram       = int(pattern.search(line).group(1).strip())
                    self.cached_pss    = int(pattern.search(line).group(2).strip())
                    self.cached_kernel = int(pattern.search(line).group(3).strip())
                    self.free          = int(pattern.search(line).group(4).strip())
                else:
                    print "Free RAM parse failure"
                    exit()
                    #print "----------------------"
            if region == 'Used RAM':
                #print line
                #print "---"
                pattern = re.compile(r'Used RAM:.*?([0-9].*)K.*?([0-9].*)K used pss +.*?([0-9].*)K kernel.*')
                if pattern.search(line) is not None:
                    #print "{:<16}".format(" Used RAM"),      "---", pattern.search(line).group(1)
                    #print "{:<16}".format(" used pss"),      "---", pattern.search(line).group(2)
                    #print "{:<16}".format(" kernel"),        "---", pattern.search(line).group(3)
                    self.usedram  = int(pattern.search(line).group(1).strip())
                    self.used_pss = int(pattern.search(line).group(2).strip())
                    self.kernel   = int(pattern.search(line).group(3).strip())
                else:
                    print "Used RAM parse failure"
                    exit()
            if region == 'Lost RAM':
                #print line
                #print "---"
                pattern = re.compile(r'Lost RAM:.*?([-0-9].*)K.*')
                if pattern.search(line) is not None:
                    #print "{:<16}".format("Lost RAM"), "---", pattern.search(line).group(1)
                    self.lostram = int(pattern.search(line).group(1).strip())
                else:
                    print "Lost RAM Parse failure!"
                    exit()

            if region == 'ZRAM':
                #print line
                pattern = re.compile(r'ZRAM:.*?([0-9].*)K physical used for.*?([0-9].*)K in swap \(.*?([0-9].*)K total swap\)')
                #ZRAM:       72084K physical used for      228080K in swap (    546368K total swap)
                if pattern.search(line) is not None:
                    #print "pattern.search(line).group(1)",pattern.search(line).group(1), int(pattern.search(line).group(1))
                    #print "pattern.search(line).group(2)",pattern.search(line).group(2), int(pattern.search(line).group(2))
                    #print "pattern.search(line).group(3)",pattern.search(line).group(3), int(pattern.search(line).group(3))
                    self.zram = [int(pattern.search(line).group(1)), int(pattern.search(line).group(2)), int(pattern.search(line).group(3))]
                else:
                    print line
                    print "ZRAM error parsed"
                    exit()
            if region == 'Tuning':
                #print line
                pattern = re.compile(r'Tuning:.*?([0-9].*)\(large.*\) oom .*?([0-9].*)K restore limit .*?([0-9].*)K.*')
                #print "{:<16}".format("oom"),           "---", pattern.search(line).group(1)
                #print "{:<16}".format("restore limit"), "---", pattern.search(line).group(2)
                #print "{:<16}".format("hight-eng-gfx"), "---", pattern.search(line).group(3)
                self.oom           = pattern.search(line).group(1)
                self.restore_limit = pattern.search(line).group(2)
                self.high_end_gfx  = pattern.search(line).group(3)
                
            #"""
	    #print "region:", region ,
	    #print "subregion:", subregion       

            

#dps_meminfo = DPS_MEMINFO(OOM_ADJ())
#dps_meminfo.parse_dumpsys_meminfo(dumpsys_meminfo)
#retval = p.wait()
