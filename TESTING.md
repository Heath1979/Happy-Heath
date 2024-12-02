# Testing

This is the TESTING file for the [Happy Heath](https://happy-heath-3daa657fbb51.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## Testing Contents  
  
- [Testing](#testing)
  - [Testing Contents](#testing-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
    - [Known Bugs](#known-bugs)

## Validation

### HTML Validation

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

Due to using Jinja syntax such as '{% extends "base.html" %} I had to use a different approach to checking my HTML as the validator would show errors if copying the HTML direct from the files in the Happy Heath project. My method to check my HTML was as follows:

- Using the deployed version from Heroku I navigated to each page.
- Right clicking on the page brought up a options menu with the option to view the page source located at the bottom.
- The complete HTML code for that page will then appear in a separate window.
- Copy that code and paste into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, and then repeat the steps to revalidate.



## Bugs

| No. | Bug | Solved | Fix | Commit no. |
| --- | ---- | ----- | --- | ---------- |
| 1 | Comments not showing when full post opened up | Yes | Added approved line to Comments modal | 57188d7 |
| 2 | Blog for Harle.tech post had a white backing not aligned to rest of blog posts | Yes | Content had been copied in from a doc and imported backing with it. Re-wrote to clear | 3f31836 |
| 3 | Image and content disappeared on Harle.tech post after weblinks implemented | Yes | changed default tag for no available url to a <p> from <a> | 39a32d7 |
| 4 | Favicon not loading | Yes | Missed % at the end of the DTL tag | 54faba0 |
| 5 | Search functionality for posts caused site to crash | Yes | Function in views did not take into account that category and location are foreign keys | 63459b9 |
| 6 | add_post.html not loading for a logged in user on the post link | Yes | blogs/urls.py pathways needed to be re-ordered. Path to the page was initially added at the bottom of the list when should have been second in the list | 



