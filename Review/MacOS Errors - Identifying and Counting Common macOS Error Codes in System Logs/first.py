def get_log_text():
    return """error 19:30:12.883436+0200 tccd Failed to copy signing info for 15059,
responsible for file:///Applications/ActivityWatch.app/Contents/MacOS/aw-qt:
#-67062: Error Domain=NSOSStatusErrorDomain Code=-67062 "(null)"
error 19:30:12.899487+0200 tccd cannot open file at line 43353 of [378230ae7f]
error 19:30:12.899530+0200 tccd os_unix.c:43353: (2)
open(/var/db/DetachedSignatures) - No such file or directory
error 19:30:12.941205+0200 runningboardd Launchd failed to get information for
pid 15088, failed with error Error Domain=NSPOSIXErrorDomain Code=113 "Unknown
error: 113"
error 19:30:13.364804+0200 System Events ERROR: Failed to create a desc with
expected type (is 'long' should be 'comp')
error 19:30:13.500082+0200 taskgated cannot open file at line 43353 of
[378230ae7f]
error 19:30:13.500129+0200 taskgated os_unix.c:43353: (2)
open(/var/db/DetachedSignatures) - No such file or directory
error 19:30:13.509382+0200 taskgated cannot open file at line 43353 of
[378230ae7f]
error 19:30:13.509438+0200 taskgated os_unix.c:43353: (2)
open(/var/db/DetachedSignatures) - No such file or directory
error 19:30:14.161766+0200 diagnostics_agent Invalid receipt [0 bytes] --
[<private>]
error 19:30:15.684412+0200 tccd FAIL: PID[15059]:
SecTaskCopySigningIdentifier(): [22: Invalid argument]
error 19:30:15.685102+0200 tccd FAIL: PID[15059]:
SecTaskCopySigningIdentifier(): [22: Invalid argument]
error 19:30:15.688060+0200 tccd cannot open file at line 43353 of [378230ae7f]
error 19:30:15.688105+0200 tccd os_unix.c:43353: (2)
open(/var/db/DetachedSignatures) - No such file or directory
error 19:30:15.689264+0200 tccd FAIL: PID[15059]:
SecTaskCopySigningIdentifier(): [22: Invalid argument]
error 19:30:15.691828+0200 tccd cannot open file at line 43353 of [378230ae7f]
error 19:30:15.691870+0200 tccd os_unix.c:43353: (2)
open(/var/db/DetachedSignatures) - No such file or directory
error 19:30:15.702193+0200 tccd FAIL: PID[15059]:
SecTaskCopySigningIdentifier(): [22: Invalid argument]
error 19:30:15.703293+0200 tccd FAIL: PID[15059]:
SecTaskCopySigningIdentifier(): [22: Invalid argument]
error 19:30:15.705486+0200 tccd cannot open file at line 43353 of [378230ae7f]
error 19:30:15.705537+0200 tccd os_unix.c:43353: (2)
open(/var/db/DetachedSignatures) - No such file or directory
error 19:30:15.707026+0200 tccd FAIL: PID[15059]:
SecTaskCopySigningIdentifier(): [22: Invalid argument]
error 19:30:15.709124+0200 tccd cannot open file at line 43353 of [378230ae7f]
error 19:30:15.709176+0200 tccd os_unix.c:43353: (2)
open(/var/db/DetachedSignatures) - No such file or directory
error 19:30:15.760375+0200 tccd FAIL: PID[15059]:
SecTaskCopySigningIdentifier(): [22: Invalid argument]
error 19:30:15.760977+0200 tccd FAIL: PID[15059]:
SecTaskCopySigningIdentifier(): [22: Invalid argument]
error 19:30:15.763766+0200 tccd cannot open file at line 43353 of [378230ae7f]
error 19:30:15.763808+0200 tccd os_unix.c:43353: (2)
open(/var/db/DetachedSignatures) - No such file or directory
error 19:30:15.766876+0200 tccd Failed to copy signing info for 15059,
responsible for file:///Applications/ActivityWatch.app/Contents/MacOS/aw-qt:
#-67062: Error Domain=NSOSStatusErrorDomain Code=-67062 "(null)"
error 19:30:15.772967+0200 tccd cannot open file at line 43353 of [378230ae7f]
error 19:30:15.773006+0200 tccd os_unix.c:43353: (2)
open(/var/db/DetachedSignatures) - No such file or directory
error 19:30:15.788297+0200 runningboardd Launchd failed to get information for
pid 15093, failed with error Error Domain=NSPOSIXErrorDomain Code=113 "Unknown
error: 113"
error 19:30:16.129523+0200 System Events ERROR: Failed to create a desc with
expected type (is 'long' should be 'comp')
error 19:30:16.803123+0200 diagnostics_agent Invalid receipt [0 bytes] --
[<private>]"""


if __name__ == "__main__":
    print(get_log_text()[:500])
