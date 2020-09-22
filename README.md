[![pypi](https://img.shields.io/pypi/v/django-include-by-ajax.svg)](https://pypi.python.org/pypi/django-include-by-ajax/)

# A Django App Providing the `{% include_by_ajax %}` Template Tag

## The Problem

Start pages usually show data aggregated from different sections. To render a start page might take some time if the relations and filters are complex or if there are a lot of images. The best practice for performance is to display the content above the fold (in the visible viewport area) as soon as possible, and then to load the rest of the page dynamically by JavaScript.

## The Solution

This app allows you to organize heavy pages into sections which are included in the main page template. The default including can be done by the `{% include template_name %}` template tag and it is rendered immediately. We are introducing a new template tag `{% include_by_ajax template_name %}` which will initially render an empty placeholder, but then will load the content by Ajax dynamically.

The template included by `{% include_by_ajax template_name %}` will get all the context that would normally be passed to a normal `{% include template_name %}` template tag.

You can also pass a placeholder template which will be shown until the content is loaded. For this use `{% include_by_ajax template_name placeholder_template_name=placeholder_template_name %}`

## Implementation Details

When you use the `{% include_by_ajax template_name %}`, the page is loaded and rendered twice:

- At first, it is loaded and rendered minimally with empty placeholders `<section class="ajax-placeholder"></section>`.
- Then, some JavaScript loads it fully by Ajax and replaces placeholders with their content.

The templates that you include by Ajax can contain `<style>` and `<script>` tags which will be executed when loaded.

In the end, `'include_by_ajax_all_loaded'` event is triggered for the `document` so that you can further initialize JavaScript functions.

## Caveats

The templates that are included by `{% include_by_ajax template_name %}` should always wrap the content into a single html tag, like `<div>`, `<span>`, `<section>`, `<article>` or other.

## Requirements

The app works with Django 1.8+ on the server and jQuery 3.x in the frontend.

## Installation and Configuration

1. Install the library to your virtual environment:

    ```bash
    (venv)$ pip install django-include-by-ajax
    ```

2. Add `'include_by_ajax'` to `INSTALLED_APPS`.

3. In your base template, link to jQuery and `include_by_ajax.js`:

    ```html
    {% load static %}
    <script src="https://code.jquery.com/jquery-3.5.1.min.js" crossorigin="anonymous"></script>
    <script src="{% static 'include_by_ajax/js/include_by_ajax.min.js' %}" defer></script>
    ```
4. In your page template, load and use the template tag for all content that is below the visible area of the page.

    ```html
    {% extends "base.html" %}
    {% load include_by_ajax_tags %}
    
    {% block content %}
        <h1>My Website</h1>
        {% include "slideshows/includes/start_page_slideshow.html" %}
        <!-- the fold -->
        {% include_by_ajax "blog/includes/latest_blog_posts.html" %}
        {% include_by_ajax "news/includes/latest_news.html" %}
        {% include_by_ajax "gallery/includes/latest_pictures.html" placeholder_template_name="utils/loading.html" %}
    {% endblock %}
    
    {% block js %}
        <script>
        $(document).on('include_by_ajax_all_loaded', function() {
            console.log('Now all placeholders are loaded and replaced with content');
        })
        </script>
    {% endblock %}    
    ```

5. Enjoy the faster-appearing web page at a glass of gingerbread latte.

## Contributors

Thanks to everybody who contributed to this project:

[![Contributors](https://contributors-img.firebaseapp.com/image?repo=archatas/django-include-by-ajax)](https://github.com/archatas/django-include-by-ajax/graphs/contributors)

<!-- Contributors' list made with https://contributors-img.firebaseapp.com -->

## Projects Using django-include-by-ajax

![1st things 1st Logo](https://www.1st-things-1st.com/static/20191003061720/webapp/img/favicon/favicon-16x16.png) [Strategic prioritizer 1st things 1st](https://www.1st-things-1st.com/)

_If you are also using the app, don't hesitate to add your site to the list…_
