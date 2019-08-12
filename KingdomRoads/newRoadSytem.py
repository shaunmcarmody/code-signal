# https://app.codesignal.com/arcade/graphs-arcade/kingdom-roads/nCMisf4ZKpDLdHevE
# https://wxtp.wordpress.com/2017/01/20/how-to-solve-newroadsystem-in-codefights/#more-2409

def newRoadSystem(roadRegister):    
    for x in range(len(roadRegister)):
        s = sum(roadRegister[x])
        ss = sum(row[x] for row in roadRegister)
        if s != ss:
            return False

    return True