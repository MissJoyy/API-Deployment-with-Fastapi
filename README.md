

<a name="readme-top"></a>

<div align="center">
<h1><b>FastAPI Deployment with Docker</b></h1>
</div>

<!-- TABLE OF CONTENTS -->
- [📗 Table of Contents](#-table-of-contents)
  - [About the project](#about-the-project)
  - [🛠 Built With](#-built-with-)
    - [Tech Stack](#tech-stack)
  - [💻 Getting Started](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
  - [👥 Authors](#-authors-)
  - [🔭 Future Features](#-future-features-)
  - [🤝 Contributing](#-contributing-)
  - [🙏 Acknowledgments](#-acknowledgments-)
  - [📝 License](#-license)

<!-- ABOUT THE PROJECT -->
## About The Project

This project demonstrates how to deploy a **FastAPI** application using **Docker**. The application runs a simple FastAPI app that can be easily containerized using Docker for deployment. FastAPI is a modern, fast web framework that is designed for building APIs with Python 3.7+.

### Features
- A simple API with one endpoint that returns a JSON response.
- Dockerized environment for easy deployment and scaling.
- Interactive API documentation via Swagger and ReDoc.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<details>
<summary>Backend</summary>
  <ul>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
    <li><a href="https://www.docker.com/">Docker</a></li>
  </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project, you will need:

- **Python 3.7+**
- **Docker**



### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/MissJoyy/API-Deployment-with-Fastapi.git
```

Change into the cloned repository

```sh
  cd     API deployment with Fastapi
  
```

Create a virtual environment

```sh

python -m venv venv

```

Activate the virtual environment

```sh
    venv/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```


### Usage

To run the project, execute the following commands:

1.Running Locally (without Docker):

uvicorn app.main:app --reload

2.Running with Docker:

docker build -t fastapi-app .

3.Build the Docker image:

docker run -d -p 8000:8000 fastapi-app





Run the Docker container:


docker run -d -p 8000:8000 fastapi-app

The app should now be accessible at http://127.0.0.1:8000.



   

<!-- AUTHORS --> 


## 👥 Authors <a name="authors"></a>




🕵🏽‍♀️**Joy Apaloo**

- GitHub: [GitHub Profile](https://github.com/MissJoyy)
- LinkedIn: [LinkedIn Profile](linkedin.com/in/joy-apaloo-0b71791a7)
- Email: [Email](apaloojoy@gmail.com)
- Article: [Article](https://medium.com/@apaloojoy/building-a-machine-learning-api-with-fastapi-a-journey-from-model-to-deployment-61d417ce522f)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>



  
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to thank all the free available resource made available online.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
