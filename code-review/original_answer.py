def CompareSwapSizeInMb(self, swap1, swap2):
    if self.OSType == "Linux":
        if swap1 < swap2:
            return False
    return True
