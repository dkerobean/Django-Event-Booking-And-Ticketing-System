<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>


<!-- ABOUT THE PROJECT -->
## About The Project
<!-- 
[![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This is a Django web application that allows users to see a list of events, order tickets, view event details and contact information for the organizer. Users also have the ability to follow and be followed by organizers.

Organizers have access to a dashboard where they can view detailed analysis of their event, add users who can manage their events, and add or delete events.


## Features
* User registration and authentication
* List of events with filters
* Event details with contact information for the organizer
* Ticket ordering system
* User can follow and be followed by organizers
* Organizer dashboard with event analysis and event management capabilities



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

You need to have eiter python or Docler installed 

### Installation


1. Install Docker 
2. Pull the Docker image from Docker Hub using the command:
   ```sh
   docker pull your-username/your-repo:latest
   ```
3. Run the Docker container using the command:
   ```sh
    docker run -p 8000:8000 your-username/your-repo:latest
   ```
4. Navigate to http://localhost:8000 in your web browser to access the application.

Without Docker
To run this app locally without Docker, you need to have Python and Django installed. Once you have these installed, follow the steps below:
1. Clone the repository:
 ```sh
   git clone https://github.com/<username>/discord-clone.git
   ```
   2. Navigate into the project directory:
   ```sh
   cd discord-clone
   ```
   3. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
   4. Activate the virtual environment:
   ```sh
   venv\Scripts\activate
   ```
   5. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
   6. Run migrations:
   ```sh
   python manage.py migrate
   ```
   7. Start the development server:
   ```sh
   python manage.py runserver
   ```
   8. Open your browser and navigate to http://localhost:8000 to view the app.




<!-- USAGE EXAMPLES -->
## Usage


Users
* Navigate to the home page to view a list of events
* Click on an event to view its details and contact information for the organizer
* Follow an organizer by clicking the follow button on their event details page
* Order tickets by selecting the desired quantity and clicking the order button
* Log in or register to access additional features such as following organizers and viewing order history

Organizers
* Log in to access the organizer dashboard
* View detailed analysis of your events including ticket sales and revenue
* Add users who can manage your events by clicking on the "Add Manager" button on the dashboard
* Add or delete events by clicking on the "Add Event" or "Delete Event" button on the dashboard



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

Dickson - dkerobean@gmail.com

Project Link: #




<!-- ACKNOWLEDGMENTS -->




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]:event.jpg
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 