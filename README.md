## 🌐 Roblox Version Reference URLs

A complete list of useful Roblox URLs for retrieving version and deployment data. These are essential for tracking updates, validating executors, and patching tools.

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

> ✅ Pro Tip: Use these endpoints to automate your executor’s update detection logic or hook them into your web monitoring tools.
