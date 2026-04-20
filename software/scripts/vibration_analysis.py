import numpy as np
from scipy.signal import butter, filtfilt

# --- CONFIGURATION ---
FS = 200 # Hz
WINDOW_SEC = 5
WINDOW_SIZE = FS * WINDOW_SEC
THRESHOLD = 0.05 # 5% shift
PERSISTENCE = 3 # Consecutive windows

def bandpass_filter(signal, fs, low=10, high=40, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, [low/nyq, high/nyq], btype='band')
    return filtfilt(b, a, signal)

def compute_rms(signal):
    return np.sqrt(np.mean(signal**2))

def detect_vibration_shift(signal):
    # 1. Filter signal
    filtered = bandpass_filter(signal, FS)
    
    # 2. Windowing
    n_windows = len(filtered) // WINDOW_SIZE
    rms_values = []
    for i in range(n_windows):
        window = filtered[i*WINDOW_SIZE:(i+1)*WINDOW_SIZE]
        rms = compute_rms(window)
        rms_values.append(rms)
    
    rms_values = np.array(rms_values)
    
    # 3. Baseline (First 3 windows)
    baseline = np.mean(rms_values[:3])
    
    # 4. Percentage change evaluation
    changes = (rms_values - baseline) / baseline
    
    # 5. Detection with persistence
    alarm = False
    counter = 0
    for i, change in enumerate(changes):
        if change >= THRESHOLD:
            counter += 1
            if counter >= PERSISTENCE:
                print(f"ALARM TRIGGERED - Window {i} | Change: {change*100:.2f}%")
                alarm = True
        else:
            counter = 0
            
    return {
        "rms": rms_values,
        "baseline": baseline,
        "change_percent": changes,
        "alarm": alarm
    }
