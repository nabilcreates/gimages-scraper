# gimages-scraper
> Scrape images from Google Images

## Current limitations:
-   Limit of 20 Images
-   Saves only the thumbnail of the image

# Usage
```bash
source bin/activate # Starts the Virtual Environment
pip install -f requirements.txt # Install all the required libraries
python3 app.py <search_query> # Run the app where search_query is user defined
```

The code above will run and once finished, all the images will be saved at the folder './output_images' and numbered from 0 to 20. All images will be default '.jpg'

# Roadmap
-   Hopefully to remove the 20 Images Limit
-   Custom path saving
-   High quality images saving
-   jpg and png selection in saving (Most likely this will not come true)

# Things that will not be in the Roadmap
-   Custom filenames