import os
import sys
import configparser
import shutil

# Read the path from the settings.ini file, create one if it doesn't exist
config = configparser.ConfigParser()
if os.path.exists('settings.ini'):
    config.read('settings.ini')
    fiveMDir = config.get('DEFAULT', 'fiveM_dir', fallback=None)
else:
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)
        fiveMDir = config.get('DEFAULT', 'fiveM_dir', fallback=None)

# If the path exists, delete the folder and its contents
if fiveMDir and os.path.exists(fiveMDir):
    fiveMCachePath = os.path.join(fiveMDir, 'cache')
    if os.path.exists(fiveMCachePath):
        print("Deleting FiveM cache folder...")
        shutil.rmtree(fiveMCachePath)
        print("Done!")
    else:
        print("Cache already deleted. Reload FiveM.")

# If the path is not found in the settings.ini file, prompt user for their FiveM directory path
if not fiveMDir:
    print("Please enter your FiveM directory path:")
    fiveMDir = input()

# If the path is valid, update the settings.ini file
if os.path.exists(fiveMDir):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'fiveM_dir': fiveMDir}
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)
        # After it creates the settings.ini file, keep the script running and delete the cache folder
        if fiveMDir and os.path.exists(fiveMDir):
            fiveMCachePath = os.path.join(fiveMDir, 'cache')
            if os.path.exists(fiveMCachePath):
                print("Deleting FiveM cache folder...")
                shutil.rmtree(fiveMCachePath)
                print("Done!")
            else:
                print("-------------------------")
else:
    print("Path not valid. Please try again.")

sys.exit()