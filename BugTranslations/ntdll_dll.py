import re;
from cBugTranslation import cBugTranslation;

aoBugTranslations = [
  # These frames are never relevant
  cBugTranslation(
    aasAdditionalIrrelevantStackFrameSymbols = [
      [
        "ntdll.dll!DbgBreakPoint",
      ],
    ],
  ),
  # Breakpoint -> HeapCorrupt
  cBugTranslation(
    sOriginalBugTypeId = "Breakpoint",
    aasOriginalTopStackFrameSymbols = [
      [
        "ntdll.dll!RtlReportCriticalFailure",
        "ntdll.dll!RtlpHeapHandleError",
      ], [
        "ntdll.dll!RtlpBreakPointHeap",
      ],
    ],
    sTranslatedBugTypeId = "HeapCorrupt",
    sTranslatedBugDescription = "A breakpoint was triggered to indicate heap corruption was detected",
    sTranslatedSecurityImpact = "This is probably an exploitable security issue",
  ),
  # AVR@Reserved -> AVR@CFG
  cBugTranslation(
    sOriginalBugTypeId = "AVR@Reserved",
    aasOriginalTopStackFrameSymbols = [
      [
        "ntdll.dll!LdrpDispatchUserCallTarget",
      ], [
        "ntdll.dll!LdrpValidateUserCallTargetBitMapCheck",
      ], [
        "ntdll.dll!LdrpValidateUserCallTarget",
      ],
    ],
    sTranslatedBugTypeId = "AVR@CFG",
    sTranslatedBugDescription = "The process attempted to call a function using an invalid function pointer, " \
        "which caused an acces violation exception in Control Flow Guard. This is often caused by a NULL pointer.",
    sTranslatedSecurityImpact = "Unlikely to be an exploitable security issue, unless you can control the invalid function pointer",
  ),
  # OOM, HeapCorrupt, DoubleFree, MisalignedFree, OOBW -> hide irrelevant frames
  cBugTranslation(
    sOriginalBugTypeId = re.compile(r"^(OOM|HeapCorrupt|DoubleFree\[.*|MisalignedFree\[.*|OOBW\[.*)$"),
    aasAdditionalIrrelevantStackFrameSymbols = [
      [
        "ntdll.dll!DbgUiRemoteBreakin",
      ], [
        "ntdll.dll!FindNodeOrParent",
      ], [
        "ntdll.dll!RtlAllocateHeap",
      ], [
        "ntdll.dll!RtlDebugAllocateHeap",
      ], [
        "ntdll.dll!RtlDebugFreeHeap",
      ], [
        "ntdll.dll!RtlDeleteCriticalSection",
      ], [
        "ntdll.dll!RtlFreeHeap",
      ], [
        "ntdll.dll!RtlInsertElementGenericTableAvl",
      ], [
        "ntdll.dll!RtlpAllocateHeap",
      ], [
        "ntdll.dll!RtlpAllocateHeapInternal",
      ], [
        "ntdll.dll!RtlpAllocateHeapRaiseException",
      ], [
        "ntdll.dll!RtlpFreeDebugInfo",
      ], [
        "ntdll.dll!RtlpFreeHeap",
      ],
    ],
  ),
];