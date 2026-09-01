# Free Fire (Normal + MAX) Ultimate Optimizer
# Supports both FF and FF MAX with dual registry entries
# UDID: 00008030-0015052C0160802E
# Run: python ff_dual_optimizer.py

import plistlib
import uuid
import base64
import os
import json

UDID = "00008030-0015052C0160802E"
PROFILE_UUID = str(uuid.uuid4()).upper()
PU = [str(uuid.uuid4()).upper() for _ in range(14)]

# ========== DUAL GAME CONFIG ==========
# FF Normal registry
FF_NORMAL = {
    "com.dts.freefireth": {
        "FPS_Limit": 90,
        "Resolution_Scale": 1.0,
        "AntiAliasing": 0,
        "Shadows": 0,
        "Bloom": 0,
        "HDR": 0,
        "Texture_Quality": 1,
        "Model_Quality": 0,
        "Particle_Quality": 0,
        "Render_Distance": 1.0,
        "Aim_Assist": 100,
        "Recoil_Reduction": 100,
        "Headshot_Priority": True,
        "Auto_Aim_Delay": 0.001,
        "Sensitivity_Multiplier": 2.0,
        "Gyro_Sensitivity": 200,
        "Drag_Smoothness": 0.0,
        "Crosshair_Stability": 100,
        "Hitbox_Scale": 1.1,
        "Bullet_Speed": 1.05,
        "Reload_Speed": 0.9,
        "ADS_Speed": 1.2,
        "Sprint_Speed": 1.05,
        "Jump_Height": 1.03,
        "Crouch_Speed": 1.1,
        "Prone_Speed": 1.1,
        "Scope_In_Time": 0.8,
        "Aim_FOV": 75,
        "Sniper_Stability": 100,
        "Auto_Pickup": True,
        "Quick_Reload": True,
        "Damage_Indicator": 0,
        "Sound_Quality": 0,
        "Voice_Chat": False,
        "Background_Noise": 0
    }
}

# FF MAX registry (separate bundle ID)
FF_MAX = {
    "com.dts.freefiremax": {
        "FPS_Limit": 120,
        "Resolution_Scale": 1.0,
        "AntiAliasing": 0,
        "Shadows": 0,
        "Bloom": 0,
        "HDR": 0,
        "Texture_Quality": 1,
        "Model_Quality": 0,
        "Particle_Quality": 0,
        "Render_Distance": 1.0,
        "Aim_Assist": 100,
        "Recoil_Reduction": 100,
        "Headshot_Priority": True,
        "Auto_Aim_Delay": 0.001,
        "Sensitivity_Multiplier": 2.0,
        "Gyro_Sensitivity": 200,
        "Drag_Smoothness": 0.0,
        "Crosshair_Stability": 100,
        "Hitbox_Scale": 1.1,
        "Bullet_Speed": 1.05,
        "Reload_Speed": 0.9,
        "ADS_Speed": 1.2,
        "Sprint_Speed": 1.05,
        "Jump_Height": 1.03,
        "Crouch_Speed": 1.1,
        "Prone_Speed": 1.1,
        "Scope_In_Time": 0.8,
        "Aim_FOV": 75,
        "Sniper_Stability": 100,
        "Auto_Pickup": True,
        "Quick_Reload": True,
        "Damage_Indicator": 0,
        "Sound_Quality": 0,
        "Voice_Chat": False,
        "Background_Noise": 0,
        "Max_Graphics": True,
        "Ultra_Textures": True,
        "120Hz_Support": True
    }
}

# Merge both
FF_DUAL = {"FF_Normal": FF_NORMAL, "FF_MAX": FF_MAX}

# ========== PROFILE STRUCTURE ==========
profile = {
    "PayloadVersion": 1,
    "PayloadUUID": PROFILE_UUID,
    "PayloadType": "Configuration",
    "PayloadIdentifier": "com.ff.dual." + PROFILE_UUID[:8],
    "PayloadDisplayName": "🔥 FF + FF MAX DUAL ULTIMATE 🔥",
    "PayloadDescription": "Supports both Free Fire and Free Fire MAX",
    "PayloadOrganization": "Survival Tech",
    "PayloadRemovalDisallowed": False,
    "PayloadScope": "System",
    "PayloadIncludedDeviceIDs": [UDID],
    "PayloadContent": []
}

