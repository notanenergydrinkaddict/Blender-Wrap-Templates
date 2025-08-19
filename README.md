# Blender-Wrap-Templates

My blender and wrap3 templates.

## Wrap3 Templates
- [`Genesis9/ExcludeWrap_EarsNoseMouth.json`](Genesis9/ExcludeWrap_EarsNoseMouth.json)
  - Excludes poly faces for Genesis 9 mesh:
    - Inner Ear (and canals)
    - Inner Nose
    - Eyeliner
    - Mouth Cavity

## Blender Scripts
- [`ExcludeFaces.py`](ExcludeFaces.py)
  - Script for Blender [2.93 LTS](https://download.blender.org/release/Blender2.93)-[3.6 LTS](https://download.blender.org/release/Blender3.6) to run headlessly to exclude faces from Wrap3 JSON.
  - Usage:
    ```powershell
    # `--factory-startup` to prevent of loading user addons
    blender.exe --factory-startup --background --python "<Path to ExcludeFaces.py>" -- "<input.obj>" "<output.obj>" "<faces.json>"
    ```
  - Example usage in Powershell
    ```powershell
    # `&` symbol is required to execute file in path
    # `--factory-startup` to prevent of loading user addons
    & "E:\blender_builds\blender-2.93.18-windows-x64\blender.exe" `
    --factory-startup --background --python `
    "E:\blender_builds\blender-2.93.18-windows-x64\ExcludeFaces.py" -- `
    "E:\models\Genesis9.obj" `
    "E:\models\Genesis9_Groups.obj" `
    "E:\models\ExcludeWrap_EarsNoseMouth.json"
    ```
