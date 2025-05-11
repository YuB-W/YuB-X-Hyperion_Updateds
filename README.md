
# 🛡️ YuB-X Hyperion_Updateds

A powerful utility and dashboard for tracking Roblox WindowsPlayer version deployments — especially built for exploit developers and reverse engineers.  
Stay ahead of Hyperion updates. Patch faster. Detect silently.

---

## 🚀 What Is This?

**YuB-X Hyperion_Updateds** helps executor developers by instantly detecting new Roblox WindowsPlayer builds and their associated Hyperion changes.  
Roblox updates without warning — this repo ensures **you don’t get caught off guard**.

🧠 Built to monitor:
- Roblox deployment versions
- WindowsPlayer & Studio build hashes
- Hyperion module changes
- Manifest references for patch inspection
- Version compatibility APIs for update prediction

---

## 📡 Why This Matters

Hyperion is Roblox’s anti-cheat system. It updates frequently and silently.  
If you’re working on an injector, exploit loader, or memory patcher, **you need to know**:

- When Roblox pushes a new version
- What the new hash is
- Whether Hyperion structure changed
- How to grab manifests for analysis

This repo automates it all. It gives you the **first-mover advantage**.

---

## 🌐 Roblox Version Reference URLs

| 🔍 Purpose                        | 🌐 URL                                                                                                                                                | 📝 Description                                |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| 🔹 Current WindowsPlayer hash     | https://clientsettings.roblox.com/v2/client-version/WindowsPlayer                                                                                     | Most direct & public                          |
| 🔹 Current MacPlayer hash         | https://clientsettings.roblox.com/v2/client-version/MacPlayer                                                                                          | Mac version                                   |
| 🔹 Deploy history (raw)           | https://setup.rbxcdn.com/DeployHistory.txt                                                                                                             | Raw full changelog                            |
| 🔹 Setup version                  | https://setup.roblox.com/version                                                                                                                       | Most recently deployed (Windows)              |
| 🔹 Setup launcher                 | https://setup.roblox.com/RobloxPlayerLauncher.exe                                                                                                      | Official launcher                             |
| 🔹 Download redirect              | https://www.roblox.com/download/client                                                                                                                 | Redirect to setup                             |
| 🔹 Public manifest reference      | https://setup.rbxcdn.com/version-<HASH>-WindowsPlayerManifest.json                                                                                     | Requires known `<HASH>`, must spoof/proxy     |
| 🔹 Version display (Studio)       | https://clientsettings.roblox.com/v2/client-version/WindowsStudio64                                                                                   | Studio build hash                             |
| 🔹 Version compatibility API      | https://versioncompatibility.api.roblox.com/GetCurrentClientVersionUpload/?apiKey=76e5a40c-3ae1-4028-9f10-7c62520bd94f&binaryType=WindowsPlayer       | Unofficial API (still works)                  |

> 💡 Use these endpoints in your own scripts to automate detection, diff patches, or validate client signatures.

---

## 🧪 Example Output

Example from the tool after detecting a new version:

```
✅ New Roblox WindowsPlayer version found!
→ Version Hash: version-ff05edc617954c5b  
→ File Version: 0.672.0.6720706  
→ Deployment Time: 2025-05-06 08:34:35 AM  
→ You are using the latest version.
```

---

## 📁 Project Files

| File                     | Purpose                                  |
|--------------------------|------------------------------------------|
| `Hyperion_Updateds.html` | Web-based UI to show version data        |
| `updateds_info.py`       | Python backend for querying endpoints    |

---

## ⚒️ Use Cases

This tool is especially useful for:

- 🧷 Manual mappers needing new manifest files
- 🧬 Hyperion reverse engineering (e.g. CFG bypass)
- 🔩 Maintaining an exploit loader post-update
- 🔁 Integrating version checks into your executor’s backend
- ⚠️ Alerting users when an update breaks their tools

---

## 🧠 Built With

- Python `requests` for HTTP fetching
- HTML/CSS for frontend dashboard
- Clean logs and auto-formatting for GitHub visibility

---

## 💬 Community

Join our Discord for updates, contributions, and exploit dev discussions:  
[![Discord](https://img.shields.io/discord/112233445566778899?label=Join%20Discord&logo=discord&color=7289DA)](https://discord.gg/4BPuyNkGsc)

---

## 🧠 Author

Developed and maintained by [YuB-X](https://github.com/YuB-W)  
Website: [https://yub-x.com](https://yub-x.com)

---

## 🔐 Disclaimer

This tool is for educational and research purposes only.  
Use responsibly. No affiliation with Roblox Corporation.
