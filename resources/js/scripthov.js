$(document).ready(function() {
    $('ul').mouseenter(function() {
        $('ul').fadeTo('fast', 1)
    });
    $('ul').mouseleave(function() {
        $('ul').fadeTo('fast', 0.5)
    });
});
