import re;
from cBugTranslation import cBugTranslation;

aoBugTranslations = [
  # Breakpoint -> Ignored
  cBugTranslation(
    sOriginalBugTypeId = "Breakpoint",
    asOriginalTopStackFrameSymbols = [
      "*!__sanitizer_cov",
    ],
    sTranslatedBugTypeId = None, # This is apparently triggered by ASAN builds to determine EIP/RIP.
    sTranslatedBugDescription = None,
    sTranslatedSecurityImpact = None,
  ),
  # Breakpoint (hide irrelevant frames only)
  cBugTranslation(
    sOriginalBugTypeId = "Breakpoint",
    aasAdditionalIrrelevantStackFrameSymbols = [
      [
        "*!base::debug::BreakDebugger",
      ],
    ],
  ),
  # Breakpoint -> OOM
  cBugTranslation(
    sOriginalBugTypeId = "Breakpoint",
    aasOriginalTopStackFrameSymbols = [
      [
        "*!base::`anonymous namespace'::OnNoMemory",
      ], [
        "*!base::`anonymous namespace'::OnNoMemory",
      ], [
        "*!logging::LogMessage::~LogMessage",
        "*!base::`anonymous namespace'::OnNoMemory",
      ], [
        "*!logging::LogMessage::~LogMessage",
        "*!base::`anonymous namespace'::OnNoMemory",
      ], [
        "*!content::`anonymous namespace'::CrashOnMapFailure",
      ], [
        "*!base::debug::CollectGDIUsageAndDie",
        "*!skia::CreateHBitmap",
      ],
    ],
    aasAdditionalIrrelevantStackFrameSymbols = [
      [
        "*!`anonymous namespace'::Create", # Part of skia
      ],
    ],
    sTranslatedBugTypeId = "OOM",
    sTranslatedBugDescription = "The application triggered a breakpoint to indicate it was unable to allocate enough memory.",
    sTranslatedSecurityImpact = None,
  ),
  # Breakpoint -> Assert
  cBugTranslation(
    sOriginalBugTypeId = "Breakpoint",
    asOriginalTopStackFrameSymbols = [
      "*!blink::reportFatalErrorInMainThread",
      "*!v8::Utils::ReportApiFailure",
    ],
    sTranslatedBugTypeId = "Assert",
    sTranslatedBugDescription = "The application triggered a breakpoint to indicate an assertion failed.",
    sTranslatedSecurityImpact = None,
  ),
  cBugTranslation(
    sOriginalBugTypeId = "Breakpoint",
    asOriginalTopStackFrameSymbols = [
      "*!logging::LogMessage::~LogMessage",
    ],
    sTranslatedBugTypeId = "Assert",
    sTranslatedBugDescription = "The application triggered a breakpoint to indicate an assertion failed.",
    sTranslatedSecurityImpact = None,
  ),
  # AVW@NULL -> Assert
  cBugTranslation(
    sOriginalBugTypeId = "AVW@NULL",
    aasOriginalTopStackFrameSymbols = [
      [
        "*!base::win::`anonymous namespace'::ForceCrashOnSigAbort",
      ],
    ],
    sTranslatedBugTypeId = "Assert",
    sTranslatedBugDescription = "The application triggered a NULL pointer access violation to indicate an assertion failed.",
    sTranslatedSecurityImpact = None,
  ),
  # Assert -> hide irrelevant frames
  cBugTranslation(
    sOriginalBugTypeId = "Assert",
    aasAdditionalIrrelevantStackFrameSymbols = [
      [
        "*!abort",
      ], [
        "*!`anonymous namespace'::Create", # Part of skia
      ], [
        "*!blink::ReportFatalErrorInMainThread",
      ], [
        "*!blink::V8ScriptRunner::CallExtraOrCrash",
      ], [
        "*!blink::V8ScriptRunner::CallExtraOrCrash<2>",
      ], [
        "*!raise",
      ], [
        "*!sk_abort_no_print",
      ], [
        "*!v8::Utils::ApiCheck",
      ],
    ],
  ),
  # Assert -> OOM
  cBugTranslation(
    sOriginalBugTypeId = "Assert",
    aasOriginalTopStackFrameSymbols = [
      [
        "*!SkBitmap::allocPixels",
      ], [
        "*!FX_OutOfMemoryTerminate",
      ],
    ],
    sTranslatedBugTypeId = "OOM",
    sTranslatedBugDescription = "The application caused an access violation by writing to NULL to indicate it was unable to allocate enough memory.",
    sTranslatedSecurityImpact = None,
  ),
  # AVW@NULL -> OOM
  cBugTranslation(
    sOriginalBugTypeId = "AVW@NULL",
    aasOriginalTopStackFrameSymbols = [
      [
        "*!WTF::partitionOutOfMemory",
      ], [
        "*!WTF::partitionsOutOfMemoryUsingLessThan16M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing16M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing32M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing64M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing128M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing256M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing512M",
      ], [
        "*!WTF::partitionExcessiveAllocationSize",
      ],
    ],
    sTranslatedBugTypeId = "OOM",
    sTranslatedBugDescription = "The application caused an access violation by writing to NULL to indicate it was unable to allocate enough memory.",
    sTranslatedSecurityImpact = None,
  ),
  # 0xE0000008 (win::kOomExceptionCode) -> OOM
  cBugTranslation(
    sOriginalBugTypeId = "0xE0000008",
    aasOriginalTopStackFrameSymbols = [
      [
        "*!base::`anonymous namespace'::OnNoMemory",
      ], [
        "*!WTF::partitionOutOfMemory",
      ], [
        "*!WTF::partitionsOutOfMemoryUsingLessThan16M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing16M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing32M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing64M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing128M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing256M",
      ], [
        "*!WTF::partitionsOutOfMemoryUsing512M",
      ], [
        "*!WTF::partitionExcessiveAllocationSize",
      ],
    ],
    sTranslatedBugTypeId = "OOM",
    sTranslatedBugDescription = "The application caused an access violation by writing to NULL to indicate it was unable to allocate enough memory.",
    sTranslatedSecurityImpact = None,
  ),
  # OOM -> hide irrelevant frames
  cBugTranslation(
    sOriginalBugTypeId = "OOM",
    aasAdditionalIrrelevantStackFrameSymbols = [
      [
        re.compile("^.+!.+::CallNewHandler$"),
      ], [
        "*!_aligned_malloc",
      ], [
        "*!_aligned_offset_malloc_base",
      ], [
        "*!`anonymous namespace'::DefaultWinHeapMallocImpl",
      ], [
        "*!`anonymous namespace'::DefaultWinHeapReallocImpl",
      ], [
        "*!base::AlignedMalloc",
      ], [
        "*!base::allocator::WinCallNewHandler",
      ], [
        "*!base::allocator::WinHeapMalloc",
      ], [
        "*!base::PartitionAllocGenericFlags",
      ], [
        "*!base::UncheckedCalloc",
      ], [
        "*!base::UncheckedMalloc",
      ], [
        "*!blink::`anonymous namespace'::ArrayBufferAllocator::Allocate",
      ], [
        "*!ShimMalloc",
      ], [
        "*!ShimRealloc",
      ], [
        "*!sk_malloc_flags",
      ], [
        "*!sk_malloc_nothrow",
      ], [
        "*!SkBitmap::allocPixels",
      ], [
        "*!SkBitmap::allocN32Pixels",
      ], [
        "*!SkBitmap::HeapAllocator::allocPixelRef",
      ], [
        "*!SkBitmap::tryAllocPixels",
      ], [
        "*!SkMallocPixelRef::MakeAllocate",
      ], [
        "*!SkMallocPixelRef::MakeUsing",
      ], [
        "*!WTF::ArrayBufferContents::AllocateMemoryOrNull",
      ], [
        "*!WTF::ArrayBufferContents::AllocateMemoryWithFlags",
      ],
    ],
  ),
];