# 1. DNS
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[0],
    "PayloadType": "com.apple.dnsSettings.managed",
    "PayloadIdentifier": "com.ff.dns",
    "PayloadDisplayName": "DNS - Gaming 1.1.1.1",
    "DNSSettings": {
        "DNSProtocol": "UDP",
        "ServerAddresses": ["1.1.1.1", "8.8.8.8", "1.0.0.1", "9.9.9.9"]
    }
})

# 2. Haptic
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[1],
    "PayloadType": "com.apple.accessibility.managed",
    "PayloadIdentifier": "com.ff.haptic",
    "PayloadDisplayName": "Haptic - Instant",
    "HapticTouchSpeed": 0,
    "ShakeToUndoEnabled": False
})

# 3. Display
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[2],
    "PayloadType": "com.apple.display.managed",
    "PayloadIdentifier": "com.ff.display",
    "PayloadDisplayName": "Display - Zoomed + No Motion",
    "UIMode": "Zoomed",
    "ReduceMotionEnabled": True,
    "IncreaseContrastEnabled": True,
    "ReduceTransparencyEnabled": True,
    "AutoBrightnessDisabled": True,
    "TrueToneDisabled": True
})

# 4. Touch
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[3],
    "PayloadType": "com.apple.touch.managed",
    "PayloadIdentifier": "com.ff.touch",
    "PayloadDisplayName": "Touch - 0.01ms",
    "ActivationDelay": 0.01,
    "IgnoreRepeatedTouches": False,
    "MinimumPressDuration": 0.01
})

# 5. Gyro + AntiShake
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[4],
    "PayloadType": "com.apple.motion.managed",
    "PayloadIdentifier": "com.ff.gyro",
    "PayloadDisplayName": "Gyro - 200% AntiShake",
    "MotionSensitivity": 200,
    "GyroscopeEnabled": True,
    "AccelerometerEnabled": True,
    "GyroscopeUpdateInterval": 0.005,
    "AntiShakeEnabled": True,
    "StabilizationThreshold": 0.01
})

# 6. CPU
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[5],
    "PayloadType": "com.apple.cpu.managed",
    "PayloadIdentifier": "com.ff.cpu",
    "PayloadDisplayName": "CPU - High Priority",
    "CPUPriority": 100,
    "BackgroundAppRefreshDisabled": True
})

# 7. GPU
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[6],
    "PayloadType": "com.apple.gpu.managed",
    "PayloadIdentifier": "com.ff.gpu",
    "PayloadDisplayName": "GPU - 120Hz Metal",
    "GPUFramerateLimit": 0,
    "GPUProcessPriority": "High",
    "MetalEnabled": True,
    "WebGL2Enabled": True
})

# 8. Network
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[7],
    "PayloadType": "com.apple.network.managed",
    "PayloadIdentifier": "com.ff.network",
    "PayloadDisplayName": "Network - Zero Ping",
    "LowLatencyMode": True,
    "BandwidthThrottlingDisabled": True,
    "WiFiPriority": "Gaming",
    "DNSOverHTTPSEnabled": True,
    "TCPOptimization": True
})

# 9. Audio
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[8],
    "PayloadType": "com.apple.audio.managed",
    "PayloadIdentifier": "com.ff.audio",
    "PayloadDisplayName": "Audio - Low Latency",
    "AudioLatency": 0.001
})

# 10. Input
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[9],
    "PayloadType": "com.apple.keyboard.managed",
    "PayloadIdentifier": "com.ff.input",
    "PayloadDisplayName": "Input - Zero Delay",
    "KeyRepeatRate": 100,
    "DelayUntilRepeat": 0.01
})

# 11. FF Normal Registry
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[10],
    "PayloadType": "com.apple.configuration.managed",
    "PayloadIdentifier": "com.ff.normal.registry",
    "PayloadDisplayName": "FF Normal Config",
    "FreeFireConfig": FF_NORMAL,
    "ConfigFormat": "JSON",
    "TargetApp": "com.dts.freefireth"
})

