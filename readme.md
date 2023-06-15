# Project Name : Blog Site

This project is a Django web application that allows users to create, view, and modify posts with comments.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:

## Usage

1. Run the development server:
2. Access the application in your web browser at `http://localhost:8000`.

## Features

The application includes the following features:

- **Home View**: Renders the homepage, displaying a list of posts ordered by their creation date. Users can create new posts using a form available on the page.

- **Post List View**: Renders a page displaying all the posts in the database. Each post is listed with its title, author, and creation date.

- **Post Detail View**: Renders a detailed view of a specific post. It displays the post's title, content, author, and creation date. Additionally, it shows the comments associated with the post and provides a form for users to add new comments.

- **Post Create View**: Allows authenticated users to create new posts. When a user submits the post creation form, the application saves the post and redirects the user to the post detail view of the newly created post.

- **Post Delete View**: Allows authenticated users to delete their own posts. If a user attempts to delete a post that they didn't create, they are redirected to the homepage. When a user deletes their own post, the application removes it from the database and redirects them to the homepage.

- **Post Modify View**: Allows authenticated users to modify their own posts. Users can access this view by clicking on the "Edit" button on a post's detail view. The view presents a form pre-filled with the current data of the post. After submitting the form, the application updates the post with the modified information.

- **Create Comment View**: Allows authenticated users to add comments to a specific post. Users can access the comment form on a post's detail view. After submitting the comment form, the application saves the comment and redirects the user back to the post's detail view, where the new comment is displayed.


