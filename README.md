# Chromecast-AirportWeather
Allows user to to change Ambient Mode screen on Chromecast to display live aviation weather maps

Initial Setup:
  This script uses Google Photos API to upload images to a designated Google Photos album. Then, using the Google Home app on your phone you can select to display the images in said album. 
  1. You will need to enable the Google Photos Library API on your Google Account. This will allow the script to access your Google Photos library. I suggest creating a dummy Google account for this purpose as the script will flood the account with maps over time. Follow instructions here: https://developers.google.com/photos/library/guides/get-started
  
  2. Step 1 should provide you with a credientials.json file. Save this file in the root folder of the py project.
  
  3. Select the images you would like displayed on Chromecast. Google Home requires at least 2 images to prevent burn-in. Digital sectional charts can be downloaded here: https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/vfr/
    Crop and save as .jpg in the root folder of the py project
    
  4. Map each desired airport on each image. You can do this with MS Paint (tutorial here: https://www.youtube.com/watch?v=opDBcwV8JRE). Note the airport name (KSEA, KPDX, etc) and each X,Y coordinate. These will be used to place the colored circles onto the image.
  
  5. Using a Python IDE (Pycharm is recommended) edit lines 74,75, 143, 144, 218, 219 of Upload.py with data from Step 4. The script is currently setup to display 3 images. If more/less are wanted, remove/add to Upload.py as appropriate.
  
  6. Change instances of TAC.jpg, TACUpdate.jpg, Seattle.png, SeattleUpdate.png, North.png, and NorthUpdate.png in Upload.py to images selected in Step 3.
  
  7. Create an album in your Google Photos account that the script will upload into. Google Library API will only allow the script to place images into an album that is created by the app itself. Run AlbumCreate.py. This will print the AlbumID of the newly created album. Edit lines 27, 42, 127, and 197 with the AlbumID.


Upload.py follows three steps:
  1. Finds mediaItemIDs of existing images in the Google Photos Album. 
  2. Removes images from the album.
  3. Edits jpgs and uploads to the album. (Google Photos API currently does not support deletion/overwriting of photos so this three step process is the workaround)
  
  To automate this, I used a Raspberry Pi running Raspbian. The script is ran every 5 minutes using CRON with the command python3 Upload.py
