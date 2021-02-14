<<<<<<< HEAD
# project1-ptp24
CS490 project 1. Fun stuff. For music discovery.
=======
## Externals/APIs used:
=======
  * Flask Framework
  * Python Request Library
  * Python Random Library
  * Python OS library
  * Python dotenv library
  * Spotify API
  * Google Fonts for CSS

Upon acquisition of the repo contents, one will need to run the main.py file, and then open it on the local host. If one wants to, they can also push it onto heroku. 
Before this, one needs to set up both a spotify and genius developer account and save their credentials in a .env file. I'd recommend saving them to the same variable as I did , otherwise we might have a problem. Do note, this is also required for genius tokens.

Add these to the .env file:
* export CLI_ID="value of your client id"
* export CLI_SEC="your client secret value"
* export Acc_Tok="The access token you generated from the genuis API management page"
* export Gen_ID="your genius id value"
* export Gen_Sec="your genius secret value"

## Problems encountered
=======
   
Most of my issues came with the genius API. The API doesn't seem very efficient and can often cause a cache miss because of timeouts. 
To counter this, I had to place a conditional in my html that reloads the page if this happens. It's a little sucky but it works.

## Future Plans
=======
  * Improve layout for site page.
  * Perhaps something to make the artists more random. Intent on depth searching with similar artists.
 
