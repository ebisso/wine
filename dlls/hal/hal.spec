@ stdcall -arch=i386 -norelay ExAcquireFastMutex(ptr)
@ stdcall -arch=i386 -norelay ExReleaseFastMutex(ptr)
@ stdcall -arch=i386 -norelay ExTryToAcquireFastMutex(ptr)
@ stub HalClearSoftwareInterrupt
@ stub HalRequestSoftwareInterrupt
@ stub HalSystemVectorDispatchEntry
@ stdcall -arch=i386 -norelay KeAcquireInStackQueuedSpinLock(ptr ptr)
@ stub KeAcquireInStackQueuedSpinLockRaiseToSynch
@ stub KeAcquireQueuedSpinLock
@ stub KeAcquireQueuedSpinLockRaiseToSynch
@ stub KeAcquireSpinLockRaiseToSynch
@ stdcall -arch=i386 -norelay KeReleaseInStackQueuedSpinLock(ptr)
@ stub KeReleaseQueuedSpinLock
@ stub KeTryToAcquireQueuedSpinLock
@ stub KeTryToAcquireQueuedSpinLockRaiseToSynch
@ stdcall -arch=i386 -norelay KfAcquireSpinLock(ptr)
@ stdcall -arch=arm,arm64,i386 -norelay KfLowerIrql(long)
@ stdcall -arch=arm,arm64,i386 -norelay KfRaiseIrql(long)
@ stdcall -arch=i386 -norelay KfReleaseSpinLock(ptr long)
@ stub HalAcquireDisplayOwnership
@ stub HalAdjustResourceList
@ stub HalAllProcessorsStarted
@ stub HalAllocateAdapterChannel
@ stub HalAllocateCommonBuffer
@ stub HalAllocateCrashDumpRegisters
@ stub HalAssignSlotResources
@ stub HalBeginSystemInterrupt
@ stub HalCalibratePerformanceCounter
@ stub HalDisableSystemInterrupt
@ stub HalDisplayString
@ stub HalEnableSystemInterrupt
@ stub HalEndSystemInterrupt
@ stub HalFlushCommonBuffer
@ stub HalFreeCommonBuffer
@ stub HalGetAdapter
@ stdcall HalGetBusData(long long long ptr long)
@ stdcall HalGetBusDataByOffset(long long long ptr long long)
@ stub HalGetEnvironmentVariable
@ stub HalGetInterruptVector
@ stub HalHandleNMI
@ stub HalInitSystem
@ stub HalInitializeProcessor
@ stub HalMakeBeep
@ stub HalProcessorIdle
@ stub HalQueryDisplayParameters
@ stub HalQueryRealTimeClock
@ stub HalReadDmaCounter
@ stub HalReportResourceUsage
@ stub HalRequestIpi
@ stub HalReturnToFirmware
@ stub HalSetBusData
@ stub HalSetBusDataByOffset
@ stub HalSetDisplayParameters
@ stub HalSetEnvironmentVariable
@ stub HalSetProfileInterval
@ stub HalSetRealTimeClock
@ stub HalSetTimeIncrement
@ stub HalStartNextProcessor
@ stub HalStartProfileInterrupt
@ stub HalStopProfileInterrupt
@ stdcall HalTranslateBusAddress(long long int64 ptr ptr)
@ stub IoAssignDriveLetters
@ stub IoFlushAdapterBuffers
@ stub IoFreeAdapterChannel
@ stub IoFreeMapRegisters
@ stub IoMapTransfer
@ stub IoReadPartitionTable
@ stub IoSetPartitionInformation
@ stub IoWritePartitionTable
@ stub KdComPortInUse
@ stdcall -arch=i386 KeAcquireSpinLock(ptr ptr)
@ stub KeFlushWriteBuffer
@ stdcall -arch=arm,arm64,i386 KeGetCurrentIrql()
@ stub KeLowerIrql
@ stdcall -ret64 KeQueryPerformanceCounter(ptr)
@ stub KeRaiseIrql
@ stub KeRaiseIrqlToDpcLevel
@ stub KeRaiseIrqlToSynchLevel
@ stdcall -arch=i386 KeReleaseSpinLock(ptr long)
@ stub KeStallExecutionProcessor
@ stub READ_PORT_BUFFER_UCHAR
@ stub READ_PORT_BUFFER_ULONG
@ stub READ_PORT_BUFFER_USHORT
@ stdcall -arch=arm,arm64,i386 READ_PORT_UCHAR(ptr)
@ stdcall -arch=arm,arm64,i386 READ_PORT_ULONG(ptr)
@ stub READ_PORT_USHORT
@ stub WRITE_PORT_BUFFER_UCHAR
@ stub WRITE_PORT_BUFFER_ULONG
@ stub WRITE_PORT_BUFFER_USHORT
@ stdcall -arch=arm,arm64,i386 WRITE_PORT_UCHAR(ptr long)
@ stdcall -arch=arm,arm64,i386 WRITE_PORT_ULONG(ptr long)
@ stub WRITE_PORT_USHORT
