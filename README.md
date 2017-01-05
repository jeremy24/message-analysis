## message-analysis

### Purpose ###
These are a couple small scripts to process and clean the data I download 
from AWS Dynamo. Dynamo exports the data to backups in JSON but has an annoying
way to store the data types so these scripts go through and pull the data out and 
mash into into a standard message model

### TODO ##
- Finish get meta to add group and user meta data to images
- Add group data processor
- Add user data processor
- Add a cool way to build a graph relating users to phrases other users, phrases, and groups. 