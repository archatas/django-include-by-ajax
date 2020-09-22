/*jshint esnext:true, unused:false */
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
    $.ajax({
        async: true,
        url: url,
        dataType: 'html'
    }).done(function(responseHTML, textStatus) {
        // 4. For each placeholder fill in the content
        let scriptsStack = [];
        $('<div>').append($.parseHTML(responseHTML, document, true)).find('.js-ajax-placeholder>*').each(function(index, element) {
            // collect scripts to a stack
            let $element = $(element);
            $element.find('script').each(function() {
                scriptsStack.push($(this));
                // remove the script from the DOM,
                // so that it's not executed by jQuery with async: false
                $(this).remove();
            });

            $($placeholders[index]).replaceWith($element);
        });

        // 5. Load and execute each script from the stack one by one
        function executeNextScriptFromStack() {
            let $script = scriptsStack.shift();
            if ($script) {
                let src = $script.attr('src');
                if (src) {
                    $.ajax({
                        async: true,
                        url: src,
                        dataType: 'script'
                    }).done(function(script, textStatus) {
                        executeNextScriptFromStack();
                    }).fail(function(jqxhr, settings, exception) {
                        executeNextScriptFromStack();
                    });
                } else {
                    $.globalEval($script.html());
                    executeNextScriptFromStack();
                }
            } else {
                // 6. Trigger a special event "include_by_ajax_all_loaded"
                $(document).trigger('include_by_ajax_all_loaded');
            }
        }
        executeNextScriptFromStack();
    });
});
