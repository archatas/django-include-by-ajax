/*jshint esnext:true */
jQuery(function($) {
    // 1. Check if there are placeholders
    let $placeholders = $('.js-ajax-placeholder');
    let placeholder_count = $placeholders.length;
    if (!placeholder_count) {
        return;
    }
    // 2. If yes, then load the same page with full_render=1 query parameter again by Ajax
    let url = location.href.replace(/#.*/, '');
    if (url.indexOf('?') === -1) {
        url += '?include_by_ajax_full_render=1';
    } else {
        url += '&include_by_ajax_full_render=1';
    }
    // 3. Load the page again by Ajax and with additional parameter
    $.get(url, function(responseHTML) {
        // 4. For each placeholder fill in the content
        $('<div>').append($.parseHTML(responseHTML)).find('.js-ajax-placeholder>*').each(function(index, element) {
            $placeholders[index].replaceWith(element);
        });
        // 5. Trigger a special event "include_by_ajax_all_loaded"
        $(document).trigger('include_by_ajax_all_loaded');
    }, 'html');
});
