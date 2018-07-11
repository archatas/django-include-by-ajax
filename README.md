# Idea for the `{% include_by_ajax %}` template tag in Django

## The Problem

Home pages of websites usually show data aggregated from different sections. To render a homepage might take some time if the relations and filters are complex or if there are a lot of images.

## The Solution

I have an idea how to speed up the initial page load by delaying the rendering of some parts of the page (for example, those which are bellow the fold). This could be done by a new third-party app with a template tag `{% include_by_ajax template_name %}`. This template tag would work similarly like `{% include template_name %}`, but instead of the content in the page, it would render placeholders, and then by Ajax call it would access the same page again, load it with all content rendered, and would dynamically fill in the missing content to the main page.

## Implementation Details

Getting deeper into the details, `{% include_by_ajax %}` would check if `request.is_ajax()` and some special variable is set, e.g. `request.GET['full_render'] == 1`. In that case it would behave similarly like `{% include template_name %}`, but maybe it would wrap the content into some `<div>` with special css classes or data attributes. Otherwise, it would render just an empty `<div>` with special css classes or data attributes.

Each template with `{% include_by_ajax %}` template tags should also load a special jQuery script, which after page load checks for placeholders, loads the same page again by Ajax call with `?full_render=1` query parameter, and would populate the content to the placeholders from the loaded page.

So to summarize, the workflow would be as follows:

1. If it's a usual request to a page, all `{% include_by_ajax %}` template tags would render placeholders.
2. On page load, a JavaScipt would check if there are any placeholders in the page and then would load the same page as an Ajax call with `?full_render=1` added to the query parameters.
3. In the Ajax call, the page would include all content for `{% include_by_ajax %}` template tag.
4. The JavaScript would load the HTML into a jQuery variable and then would find all contents in placeholders and would replace the placeholders in the original page with those contents.
5. The JavaScript would trigger some custom event, that allowed doing something with the loaded HTML.

## More

Also it would be interesting to benchmark some specific websites how much faster would the pages load with this technique.
