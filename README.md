# Rojak - Data Centric Development Milestone Project
Rojak' is a Malaysian mixed fruit and vegetable salad, that is enjoyed by all races and ethinicities in Malaysia. Keyword: Mixed. It is also used on a colloquial basis to mean a multi-linguistic fashion of speaking. The picture above concisely sets an example on a sentence that is 'rojak'. This website serves as an open source anyone-can-edit dictionary of 'rojak'-applicable slangs commonly used in Malaysia.
<https://rojak-malaysian-slangs.herokuapp.com/>



## UX
The theme for the project is clean, minimalism, with a black-orange colour theme.

### User Stories

* As a language-enthusiast, I want to learn Malaysian slangs, so I can sound more local when I speak some of the Malaysian languages
* As a Malaysian citizen, I want to contribute to the list of Malaysian slangs, so Malaysians from other ethinicities and tourists can understand the local speak from different ethinicities more intimately
* As a member of an ethnic group in Malaysia, I want to help refine the definitions of some of the listed words in the website that's my mother tongue, so that the best meaning of a slang can be shared to people from other ethinicities with a different mother tongue
* As a knowledgable Malaysian, I want to correct any mistakes in the descriptions of the jargon shared, so the right information can be conveyed
* As a generally nice human being, I want to delete some words in the list, so that the list of words are always family-friendly and non-offensive and if the slang is not applicable anywhere in Malaysia


## Features
### Existing Features

1) /rojak landing page:
* Media responsive navigation bar that condenses the home, about, dictionary, contribute links into a collapsible button when viewed on a small iPad or a mobile device
* Interactive sidebar pull-out page displaying the home, about, dictionary, contribute links when collapsible button is clicked when website is viewed on a small viewing port
* Description on the contents of the website, what 'rojak' means, and link to view the dictionary of Malaysian slangs

2) dictionary.html page:
* Displays all the list of Malaysian slang words in a card format, with functional edit and delete buttons 
* Edit button links user to a form, which will post the corrected information for a particular word into the list of words (dictionary). A flash message will pop up after form submission to notify of the successful update. Dictionary updated as accordingly.
* At the edit form, a cancel button on the edit a slang form also available to link user back to the dictionary.
* Delete button when clicked will remove the card of the word, with its meaning and language category. Flash message will appear too, to notify deletion was successful.

3) add_slang.html page:
* User ushered to a "share a slang" form that will post the name of the slang, meaning and language origin into the database and showcase this into the dictionary in the website
* Flash message will appear to notify successful addition of the word into the database. Word added and it's details will appear in the dictionary.html page, to where the user is auto-redirected after submitting the form.

### Future Features

* Search bar that's working to look up for slangs
* User authentication so that the name of the contributor can also be listed in the cards containing the word and its descriptions
* Defensive design based on votes, to only remove a card for a word if downvotes surpassed a threshold


## Technologies Used
* [HTML5](https://www.w3.org/TR/2017/REC-html52-20171214/)

* [CSS3](https://www.w3.org/Style/CSS/)

* [Materialize Starter Template](https://materializecss.com/getting-started.html)

* [Materialize Formatting](https://materializecss.com/)

* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

  * Customised to make pages interactive to the user's actions

* [Git](https://git-scm.com/)

  * Used for version control and committing changes to GitHub.

* [GitHub](https://github.com/)

  * Used to host and publish my project files.

* [Heroku](https://www.google.com/search?q=heroku&rlz=1C5CHFA_enMY578MY580&oq=heroku&aqs=chrome.0.69i59l3j69i60l3j69i65l2.1102j0j4&sourceid=chrome&ie=UTF-8)

* [GitPod IDE](https://gitpod.io/)

  * The application I used to develop the project.

* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

* [Python](https://www.python.org/)

* [MongoDB](https://www.mongodb.com/)
  
  * Used to store website client input data, and for website admin to manually CRUD data

## Data Structure
![alt text](https://github.com/farahroslend/rojak/blob/master/static/media/data_structure.jpeg)


## Version Control
* Development of the website using the Gitpod IDE, launched by including `gitpod.io/#` at the beginning of the rojak Github repository, as prescribed by Github [here] (https://www.gitpod.io/docs/getting-started/)
* Accidentally installed a branched version of the repository in Gitpod farahroslend/gitpod-setup, thereby needing pull requests to merge the new versions of the codes with the master branch
* Used the following commands in the CLI in Gitpod to for version control:
    * `git add .`
    * `git commit -m "...insert comment here..."`
    * `git push`

## Testing 

### Tools
* W3C CSS Validation Service (https://jigsaw.w3.org/css-validator/).
* W3C Markup Validation Service (https://validator.w3.org/).
* JavaScript codes (https://jshint.com/)
* run `$ python3 -m http.server 8080` on Gitpod's CLI to preview website
* Used Google Chrome's Inspect Feature to improve layout design and troubleshoot bugs 

### Debugging
* Map loads perfectly on the landing page, panning into the Asia region with functional zoom in and out buttons
* Map displays all the markers for the diving spots, when webpage is loaded in all 3 viewing port sizes (large, medium, small), and the name of the location pops up when clicked 
* Marker pops up the names of the diving location with the link to a page with more details on the area, when clicked. Need to use `coordinate` in the javascript codes to view the OpenStreetMap coordinates to pin the location name pop up close to where the marker is. This code is removed after deployment.
* Links at the markers ushers user to the right section of the travel deals page 
* Links to external travel vendors works well
* Pop up closes when other markers or anywhere else are clicked 
* Navigation bar contents links to the right pages when clicked


### Media Responsiveness
* On large screens, nav bar displays all the contents it hosts in its div
* On small screens, the nav bar condenses the right half of the contents of its div into a collapsible button that pulls out a sidebar tab when clicked to view all the elements in the navbar
* Since the design of the website is minimalistic, there is not much need to significantly change the layout of the other divs


## Deployment
Narrating the process from the start to the end:
* Gitpod CLI
    * `$ pip3 freeze --local > requirements.txt`
    * `echo web : python app.py > Procfile`

* Heroku website
    * created new app 
    * connect with Github
    * settings -> reveal config vars -> input for the following keys: IP_POT, SECRET_KEY, MONGO_URI, MONGO_DBNAME and their respective keys

* Gitpod CLI
    * `git add requirement.txt`
    * `git commit -m "added requirement.txt "`
    * `git add Procfile`
    * `git commit -m "added Procfile"`
    * `git push"`

* Heroku website
    * enable auto deployment -> deploy branch  
    * [deployed Heroku app](https://rojak-malaysian-slangs.herokuapp.com/)


## Credits
### Content
From my own knowledge as a Malaysian familiar with the local colloquial.

### Media
Images were sourced from: [Google Images](https://twitter.com/Botanygeek/status/1063036281154879488/photo/1)

### Codes
* Used Bootstrap Materialise Start Up Template to set up the navigation bar and landing page, with some customisation to fit the theme of this project.
* Customisation of Code Institute's Flask Task Manager Project (followed Tim's lessons; not published yet in the CI website), to evolve the website into a functional open source online dictionary