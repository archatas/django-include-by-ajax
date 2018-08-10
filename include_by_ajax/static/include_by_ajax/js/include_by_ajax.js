jQuery(function($) {
    // 1. Check if there are placeholders
    let placeholder_count = $('.ajax-placeholder').length;
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
    $('.ajax-placeholder').each(function(index, element) {
        $(this).load(url + ' .ajax-placeholder:eq(' + index + ')>', function() {
            placeholder_count --;
            if (!placeholder_count) {
                // 4. Trigger a special event "all_loaded"
                $(document).trigger('include_by_ajax_all_loaded');
            }
        });
    });
});