# RESTful API 

> EdTube is a video streaming platform built with Django Restful & MySQL.

## Features

> CRUD (Create, Read, Update And Delete)

- Authentication with JWT (Reset Password with email)
  - Login (User/Admin)
  - Register
  - Forgot Password
- Pagination and search where necessary
- API Security (NoSQL Injections, XSS Attacks, http param pollution etc)
- Video (CRUD)
  - Upload video
  - Upload video thumbnail
  - Watch video
  - Increase Views
  - Like and dislike video
  - Download video
  - Comment & reply for video
  - Update video details
  - Delete video
- Subscribe to a channel
- View liked videos
- Trending
- Subscriptions
- History (CRUD)
  - Watch history
  - Search history
- Settings
  - Modify channel name and email
  - Change password
  - Upload channel avatar

## Frontend Repo

Frontend was developed with vue.js and ElementUI [EdTube](https://github.com/techreagan/vue-nodejs-youtube-clone)

## API Documentation

Extensive and testing documentation with postman: [VueTube API](https://documenter.getpostman.com/view/9407876/SzYaVdtC?version=latest)

## Database Model

[![Screenshot](https://github.com/techreagan/youtube-clone-nodejs-api/raw/master/screenshots/vue_tube_ERD.jpg)](https://github.com/techreagan/youtube-clone-nodejs-api/blob/master/screenshots/vue_tube_ERD.jpg)

## Requirement

- Django
- MySQL

## Configuration File

Rename the config/.env.example to .env, then modify to your environment variables, mongodb uri, set your JWT_SECRET and SMTP variables

```
NODE_ENV=development
PORT=3001

MONGO_URI=YOUR_URL

JWT_SECRET=YOUR_SECRET
JWT_EXPIRE=30d
JWT_COOKIE_EXPIRE=30

FILE_UPLOAD_PATH = ./public/uploads
MAX_FILE_UPLOAD = 1000000

SMTP_HOST=smtp.mailtrap.io
SMTP_PORT=2525
SMTP_EMAIL=
SMTP_PASSWORD=
FROM_EMAIL=noreply@quizapp.com
FROM_NAME=QuizzApp
```

Email testing: use mailtrap for email testing, it's easy no stress.

## Installation

Install all npm dependecies

```
npm install
```

Install nodemon globally

```
npm install -g nodemon
```

### Note

Make sure you run the seeder to get categories in your database or Create a user with the role admin, then add category with the category endpoint.

Run database seeder

- Seeder folder is _data/
- Edit the seeder file if you want to

```
node seeder -i
```

Delete all data

```
node seeder -d
```

## Start web server

```
node run dev
```

## Screenshots

### Sign In

[![Screenshot](https://github.com/techreagan/youtube-clone-nodejs-api/raw/master/screenshots/20%20-%20Sign%20in.jpg)](https://github.com/techreagan/youtube-clone-nodejs-api/blob/master/screenshots/20 - Sign in.jpg)

### Sign Up

[![Screenshot](https://github.com/techreagan/youtube-clone-nodejs-api/raw/master/screenshots/21%20-%20Sign%20up.jpg)](https://github.com/techreagan/youtube-clone-nodejs-api/blob/master/screenshots/21 - Sign up.jpg)

### Home Page

[![Screenshot](https://github.com/techreagan/youtube-clone-nodejs-api/raw/master/screenshots/1%20-%20Home.jpg)](https://github.com/techreagan/youtube-clone-nodejs-api/blob/master/screenshots/1 - Home.jpg)

### Watch Page

[![Screenshot](https://github.com/techreagan/youtube-clone-nodejs-api/raw/master/screenshots/7%20-%20Watch.jpg)](https://github.com/techreagan/youtube-clone-nodejs-api/blob/master/screenshots/7 - Watch.jpg)

### Upload Thumbnail Modal

[![Screenshot](https://github.com/techreagan/youtube-clone-nodejs-api/raw/master/screenshots/16%20-%20Upload%20Thumbnail%20Modal.jpg)](https://github.com/techreagan/youtube-clone-nodejs-api/blob/master/screenshots/16 - Upload Thumbnail Modal.jpg)