def adjust_signal(congestion_level):
    if congestion_level > 0.7:
        return "Extend green time by 30s"
    elif congestion_level < 0.3:
        return "Reduce green time by 15s"
    else:
        return "Maintain default timing"

# Example
print(adjust_signal(0.8))
