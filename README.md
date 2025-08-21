# Blender-Wrap-Templates

My blender and wrap3 templates.

## Wrap3 Templates
### DAZ Studio

- [`Genesis 8.1 Male`](Genesis8.1/Male)
- [`Genesis 8.1 Female`](Genesis8.1/Female)
  - Excludes Mouth, Teeth, EyeMoisture, EyeSocket, Ear Canals, Nose
    ![](https://github.com/user-attachments/assets/f77c4102-e601-4e47-84d4-d6a839cb30ec)
- [`Genesis 9`](Genesis9)
  - Excludes Mouth, Inner Eyes, Ear Canals, Nose
    ![](https://github.com/user-attachments/assets/49747c09-6c6b-4670-a772-bf122cf299ba)


## Blender Scripts
- [`ExcludeFaces.py`](ExcludeFaces.py)
  - Script for Blender [2.93 LTS](https://download.blender.org/release/Blender2.93)-[3.6 LTS](https://download.blender.org/release/Blender3.6) to run headlessly to exclude faces from Wrap3 JSON.
  - Usage:
    ```powershell
    # `--factory-startup` to prevent of loading user addons
    blender.exe --factory-startup --background --python "<Path to ExcludeFaces.py>" -- "<input.obj> <output.obj> <faces.json or list.txt>"
    ```
  - Example usage in Powershell (single JSON)
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
  - Example usage of list files
    ```
    E:\models\G8.1_ExcludeWrap_EarsNoseMouthEyes.json
    E:\models\G8.1_ExcludeWrap_Fingernails.json
    E:\models\G8.1_ExcludeWrap_Toenails.json
    ```
    - Launching script
    ```powershell
    # `&` symbol is required to execute file in path
    # `--factory-startup` to prevent of loading user addons
    #
    # Filename can be anything as long it ends with `.txt`
    & "E:\blender_builds\blender-2.93.18-windows-x64\blender.exe" `
    --factory-startup --background --python `
    "E:\blender_builds\blender-2.93.18-windows-x64\ExcludeFaces.py" -- `
    "E:\models\Genesis8.1.obj" `
    "E:\models\Genesis8.1_Groups.obj" `
    "E:\models\WrapList.txt"
    ```
