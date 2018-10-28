# A Django App Providing the `{% include_by_ajax %}` Template Tag

## The Problem

Start pages usually show data aggregated from different sections. To render a start page might take some time if the relations and filters are complex or if there are a lot of images. The best practice for performance is to display the content above the fold (in the visible viewport area) as soon as possible, and then to load the rest of the page dynamically by JavaScript.

## The Solution

This app allows you to organize heavy pages into sections which are included in the main page template. The default including can be done by the `{% include template_name %}` template tag and it is rendered immediately. We are introducing a new template tag `{% include_by_ajax template_name %}` which will initially render an empty placeholder, but then will load the content by Ajax dynamically.

The template included by `{% include_by_ajax template_name %}` will get all the context that would normally be passed to a normal `{% include template_name %}` template tag.

## Implementation Details

When you use the `{% include_by_ajax template_name %}`, the page is loaded and rendered twice: once it is loaded with empty placeholders `<section class="ajax-placeholder"></section>`. Then it is loaded by Ajax again, and the placeholders get the data rendered. When the second load is complete, JavaScript replaces all the placeholders with their content. In the end, 'include_by_ajax_all_loaded' event is triggered for the document so that you can further initialize JavaScript functions.

## Caveats

The templates that are included by `{% include_by_ajax template_name %}` should always wrap the content into a single html tag, like `<div>`, `<span>`, `<section>`, `<article>` or other.

## Installation and configuration

1. Install the library to your virtual environment:

    ```bash
    (venv)$ pip install django-include-by-ajax
    ```

2. Add `'include_by_ajax'` to `INSTALLED_APPS`.

3. In your base template, link to jQuery and `include_by_ajax.js`:

    ```html
    {% load staticfiles %}
    <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
    <script src="{% static 'include_by_ajax/js/include_by_ajax.js' %}" defer></script>
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
        {% include_by_ajax "gallery/includes/latest_pictures.html" %}
    {% endblock %}
    
    {% block js %}
        <script>
        $(document).on('include_by_ajax_all_loaded', function() {
            console.log('Now all placeholders are loaded and replaced with content');
        })
        </script>
    {% endblock %}    
    ```

5. Enjoy the faster appearing web page at a cup of hot ginger and lemon tea.
