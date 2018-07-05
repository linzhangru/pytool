

class category:
    def __init__(self,
                 Native     = 0, Dalvik       = 0, dex_mmap = 0,
                 so_mmap    = 0, unknown      = 0, oat_mmap = 0,
                 art_mmap   = 0, dalvik_other = 0, apk_mmap = 0,
                 egl_mtrack = 0, gl_mtrack    = 0, stack    = 0,
                 gfx_dev    = 0, other_mmap   = 0, jar_mmap = 0,
                 cursor     = 0, other_mtrack = 0):
        self.Native        = Native
        self.Dalvik        = Dalvik
        self.dex_mmap      = dex_mmap
        self.so_mmap       = so_mmap
        self.unknown       = unknown
        self.oat_mmap      = oat_mmap
        self.art_mmap      = art_mmap
        self.dalvik_other  = dalvik_other
        self.apk_mmap      = apk_mmap
        self.egl_mtrack    = egl_mtrack
        self.gl_mtrack     = gl_mtrack
        self.stack         = stack
        self.gfx_dev       = gfx_dev
        self.other_mmap    = other_mmap
        self.jar_mmap      = jar_mmap
        self.cursor        = cursor
        self.other_mtrack  = other_mtrack
