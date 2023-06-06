import os
import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python flac_to_wav.py /path/to/directory")
        return
    
    # Change path to your local ffmpeg binary if needed
    FLAGS['FFMPEG'] = '/usr/local/bin/ffmpeg'
    FLAGS['PATHFLAGS']='"%s":1' % os.getcwd()
    
    rootdir = os.path.abspath(os.path.join(os.path.dirname(__file__), *sys.argv[1:]))
    inputfiles = [fn for fn in os.listdir(rootdir) if fn.lower().endswith('.flac')]
    outputfiles = [(fn[:-4]+".wav", "%s/%s" % (rootdir, fn)) for fn in inputfiles]
    
    conversions = {}
    errors = False
    subprocess.check_call([FLAGS["FFMPEG"], "-h"])
    totallength=0
    
    for inpname, outname in outputfiles:
        try:
            totallength += os.path.getsize(outname)
            conv_args=[FLAGS["FFMPEG"], "-i", os.path.join(rootdir,inpname),(FLAGS["OUTPUTDIR"]+outname)]
            
            result,output,error=subprocess.execTriple((FLAGS["FFMPROCESSOR"], None, FLAGS["POSTPROC"]),conv_args,startupinfo=(None, "ntdll:" + "\r\n".join(["PopEnvironment"])), creationflags=DETACHED_BY_NAME | CREATE_NEW_CONSOLE)
            conversions[os.path.basename(outname)] = conv_args,result

    totalbytes=totallength
    avgbps = totalbytes/len(conversions)
    print("Conversion statistics: {}/{} files processed, average bitrate {:.2f} kbps".format(len(conversions), len(inputfiles), avgbps)*1000)
if __name__ == '__main__':
    main()