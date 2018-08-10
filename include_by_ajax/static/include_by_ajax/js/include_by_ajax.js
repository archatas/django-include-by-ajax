jQuery(function($) {
    // 1. Check if there are placeholders
    let $placeholders = $('.ajax-placeholder');
    let placeholder_count = $placeholders.length;
    if (!placeholder_count) {
        return;
    }
    // 2. If yes, then load the same page with full_render=1 query parameter again by Ajax
    let url = location.href;
    if (url.indexOf('?') === -1) {
        url += '?include_by_ajax_full_render=1';
    } else {
        url += '&include_by_ajax_full_render=1';
    }
    // 3. For each placeholder in that jQuery object, populate the placeholder in the document with placeholder's content
    $placeholders.each(function(index, element) {
        $(this).load(url + ' .ajax-placeholder:eq(' + index + ')>', function(data) {
            $(this).replaceWith($(this).html());
            placeholder_count--;
            if (!placeholder_count) {
                // 4. Trigger a special event "include_by_ajax_all_loaded"
                $(document).trigger('include_by_ajax_all_loaded');
            }
        });
    });
});