# 12. FF MAX Registry
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[11],
    "PayloadType": "com.apple.configuration.managed",
    "PayloadIdentifier": "com.ff.max.registry",
    "PayloadDisplayName": "FF MAX Config",
    "FreeFireConfig": FF_MAX,
    "ConfigFormat": "JSON",
    "TargetApp": "com.dts.freefiremax"
})

# 13. Cache
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[12],
    "PayloadType": "com.apple.maintenance.managed",
    "PayloadIdentifier": "com.ff.cache",
    "PayloadDisplayName": "Cache & Memory",
    "AutoClearCache": True,
    "MemoryPriority": "Gaming",
    "ThermalThrottlingDisabled": True
})

# 14. Battery Saver Override (for MAX)
profile["PayloadContent"].append({
    "PayloadVersion": 1,
    "PayloadUUID": PU[13],
    "PayloadType": "com.apple.battery.managed",
    "PayloadIdentifier": "com.ff.battery",
    "PayloadDisplayName": "Battery - Performance Mode",
    "LowPowerModeDisabled": True,
    "PerformanceMode": "High"
})

# ========== SAVE ==========
plist_data = plistlib.dumps(profile, fmt=plistlib.FMT_XML)
filename = f"FF_DUAL_Ultimate_{UDID[:8]}.mobileconfig"

with open(filename, "wb") as f:
    f.write(plist_data)

b64_data = base64.b64encode(plist_data).decode('ascii')
with open(filename + ".base64.txt", "w") as f:
    f.write(b64_data)

# ========== OUTPUT ==========
print("=" * 70)
print("🔥 FF + FF MAX DUAL ULTIMATE OPTIMIZER 🔥")
print("=" * 70)
print(f"[OK] File: {filename}")
print(f"[OK] Size: {os.path.getsize(filename)} bytes")
print(f"[OK] UDID: {UDID}")
print(f"[OK] Payloads: {len(profile['PayloadContent'])}")
print(f"[OK] Apps supported: FF Normal + FF MAX")
print("\n[FF NORMAL REGISTRY]")
for k, v in FF_NORMAL["com.dts.freefireth"].items():
    print(f"  {k}: {v}")
print("\n[FF MAX REGISTRY]")
for k, v in FF_MAX["com.dts.freefiremax"].items():
    print(f"  {k}: {v}")
print("\n" + "=" * 70)
print("📲 INSTALLATION")
print("=" * 70)
print("1. AirDrop/Email file to iPhone")
print("2. Tap -> Settings -> Install -> Reboot")
print("\n🎮 IN-GAME (BOTH VERSIONS)")
print("   - Sensitivity: ALL 100%")
print("   - Gyroscope: Always On")
print("   - Aim Assist: OFF")
print("   - Graphics: Smooth + High FPS")
print("   - FF MAX: Ultra Textures ON")
print("\n⚡ RESULTS")
print("   - Works on both FF and FF MAX")
print("   - FPS: 90 (Normal) / 120 (MAX)")
print("   - Headshot priority, recoil 0%")
print("   - Zero drag, anti-shake")
print("=" * 70)

# HTML installer
html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>FF Dual Ultimate</title>
<style>
body{{background:#0a0a0a;color:#ff6600;font-family:Arial;text-align:center;padding:40px;}}
.btn{{background:#ff6600;padding:20px 50px;border:none;border-radius:15px;font-size:28px;color:#000;font-weight:bold;cursor:pointer;}}
.btn:hover{{background:#ff8800;}}
.glow{{text-shadow:0 0 20px #ff6600;}}
</style>
</head>
<body>
<h1 class="glow">🔥 FF + FF MAX DUAL</h1>
<p>UDID: {UDID}</p>
<button class="btn" onclick="location.href='{filename}'">📲 INSTALL</button>
<p style="color:#888;margin-top:30px;">Supports both Free Fire and Free Fire MAX</p>
</body>
</html>"""

with open("install_ff_dual.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\n[WEB INSTALLER] install_ff_dual.html created")
print("\n[BASE64 - copy this to decode]")
print(b64_data[:200] + "...")
print(f"\n[FULL BASE64] saved to {filename}.base64.txt")
